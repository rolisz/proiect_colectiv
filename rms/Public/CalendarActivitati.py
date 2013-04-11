from camelot.admin.entity_admin import EntityAdmin
from camelot.admin import table
from camelot.core.orm import Entity
from camelot.view import forms
from sqlalchemy.schema import Column
from camelot.core.utils import ugettext_lazy as _
from sqlalchemy import Unicode, Integer, Boolean,Date
from rms.Model.Activitate import Activitate

from camelot.admin.action import Action
class CalendarActivitati(Entity):
	verbose_name = 'CalendarActivitati'
	__tablename__ = 'Calendar Activitati'
	nume_coordonator = Column(Unicode(50),nullable=False)
	tip = Column(Integer, nullable=False)
	aprobata = Column(Boolean, nullable=False)
	data_inceput = Column(Date,nullable=False)
	data_sfarsit = Column(Date,nullable=False)
	nume_membru = Column(Unicode(50), nullable=False)
	
	class Admin(EntityAdmin):
		verbose_name = 'Calendar Activitati'
		verbose_name_plural = 'Calendar Activitati'
		list_display = ['nume_coordonator','activitati.tip','aprobata','data_inceput','data_sfarsit','nume_membru',]