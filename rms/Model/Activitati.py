from sqlalchemy.schema import Column
import sqlalchemy.types
from camelot.admin.entity_admin import EntityAdmin
from camelot.core.orm import Entity
from sqlalchemy import Unicode, Date, Integer, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey
import EchipaActivitate,MembriActivitate

class Activitati(Entity):

	__tablename__ = 'activitati'

	id = Column(Integer, primary_key=True)
	id_coordonator = Column(Integer,nullable=False)
	tip = Column(Integer, nullable=False)
	aprobata = Column(Boolean, nullable=False)
	
	echipa_activitate = relationship('EchipaActivitate')
	membri_activitate = relationship('MembriActivitate')

	def __unicode__(self):
		return self.echipa_activitate or 'Unknown'

	class Admin(EntityAdmin):
		verbose_name = 'Activitati'
		list_display = ['id','id_coordonator','tip','aprobata']
