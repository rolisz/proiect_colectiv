from sqlalchemy.schema import Column
import sqlalchemy.types
from camelot.admin.entity_admin import EntityAdmin
from camelot.core.orm import Entity
from sqlalchemy import Unicode, Date, Integer, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey

class ResurseUmane(Entity):

    __tablename__ = 'resurse_umane'

    username = Column(Unicode(30))
    nume = Column(Unicode(50), nullable=False)
    doctorat = Column(Boolean, nullable=False)
    functie = Column(Unicode(30), nullable=True)
    echipa_activitate = relationship('EchipaActivitate')
    membru_task = relationship('MembruTask')
    def __unicode__(self):
        return self.echipa_activitate or 'Unknown'
        
    class Admin(EntityAdmin):
        verbose_name = 'ResurseUmane'
        verbose_name_plural ='ResurseUmane'
        list_display = ['username', 'nume','doctorat','functie']