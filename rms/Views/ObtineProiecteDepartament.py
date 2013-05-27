from camelot.admin.entity_admin import EntityAdmin
from camelot.admin.action import Action, ActionStep
from camelot.admin import table
from camelot.core.orm import Entity,Session
from camelot.view import forms
from camelot.view.controls.modeltree import ModelTree
from camelot.view.model_thread import post
from sqlalchemy.schema import Column
from camelot.core.utils import ugettext_lazy as _
from sqlalchemy import Unicode, Integer, Boolean
from rms.Model.Activitate import *
class ObtineProiecteDepartament(Action):
    verbose_name = 'Obtine Proiecte Departament'

    def model_run(self, model_context):
            yield ObtineProiecteDepartamentGUI()

class SubclassTree(ModelTree):
    def __init__(self, admin, parent):
        header_labels = ['Types']
        ModelTree.__init__(self, header_labels, parent)
        self.admin = admin
        self.subclasses = []
        post(self.admin.get_subclass_tree, self.setSubclasses)
        self.setSizePolicy(
            QtGui.QSizePolicy.Minimum,
            QtGui.QSizePolicy.Expanding
        )

class ObtineProiecteDepartamentGUI(ActionStep):
        def __init__(self):
            pass
        def gui_run( self, gui_context ):
            gui_context.workspace._tab_widget.clear()
            proiecte_table = Activitate.Admin3(gui_context.admin, Activitate).create_table_view(gui_context)
            proiecte_table.setObjectName('proiecte_table')
            gui_context.workspace._tab_widget.addTab(proiecte_table, "Proiecte Departament")

