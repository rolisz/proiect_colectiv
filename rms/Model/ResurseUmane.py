from camelot.admin.not_editable_admin import not_editable_admin
from sqlalchemy.schema import Column
import sqlalchemy.types
from camelot.admin.entity_admin import EntityAdmin
from camelot.core.orm import Entity, ManyToMany, OneToMany
from sqlalchemy import Unicode, Date, Integer, Boolean, String
from sqlalchemy.schema import ForeignKey

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

    class Admin2(EntityAdmin):
        verbose_name = 'Resursa Umane'
        verbose_name_plural = 'Resurse Umane'
        list_display = ['username', 'nume', 'doctorat', 'functie']

    Admin2 = not_editable_admin(Admin2)


class Student(ResurseUmane):
    __tablename__ = None

    __mapper_args__ = {
        'polymorphic_identity': 'Student'
    }
    class Admin(EntityAdmin):
        verbose_name = 'Student'
        verbose_name_plural = 'Studenti'
        list_display = ['username', 'nume', 'doctorat']


class Profesor(ResurseUmane):
    __tablename__ = None

    # materii = relationship('Discipline')
    # ore_suplimentare = relationship('OreSuplimentare')

    den_post = Column(String(20))
    den_functie = Column(String(20))
    titular = Column(Boolean())

    # def __init__(self, poz=None, den_post=None, nume=None, den_functie=None, titular=None):
    #     if poz:
    #         self.den_post = den_post
    #         self.nume = nume
    #         self.den_functie = den_functie
    #         self.titular = titular == 'Tit'
    #         #super(ResurseUmane).__init__()

    __mapper_args__ = {
        'polymorphic_identity': 'Profesor'
    }
    class Admin(EntityAdmin):
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesori'
        list_display = ['username', 'nume', 'doctorat', 'den_post', 'den_functie', 'titular']


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

#todo adaugat alte tipuri de resurse umane gen om de serivic, secretara, etc

#todo cadru auxiliar
