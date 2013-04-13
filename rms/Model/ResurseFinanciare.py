from camelot.admin.action import Action, ActionStep
from sqlalchemy.schema import Column
import sqlalchemy.types
from camelot.admin.entity_admin import EntityAdmin
from camelot.core.orm import Entity, Session
from sqlalchemy import Unicode, Date, Integer, Boolean, String
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey


class ResurseFinanciare(Entity):
    __tablename__ = 'resurse_financiare'

    valoare = Column(Integer)
    tip =  Column('type',String(10))
    categorie = Column(Unicode(30))
    __mapper_args__ = {
        'polymorphic_on': tip,
        }

    def __unicode__(self):
        return self.categorie + str(self.valoare if self.tip else -self.valoare) or 'Unknown'

    class Admin(EntityAdmin):
        verbose_name = 'ResurseFinanciare'
        verbose_name_plural = 'ResurseFinanciare'
        list_display = ['valoare', 'categorie']

        def get_query(self):
            session = Session
            return session.query(ResurseFinanciare).filter_by(tip='venituri')

    class Admin2(EntityAdmin):
        verbose_name = 'ResurseFinanciare'
        verbose_name_plural = 'ResurseFinanciare'
        list_display = ['valoare', 'categorie']


        def get_query(self):
            session = Session
            return session.query(ResurseFinanciare).filter_by(tip='cheltuieli')

class Venituri(ResurseFinanciare):
    __tablename__ = None

    __mapper_args__ = {
       'polymorphic_identity': 'venituri'
    }

    class Admin(EntityAdmin):
        verbose_name = 'Venituri'
        verbose_name_plural = 'Venituri'
        list_display = ['valoare', 'categorie']


class Cheltuieli(ResurseFinanciare):
    __tablename__ = None

    __mapper_args__ = {
        'polymorphic_identity': 'Cheltuieli'
    }

    class Admin2(EntityAdmin):
        verbose_name = 'Cheltuieli'
        verbose_name_plural = 'Cheltuieli'
        list_display = ['valoare', 'categorie']


