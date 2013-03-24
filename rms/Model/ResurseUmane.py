from sqlalchemy.schema import Column
import sqlalchemy.types
from camelot.admin.entity_admin import EntityAdmin
from camelot.core.orm import Entity
from sqlalchemy import Unicode, Date, Integer, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey

class ResurseUmane(Entity):

    __tablename__ = 'resurse_umane'

    username = Column(Unicode(30), primary_key=True)
    nume = Column(Unicode(50), nullable=False)
    doctorat = Column(Boolean, nullable=False)
    functie = Column(Unicode(30), nullable=True)

    def __unicode__(self):
        return self.name or 'Unknown'
        
    class Admin(EntityAdmin):
        verbose_name = 'ResurseUmane'
        list_display = ['username', 'name','doctorat','functie']