from sqlalchemy.schema import Column
import sqlalchemy.types
from camelot.admin.entity_admin import EntityAdmin
from camelot.core.orm import Entity
from sqlalchemy import Unicode, Date, Integer, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey

class EchipaActivitate(Entity):

	__tablename__ = 'echipa_activitate'

	id_grant = Column(Integer, ForeignKey('activitati.id'))
	id_membru = Column(Integer,nullable=False)
	
	activitati = relationship('Activitati')
	membri_activitate = relationship('MembriActivitate')

	def __unicode__(self):
		return self.activitati or 'Unknown'

	class Admin(EntityAdmin):
		verbose_name = 'EchipaActivitate'
		list_display = ['activitati','id_membru']
