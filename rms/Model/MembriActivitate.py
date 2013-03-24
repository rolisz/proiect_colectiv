from sqlalchemy.schema import Column
import sqlalchemy.types
from camelot.admin.entity_admin import EntityAdmin
from camelot.core.orm import Entity
from sqlalchemy import Unicode, Date, Integer, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey
import Activitati,EchipaActivitate

class MembriActivitate(Entity):

	__tablename__ = 'membri_activitate'

	id_activitate = Column(Integer, ForeignKey('activitati.id'))
	id_membru = Column(Integer, ForeignKey('echipa_activitate.id_membru'))
	
	activitate = relationship('Activitati')
	echipa_activitate = relationship('EchipaActivitate')

	def __unicode__(self):
		return self.activitate or 'Unknown'

	class Admin(EntityAdmin):
		verbose_name = 'MembriActivitate'
		list_display = ['id_activitate','id_membru']
