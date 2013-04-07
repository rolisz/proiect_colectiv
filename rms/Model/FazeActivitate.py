from sqlalchemy.schema import Column
import sqlalchemy.types
from camelot.admin.entity_admin import EntityAdmin
from camelot.core.orm import Entity
from sqlalchemy import Unicode, Date, Integer, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey


class FazeActivitate(Entity):
    __tablename__ = 'faze_activitati'

    id_activitate = Column(Integer, ForeignKey('activitati.id'))
    nume = Column(Unicode(30))
    descriere = Column(Unicode(200))
    data_inceput = Column(Date)
    data_sfarsit = Column(Date)

    task = relationship('Task')
    activitate = relationship('Activitate')

    def __unicode__(self):
        return self.task or 'Unknown'

    class Admin(EntityAdmin):
        verbose_name = 'FazeActivitate'
        verbose_name_plural = 'FazeActivitati'
        list_display = ['activitate', 'nume', 'descriere', 'data_inceput', 'data_sfarsit']
