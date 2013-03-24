from sqlalchemy.schema import Column
import sqlalchemy.types
from camelot.admin.entity_admin import EntityAdmin
from camelot.core.orm import Entity
from sqlalchemy import Unicode, Date, Integer, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey

class ActivitatiGranturi(Entity):

	__tablename__ = 'activitati_granturi'

	id = Column(Integer, primary_key=True)
	id_faza = Column(Integer,nullable=False)
	nume = Column(Unicode(30), nullable=False)
	descriere = Column(Unicode(200), nullable=False)

	def __unicode__(self):
		return self.stuff or 'Unknown'

	class Admin(EntityAdmin):
		verbose_name = 'ActivitatiGranturi'
		list_display = ['id','id_faza','nume','descriere']
