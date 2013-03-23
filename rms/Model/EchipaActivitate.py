from sqlalchemy.schema import Column
import sqlalchemy.types
from camelot.admin.entity_admin import EntityAdmin
from camelot.core.orm import Entity
from sqlalchemy import Unicode, Date, Integer, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey

class EchipaActivitate(Entity):

	__tablename__ = 'echipa_activitate'

	id_activitate = Column(Integer, ForeignKey('activitati.id'))
	id_membru = Column(Integer,ForeignKey('resurse_umane.id'))

	activitati = relationship('Activitati')
	resurse = relationship('ResurseUmane')

	def __unicode__(self):
		return self.activitati or 'Unknown'

	class Admin(EntityAdmin):
		verbose_name = 'EchipaActivitate'
		verbose_name_plural = 'EchipaActivitate'
		list_display = ['id_activitate','id_membru']
