from sqlalchemy.schema import Column
import sqlalchemy.types
from camelot.admin.entity_admin import EntityAdmin
from camelot.core.orm import Entity
from sqlalchemy import Unicode, Date, Integer, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey

class EchipaActivitate(Entity):

	__tablename__ = 'echipa_activitate'

	id_activitate = Column(Integer, ForeignKey('activitate.id'))
	id_membru = Column(Integer,ForeignKey('resurse_umane.id'))

	activitate = relationship('Activitate')
	resurse = relationship('ResurseUmane')

	def __unicode__(self):
		return self.activitate or 'Unknown'

	class Admin(EntityAdmin):
		verbose_name = 'EchipaActivitate'
		verbose_name_plural = 'EchipeActivitati'
		list_display = ['id_activitate','id_membru']
