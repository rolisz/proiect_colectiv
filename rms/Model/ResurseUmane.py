from camelot.admin.not_editable_admin import not_editable_admin
from camelot.view.forms import Form, TabForm
from sqlalchemy.schema import Column
import sqlalchemy.types
from camelot.admin.entity_admin import EntityAdmin
from camelot.core.orm import Entity, ManyToMany, OneToMany, OneToOne, ManyToOne
from sqlalchemy import Unicode, Date, Integer, Boolean, String
from sqlalchemy.schema import ForeignKey
from rms.Model.Discipline import Discipline
from rms.Model.OreSuplimentare import OreSuplimentare
from rms.Views.Rapoarte import RaportResurseUmane


class ResurseUmane(Entity):
    __tablename__ = 'resurse_umane'
    username = Column(String(30), nullable=False)
    nume = Column(String(50))
    doctorat = Column(Boolean)
    functie = Column(String(30))

    activitati = ManyToMany('Activitate')
    activitati_coordonate = OneToMany('Activitate')

    taskuri = OneToMany("Task", inverse="membrii")
    __mapper_args__ = {
        'polymorphic_on': functie,
    }

    def __unicode__(self):
        return self.nume or 'Unknown'

    class Admin(EntityAdmin):
        verbose_name = 'Resurse Umane'
        verbose_name_plural = 'Resurse Umane'
        list_display = ['username', 'nume', 'doctorat', 'functie']
        field_attributes = {
            'functie': {'choices': lambda o: [('Profesor', 'Profesor'), ('Director', 'Director'),
                                              ('Administrator', 'Administrator')],
                        'default': 'Profesor'}
        }
        form_actions = [RaportResurseUmane()]

    AdminPublic = not_editable_admin(Admin, actions=False)


# class Student(ResurseUmane):
#     __tablename__ = None
#
#     __mapper_args__ = {
#         'polymorphic_identity': 'Student'
#     }
#     class Admin(EntityAdmin):
#         verbose_name = 'Student'
#         verbose_name_plural = 'Studenti'
#         list_display = ['username', 'nume', 'doctorat']


class Profesor(ResurseUmane):
    __tablename__ = None

    materii = OneToMany('Discipline')
    ore_suplimentare = OneToMany('OreSuplimentare') # todo should do something about this

    den_post = Column(String(20))
    den_functie = Column(String(20))
    titular = Column(Boolean())

    def __init__(self, user=None, den_post=None, nume=None, den_functie=None, titular=None):
        if user:
            self.username = user
            self.den_post = den_post
            self.nume = nume
            self.den_functie = den_functie
            self.titular = titular == 'Tit'
        super(Profesor, self).__init__()
        self.doctorat = True

    __mapper_args__ = {
        'polymorphic_identity': 'Profesor'
    }

    class Admin(EntityAdmin):
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesori'
        list_display = ['username', 'nume', 'den_post', 'den_functie', 'titular']
        form_display = TabForm([('Date personale', Form(['username', 'nume', 'den_post', 'den_functie', 'titular'])),
                                ('Materii predate', Form(['materii'])),
                                ('Ore suplimentare', Form(['ore_suplimentare']))
        ])
        field_attributes = {
            'den_post': {'name': 'Denumire post'},
            'den_functie': {'name': 'Denumire functie'},
            'materii': {'admin': Discipline.AdminProf},
            'ore_suplimentare': {'admin': OreSuplimentare.AdminProf},

        }


class Administrator(ResurseUmane):
    __tablename__ = None

    __mapper_args__ = {
        'polymorphic_identity': 'Administrator'
    }

    class Admin(EntityAdmin):
        verbose_name = 'Administrator'
        verbose_name_plural = 'Administratori'
        list_display = ['username', 'nume']


class Director(ResurseUmane):
    __tablename__ = None

    __mapper_args__ = {
        'polymorphic_identity': 'Director'
    }

    class Admin(EntityAdmin):
        verbose_name = 'Director'
        verbose_name_plural = 'Directori'
        list_display = ['username', 'nume']


# class ResurseAuxiliare(ResurseUmane):
#     __tablename__ = None
#
#     __mapper_args__ = {
#         'polymorphic_identity': 'Resurse Auxiliare'
#     }
#
#     class Admin(EntityAdmin):
#         verbose_name = 'Resurse Auxiliare'
#         verbose_name_plural = 'Resurse Auxiliare'
#         list_display = ['username', 'nume']
#todo adaugat alte tipuri de resurse umane gen om de serivic, secretara, etc

#todo cadru auxiliar
