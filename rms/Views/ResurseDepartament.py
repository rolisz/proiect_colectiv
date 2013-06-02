from camelot.admin.action import Action, ActionStep
from rms.Model.ResurseLogistice import ResursaLogistica
from rms.Model.ResurseUmane import ResurseUmane

class ObtineResurseDepartament(Action):
    verbose_name = 'Resurse Departament'

    def model_run( self, model_context):
        yield ObtineResurseDepartamentGUI()

class ObtineResurseDepartamentGUI(ActionStep):
    def __init__(self):
        pass

    def gui_run( self, gui_context):
        gui_context.workspace._tab_widget.clear()
        reslogistice_table = ResursaLogistica.AdminPublic(gui_context.admin, ResursaLogistica).create_table_view(gui_context)
        reslogistice_table.setObjectName('reslogistice_table')
        resumane_table = ResurseUmane.AdminPublic(gui_context.admin, ResurseUmane).create_table_view(gui_context)
        resumane_table.setObjectName('resumane_table')
        gui_context.workspace._tab_widget.addTab(resumane_table, "Resurse Umane")
        gui_context.workspace._tab_widget.addTab(reslogistice_table, "Resurse Logistice")
