from sqlalchemy.schema import Column
import sqlalchemy.types
from camelot.admin.entity_admin import EntityAdmin
from camelot.core.orm import Entity
from sqlalchemy import Unicode, Date, Integer, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey

class ResurseFinanciare( Entity ):

	__tablename__ = 'resurse_financiare'

	valoare = Column(Integer, primary_key=True)
	tip = Column(Boolean,nullable=False)

	def __unicode__(self):
		return self.stuff or 'Unknown'

	class Admin(EntityAdmin):
		verbose_name = 'ResurseFinanciare'
		list_display = ['valoare','tip']