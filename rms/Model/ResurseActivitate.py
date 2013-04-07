from sqlalchemy.schema import Column
import sqlalchemy.types
from camelot.admin.entity_admin import EntityAdmin
from camelot.core.orm import Entity
from sqlalchemy import Unicode, Date, Integer, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey


class ResurseActivitate(Entity):
    __tablename__ = 'resurse_activitati'

    id_activitate = Column(Integer, ForeignKey('activitati.id'))
    id_resursa = Column(Integer, nullable=False)
    tip = Column(Integer, nullable=False)

    activitate = relationship('Activitate')

    def __unicode__(self):
        return self.activitate or 'Unknown'

    class Admin(EntityAdmin):
        verbose_name = 'ResurseActivitate'
        verbose_name_plural = 'ResurseActivitati'
        list_display = ['activitate', 'id_resursa', 'tip']
