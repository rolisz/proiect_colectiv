from PyQt4 import QtGui
from camelot.admin.action import Action, ActionStep
from camelot.admin.not_editable_admin import not_editable_admin
from camelot.core.sql import metadata
from camelot.view.controls.tableview import TableView
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from camelot.admin.entity_admin import EntityAdmin
from camelot.core.orm import Entity, ManyToMany, using_options, Session
from sqlalchemy import Unicode, Date, Integer, Boolean, String
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey


class Activitate(Entity):
    __tablename__ = 'activitati'

    id_coordonator = Column(Integer, ForeignKey('resurse_umane.id'))
    nume = Column(Unicode(50))
    coordonator = relationship('ResurseUmane')
    tip = Column('type',String(10))

    aprobata = Column(Boolean)

    echipa_activitate = relationship('EchipaActivitate')
    faze_activitate = relationship('FazeActivitate')
    resurse_activitate = relationship('ResurseActivitate')

    __mapper_args__ = {
        'polymorphic_on': tip,
    }

    def __unicode__(self):
        return self.echipa_activitate or 'Unknown'

    class Admin(EntityAdmin):
        verbose_name = 'Activitate'
        verbose_name_plural = 'Activitati'
        list_display = ['coordonator', 'tip', 'aprobata', 'echipa_activitate',
                        'faze_activitate']

        form_display = ['coordonator', 'tip']


    # Cum se creaza un view separat care contine doar anumite obiecte
    class Admin2(EntityAdmin):
        verbose_name = 'Activitate'
        verbose_name_plural = 'Activitati'
        list_display = ['coordonator', 'tip', 'aprobata', 'echipa_activitate']

        def get_query(self):
            session = Session
            return session.query(Activitate).filter_by(tip='cerc')


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

    class Admin(EntityAdmin):
        verbose_name = 'Cerc'
        verbose_name_plural = 'Cercuri'
        list_display = ['coordonator', 'tip', 'aprobata', 'echipa_activitate',
                        'faze_activitate']

        form_display = ['coordonator', 'tip']


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
