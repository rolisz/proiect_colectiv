from sqlalchemy.schema import Column
import sqlalchemy.types
from camelot.admin.entity_admin import EntityAdmin
from camelot.core.orm import Entity
from sqlalchemy import Unicode, Date, Integer, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey

class ProgrameStudiu(Entity):

	__tablename__ = 'programe_studiu'

	nivel = Column(Integer, nullable=False)
	sectie = Column(Unicode(30),nullable=False)
	durata = Column(Integer, nullable=False)
	credite = Column(Integer, nullable=False)
	descriere = Column(Unicode(200), nullable=False)

	def __unicode__(self):
		return self.stuff or 'Unknown'

	class Admin(EntityAdmin):
		verbose_name = 'ProgrameStudiu'
		verbose_name_plural = 'ProgrameStudiu'
		list_display = ['nivel','sectie','durata','credite','descriere']