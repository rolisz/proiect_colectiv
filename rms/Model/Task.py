from sqlalchemy.schema import Column
import sqlalchemy.types
from camelot.admin.entity_admin import EntityAdmin
from camelot.core.orm import Entity, ManyToOne
from sqlalchemy import Unicode, Date, Integer, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey


class Task(Entity):
    __tablename__ = 'taskuri'

    id_faza = Column(Integer, ForeignKey('faze_activitati.id'))
    nume = Column(Unicode(30), nullable=False)
    descriere = Column(Unicode(200), nullable=False)
    desfasurat = Column(Boolean, nullable=False)
    faze_activitate = relationship('FazeActivitate')
    membrii = ManyToOne("ResurseUmane", inverse="taskuri")

    def __unicode__(self):
        return self.faze_activitate or 'Unknown'

    class Admin(EntityAdmin):
        verbose_name = 'Task'
        verbose_name_plural = 'Taskuri'
        list_display = ['id', 'id_faza', 'nume', 'descriere']
