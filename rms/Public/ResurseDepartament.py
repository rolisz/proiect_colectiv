from camelot.admin.entity_admin import EntityAdmin
from camelot.admin import table
from camelot.core.orm import Entity
from camelot.view import forms
from sqlalchemy.schema import Column
from camelot.core.utils import ugettext_lazy as _
from sqlalchemy import Unicode, Integer, Boolean


class ResurseDepartament(Entity):
    __tablename__ = 'ResurseDepartament'
    nume = Column(Unicode(50), nullable=False)
    functie = Column(Unicode(30), nullable=True)
    doctorat = Column(Boolean, nullable=False)
    valoare = Column(Integer, nullable=False)
    tip = Column(Boolean, nullable=False)
    categorie = Column(Unicode(30), nullable=False)

    class Admin(EntityAdmin):
        verbose_name = 'Resurse Departament'
        verbose_name_plural = 'Resurse Departament'
        list_display = table.Table([table.ColumnGroup(('Resurse umane'), ['nume', 'functie', 'doctorat', ]),
                                    table.ColumnGroup(('Resurse logistice'), ['valoare', 'tip', 'categorie', ])]
        )
