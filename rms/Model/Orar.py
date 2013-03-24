from sqlalchemy.schema import Column
import sqlalchemy.types
from camelot.admin.entity_admin import EntityAdmin
from camelot.core.orm import Entity
from sqlalchemy import Unicode, Date, Integer, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey

class Orar(Entity):

	__tablename__ = 'orar'

	zi = Column(Integer, nullable=False)
	ora = Column(Unicode(30),nullable=False)
	frecventa = Column(Integer, nullable=False)
	sala = Column(Unicode(6), nullable=False)
	anul = Column(Unicode(10), nullable=False)
	formatia = Column(Unicode(5), nullable=False)
	tip = Column(Integer, nullable=False)
	disciplina = Column(Unicode(30), nullable=False)

	def __unicode__(self):
		return self.stuff or 'Unknown'

	class Admin(EntityAdmin):
		verbose_name = 'Orar'
		list_display = ['zi','ora','frecventa','sala','anul','formatia','tip','disciplina']