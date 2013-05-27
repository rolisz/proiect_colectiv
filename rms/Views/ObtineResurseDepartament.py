from camelot.admin.entity_admin import EntityAdmin
from camelot.admin.action import Action, ActionStep
from camelot.admin import table
from camelot.core.orm import Entity,Session
from camelot.view import forms
from sqlalchemy.schema import Column
from camelot.core.utils import ugettext_lazy as _
from sqlalchemy import Unicode, Integer, Boolean
from rms.Model.ResurseLogistice import ResursaLogistica
from rms.Model.ResurseUmane import *
from rms.Model.ResurseFinanciare import *

class ObtineResurseDepartament(Action):
    verbose_name = 'Obtine Resurse Departament'

    def model_run( self, model_context):
        yield ObtineResurseDepartamentGUI()

class ObtineResurseDepartamentGUI(ActionStep):

    def __init__(self):
        pass

    def gui_run( self, gui_context):
        gui_context.workspace._tab_widget.clear()
        resfinanciare_table = ResurseFinanciare.Admin2(gui_context.admin,ResurseFinanciare).create_table_view(gui_context)
        resfinanciare_table.setObjectName('resfinanciare_table')
        resumane_table = ResursaLogistica.Admin2(gui_context.admin,ResursaLogistica).create_table_view(gui_context)
        resumane_table.setObjectName('resumane_table')
        gui_context.workspace._tab_widget.addTab(resfinanciare_table, "Resurse Financiare")
        gui_context.workspace._tab_widget.addTab(resumane_table, "Resurse Logistice")