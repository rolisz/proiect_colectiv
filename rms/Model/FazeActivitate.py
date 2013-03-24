from sqlalchemy.schema import Column
import sqlalchemy.types
from camelot.admin.entity_admin import EntityAdmin
from camelot.core.orm import Entity
from sqlalchemy import Unicode, Date, Integer, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey

class FazeActivitate(Entity):

	__tablename__ = 'faze_activitate'

	id = Column(Integer, primary_key=True)
	id_grant = Column(Integer,nullable=False)
	nume = Column(Unicode(30), nullable=False)
	descriere = Column(Unicode(200), nullable=False)
	data_inceput = Column(Date,nullable=False)
	data_sfarsit = Column(Date,nullable=False)

	def __unicode__(self):
		return self.stuff or 'Unknown'

	class Admin(EntityAdmin):
		verbose_name = 'FazeActivitate'
		list_display = ['id','id_grant','nume','descriere','data_inceput','data_sfarsit']
