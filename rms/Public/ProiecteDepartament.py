from camelot.admin.entity_admin import EntityAdmin
from camelot.admin import table
from camelot.core.orm import Entity
from camelot.view import forms
from sqlalchemy.schema import Column
from camelot.core.utils import ugettext_lazy as _
from sqlalchemy import Unicode, Integer, Boolean, Date
class ProiecteDepartament(Entity):
	__tablename__ = 'ProiecteDepartament'
	nume_proiect = Column(Unicode(30), nullable=False)
	descriere = Column(Unicode(200), nullable=False)
	desfasurat = Column(Boolean, nullable=False)
	nume_faza = Column(Unicode(30), nullable=False)
	descriere_faza = Column(Unicode(200), nullable=False)
	data_inceput = Column(Date,nullable=False)
	data_sfarsit = Column(Date,nullable=False)
	nume_membru = Column(Unicode(50), nullable=False)
	functie_membru = Column(Unicode(30), nullable=True)
	doctorat = Column(Boolean, nullable=False)
	class Admin(EntityAdmin):
		verbose_name = 'Proiecte Departament'
		verbose_name_plural = 'Proiecte Departament'
		list_display = table.Table( [ table.ColumnGroup( ('Informatii proiect'),['nume_proiect','descriere','desfasurat',] ),
					      table.ColumnGroup( ('Detalii faza proiect'),['nume_proiect','nume_faza','descriere_faza','data_inceput','data_sfarsit'] ),
					      table.ColumnGroup( ('Detalii membrii proiect'),['nume_proiect','nume_membru','doctorat','functie_membru',] ) ]
						      )
