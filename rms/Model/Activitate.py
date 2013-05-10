from PyQt4 import QtGui
from camelot.admin.action import Action, ActionStep
from camelot.admin.not_editable_admin import not_editable_admin
from camelot.core.sql import metadata
from camelot.view.controls.tableview import TableView
from camelot.view.forms import TabForm, Form
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from camelot.admin.entity_admin import EntityAdmin
from camelot.core.orm import Entity, ManyToMany, using_options, Session, OneToMany, ManyToOne, Field
from sqlalchemy import Unicode, Date, Integer, Boolean, String
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey
from rms.Model.ResurseUmane import ResurseUmane


class Activitate(Entity):
    __tablename__ = 'activitati'

    tip = Column(String(30))
    __mapper_args__ = {'polymorphic_on': tip}

    nume = Field(Unicode(50), required=True, index=True)
    coordonator = ManyToOne('ResurseUmane', inverse='activitati_coordonate')
    membrii = ManyToMany('ResurseUmane')
    aprobata = Column(Boolean)
    #todo adaugat faze activitate
    def __unicode__(self):
        return self.nume or ''

    class Admin(EntityAdmin):
        verbose_name = 'Activitate'
        verbose_name_plural = 'Activitati'
        list_display = ['nume']
        form_display = TabForm([( 'Basic', Form(['nume', 'coordonator']) ),
                                ( 'Employment', Form(['membrii']) ),
                               # ( 'Corporate', Form(['directors']) ),
        ])
        field_attributes = dict(ResurseUmane.Admin.field_attributes)



# subclasa care contine doar granturi
class Granturi(Activitate):
    __tablename__ = None

    __mapper_args__ = {
        'polymorphic_identity': 'grant'
    }

    class Admin(EntityAdmin):
        verbose_name = 'Grant'
        verbose_name_plural = 'Granturi'
        list_display = ['coordonator', 'tip', 'aprobata', 'echipa_activitate',
                        'faze_activitate']

        form_display = ['coordonator', 'tip']



class Cercuri(Activitate):
    __tablename__ = None

    __mapper_args__ = {
        'polymorphic_identity': 'cerc'
    }

    class Admin(Activitate.Admin):
        verbose_name = 'Cerc'
        verbose_name_plural = 'Cercuri'



# chestiile necesare pentru a face viewuri custom
class FiltrareActivitatiAction(Action):
    verbose_name = "Filtare activitati"

    def model_run(self, model_context):
        yield FiltrareActivitatiGUI()


class FiltrareActivitatiGUI(ActionStep):

    def __init__(self):
        pass

    def gui_run(self, gui_context):
        gui_context.workspace._tab_widget.clear()
        activi_table = Activitate.Admin2(gui_context.admin, Activitate).create_table_view(gui_context)
        gui_context.workspace._tab_widget.addTab(activi_table, "Filtrare")
