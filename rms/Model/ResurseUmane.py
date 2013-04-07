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
    nume = Column(Unicode(50))
    doctorat = Column(Boolean)
    functie = Column(Unicode(30))

    def __unicode__(self):
        return self.nume or 'Unknown'

    class Admin(EntityAdmin):
        verbose_name = 'ResurseUmane'
        verbose_name_plural = 'ResurseUmane'
        list_display = ['username', 'nume', 'doctorat', 'functie']
