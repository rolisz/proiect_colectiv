from camelot.admin.action import Action, ActionStep
from rms.Model.FazeActivitate import *
from rms.Model.Orar import *


class CalendarActivitatiAction(Action):
    verbose_name = "Calendar activitati"

    def model_run(self, model_context):
        yield CalendarActivitatiGUI()

class CalendarActivitatiGUI(ActionStep):
    def __init__(self):
        pass

    def gui_run(self, gui_context):
        gui_context.workspace._tab_widget.clear()
        faze_table = FazeActivitate.AdminCadru(gui_context.admin, FazeActivitate).create_table_view(gui_context)
        faze_table.setObjectName('faze_table')
        orar_table = Orar.AdminCadru(gui_context.admin,Orar).create_table_view(gui_context)
        orar_table.setObjectName('orar_table')
        gui_context.workspace._tab_widget.addTab(faze_table, "Calendar activitate")
        gui_context.workspace._tab_widget.addTab(orar_table, "Orar")

