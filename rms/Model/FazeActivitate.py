from sqlalchemy.schema import Column
import sqlalchemy.types
from camelot.admin.entity_admin import EntityAdmin
from camelot.core.orm import Entity
from sqlalchemy import Unicode, Date, Integer, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey

class FazeActivitate(Entity):

	__tablename__ = 'faze_activitate'

	id_activitate = Column(Integer,ForeignKey('activitati.id'))
	nume = Column(Unicode(30), nullable=False)
	descriere = Column(Unicode(200), nullable=False)
	data_inceput = Column(Date,nullable=False)
	data_sfarsit = Column(Date,nullable=False)
	
	task = relationship('Task')
	activitati = relationship('Activitati')
	def __unicode__(self):
		return self.task or 'Unknown'

	class Admin(EntityAdmin):
		verbose_name = 'FazeActivitate'
		verbose_name_plural = 'FazeActivitati'
		list_display = ['id_activitate','nume','descriere','data_inceput','data_sfarsit']
