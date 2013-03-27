from sqlalchemy.schema import Column
import sqlalchemy.types
from camelot.admin.entity_admin import EntityAdmin
from camelot.core.orm import Entity
from sqlalchemy import Unicode, Date, Integer, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey

class MembruTask(Entity):

	__tablename__ = 'membri_taskuri'

	id_task = Column(Integer, ForeignKey('task.id'))
	id_membru = Column(Integer,ForeignKey('resurse_umane.id'))
	task = relationship('Task')
	resurse_umane = relationship('ResurseUmane')
	def __unicode__(self):
		return self.resurse_umane or 'Unknown'

	class Admin(EntityAdmin):
		verbose_name = 'MembruTask'
		verbose_name_plural = 'MembriTaskuri'
		list_display = ['id_task','id_membru']
