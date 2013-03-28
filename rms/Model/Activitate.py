from sqlalchemy.schema import Column
import sqlalchemy.types
from camelot.admin.entity_admin import EntityAdmin
from camelot.core.orm import Entity
from sqlalchemy import Unicode, Date, Integer, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey

class Activitate(Entity):

	__tablename__ = 'activitati'

	id_coordonator = Column(Integer,nullable=False)
	tip = Column(Integer, nullable=False)
	aprobata = Column(Boolean, nullable=False)

	echipa_activitate = relationship('EchipaActivitate') 
	faze_activitate = relationship('FazeActivitate')
	resurse_activitate = relationship('ResurseActivitate')

	def __unicode__(self):
		return self.echipa_activitate or 'Unknown'

	class Admin(EntityAdmin):
		verbose_name = 'Activitate'
		verbose_name_plural = 'Activitati'
		list_display = ['id_coordonator','tip','aprobata']
