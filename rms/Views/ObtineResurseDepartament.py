from camelot.admin.entity_admin import EntityAdmin
from camelot.admin.action import Action, ActionStep
from camelot.admin import table
from camelot.core.orm import Entity,Session
from camelot.view import forms
from sqlalchemy.schema import Column
from camelot.core.utils import ugettext_lazy as _
from sqlalchemy import Unicode, Integer, Boolean
from rms.Model.ResurseUmane import *
from rms.Model.ResurseFinanciare import *
class ResurseDepartament:
    __tablename__ = None

    class ResurseFinanciare(EntityAdmin):
        verbose_name = 'Resurse Financiare'
        verbose_name_plural = 'Resurse Financiare'
        list_display = ['valoare', 'tip', 'categorie']
        def get_query(self):
            session = Session
            return session.query(ResurseFinanciare)

    class ResurseUmane(EntityAdmin):
        verbose_name = 'Resurse Umane'
        verbose_name_plural = 'Resurse Umane'
        list_display = ['username', 'nume', 'doctorat', 'functie']
        def get_query(self):
            session = Session
            return session.query(ResurseUmane)

class ObtineResurseDepartament(Action):
    verbose_name = 'Obtine Resurse Departament'

    def model_run( self, model_context):
        yield ObtineResurseDepartamentGUI()

class ObtineResurseDepartamentGUI(ActionStep):

    def __init__(self):
        pass

    def gui_run( self, gui_context ):
        gui_context.workspace._tab_widget.clear()
        resfinanciare_table = ResurseDepartament.ResurseFinanciare(gui_context.admin,ResurseFinanciare).create_table_view(gui_context)
        resfinanciare_table.setObjectName('resfinanciare_table')
        resumane_table = ResurseDepartament.ResurseUmane(gui_context.admin,ResurseUmane).create_table_view(gui_context)
        resumane_table.setObjectName('resumane_table')

        gui_context.workspace._tab_widget.addTab(resfinanciare_table, "Resurse Financiare")
        gui_context.workspace._tab_widget.addTab(resumane_table, "Resurse Umane")