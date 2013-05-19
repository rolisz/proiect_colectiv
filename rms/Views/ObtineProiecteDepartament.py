from camelot.admin.entity_admin import EntityAdmin
from camelot.admin.action import Action, ActionStep
from camelot.admin import table
from camelot.core.orm import Entity,Session
from camelot.view import forms
from sqlalchemy.schema import Column
from camelot.core.utils import ugettext_lazy as _
from sqlalchemy import Unicode, Integer, Boolean
from rms.Model.Activitate import *
class ProiecteDepartament:
    __tablename__ = None

    class Admin(EntityAdmin):
        verbose_name = 'Proiect Departament'
        verbose_name_plural = 'Proiecte Departament'
        list_display = ['valoare', 'tip', 'categorie']
        def get_query(self):
            session = Session
            return session.query(Activitate)

class ObtineProiecteDepartament(Action):
    verbose_name = 'Obtine Proiecte Departament'

    def model_run( self, model_context):
        yield ObtineProiecteDepartamentGUI()

class ObtineProiecteDepartamentGUI(ActionStep):

    def __init__(self):
        pass

    def gui_run( self, gui_context ):
        gui_context.workspace._tab_widget.clear()
        proiecte_table = ProiecteDepartament.Admin(gui_context.admin, Activitate).create_table_view(gui_context)
        proiecte_table.setObjectName('proiecte_table')

        gui_context.workspace._tab_widget.addTab(proiecte_table, "Proiecte Departament")