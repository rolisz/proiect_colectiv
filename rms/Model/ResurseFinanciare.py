from camelot.admin.action import Action, ActionStep
from camelot.admin.not_editable_admin import not_editable_admin
from sqlalchemy.schema import Column
import sqlalchemy.types
from camelot.admin.entity_admin import EntityAdmin
from camelot.core.orm import Entity, ManyToOne, Session
from sqlalchemy import Unicode, Date, Integer, Boolean, String

#todo dropdown pt categorii

class ResurseFinanciare(Entity):
    __tablename__ = 'resurse_financiare'

    valoare = Column(Integer, nullable=False)
    categorie = Column(Unicode(50))
    activitate = ManyToOne("Activitate")

    def __unicode__(self):
        return self.categorie or 'Unknown'

    class Admin(EntityAdmin):
        verbose_name = 'Resursa Financiara'
        verbose_name_plural = 'Resurse Financiare'
        list_display = ['valoare', 'categorie']
        field_attributes = {
            'valoare': {'minimum': 0, 'maximum': 50000},
            'categorie': {'choices': lambda o: [('Salarii', 'Salarii'), ('Mobilitati', 'Mobilitati'),
                                                ('Cheltuieli logistice', 'Cheltuieli logistice')],
                          'default': 'Salarii'}
        }



# class Venituri(ResurseFinanciare):
#     __tablename__ = None
#
#     __mapper_args__ = {
#         'polymorphic_identity': 'venituri'
#     }
#
#     class Admin(EntityAdmin):
#         verbose_name = 'Venituri'
#         verbose_name_plural = 'Venituri'
#         list_display = ['valoare', 'categorie']


