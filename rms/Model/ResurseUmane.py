from sqlalchemy.schema import Column
import sqlalchemy.types
from camelot.admin.entity_admin import EntityAdmin
from camelot.core.orm import Entity
from sqlalchemy import Unicode, Date, Integer, Boolean, String
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey


class ResurseUmane(Entity):
    __tablename__ = 'resurse_umane'

    username = Column(String(30))
    nume = Column(String(50))
    doctorat = Column(Boolean)
    functie = Column(String(30))

    __mapper_args__ = {
        'polymorphic_on': functie,
    }

    def __unicode__(self):
        return self.nume or 'Unknown'

    class Admin(EntityAdmin):
        verbose_name = 'ResurseUmane'
        verbose_name_plural = 'ResurseUmane'
        list_display = ['username', 'nume', 'doctorat', 'functie']


class Student(ResurseUmane):
    __tablename__ = None

    __mapper_args__ = {
        'polymorphic_identity': 'Student'
    }


class Profesor(ResurseUmane):
    __tablename__ = None

    materii = relationship('Discipline')
    ore_suplimentare = relationship('OreSuplimentare')

    poz = Column(Integer)
    den_post = Column(String(20))
    den_functie = Column(String(20))
    titular = Column(Boolean())

    def __init__(self, poz=None, den_post=None, nume=None,den_functie=None, titular=None):
        if poz:
            self.poz = poz
            self.den_post = den_post
            self.nume = nume
            self.den_functie = den_functie
            self.titular = titular == 'Tit'
        #super(ResurseUmane).__init__()

    __mapper_args__ = {
        'polymorphic_identity': 'Profesor'
    }