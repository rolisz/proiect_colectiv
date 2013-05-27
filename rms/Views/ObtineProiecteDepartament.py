from camelot.admin.action import Action, ActionStep
from rms.Model.Activitate import *
class ObtineProiecteDepartament(Action):
    verbose_name = 'Obtine Proiecte Departament'

    def model_run(self, model_context):
            yield ObtineProiecteDepartamentGUI()

class ObtineProiecteDepartamentGUI(ActionStep):
        def __init__(self):
            pass
        def gui_run( self, gui_context ):
            gui_context.workspace._tab_widget.clear()
            proiecte_table = Activitate.Admin3(gui_context.admin, Activitate).create_table_view(gui_context)
            proiecte_table.setObjectName('proiecte_table')
            gui_context.workspace._tab_widget.addTab(proiecte_table, "Proiecte Departament")

