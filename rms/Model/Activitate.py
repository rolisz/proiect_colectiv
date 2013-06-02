from camelot.admin.action import Action, ActionStep
from camelot.admin.not_editable_admin import not_editable_admin
from camelot.core.sql import metadata
from camelot.view.controls.modeltree import ModelTree, ModelItem
from camelot.view.controls.tableview import TableView
from camelot.view.forms import TabForm, Form
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from camelot.admin.entity_admin import EntityAdmin
from camelot.core.orm import Entity, ManyToMany, using_options, Session, OneToMany, ManyToOne, Field
from sqlalchemy import Unicode, Date, Integer, Boolean, String
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey
import rms
from rms.Model.ResurseUmane import ResurseUmane

class RapoarteActivitati(Action):
    verbose_name = "Rapoarte folosire activitati"

    def model_run(self, model_context):
        from camelot.view.action_steps import PrintHtml
        import datetime
        import os
        from jinja import Environment, FileSystemLoader
        from pkg_resources import resource_filename

        fileloader = FileSystemLoader(resource_filename(rms.__name__, 'templates'))
        e = Environment(loader=fileloader)
        activitate = model_context.get_object()
        context = {
            'header': activitate.nume,
            'title': 'Raport activitate',
            'style': '.label { font-weight:bold; }',
            'coordonator': activitate.coordonator,
            'aprobata': activitate.aprobata,
            'membrii': activitate.membrii,
            'res_fin': activitate.res_fin,
            'res_log': activitate.res_logistice,
            'footer': str(datetime.datetime.now().year)
        }
        t = e.get_template('activitate.html')
        yield PrintHtml(t.render(context))

class Activitate(Entity):
    __tablename__ = 'activitati'

    tip = Column(String(30))
    __mapper_args__ = {'polymorphic_on': tip}

    nume = Field(Unicode(50), required=True, index=True)
    coordonator = ManyToOne('ResurseUmane', inverse='activitati_coordonate')
    membrii = ManyToMany('ResurseUmane')
    aprobata = Column(Boolean)
    res_fin = OneToMany('ResurseFinanciare', inverse="activitate")
    res_logistice = ManyToMany('ResursaLogistica')

    confidentiala = Column(Boolean)
    #todo adaugat faze activitate
    faze = OneToMany("FazeActivitate")
    def __unicode__(self):
        return self.nume or ''

    class Admin(EntityAdmin):
        verbose_name = 'Activitate'
        verbose_name_plural = 'Activitati'
        list_display = ['nume', 'coordonator', 'aprobata', 'confidentiala']
        form_display = TabForm([('Importante', Form(['nume', 'coordonator', 'confidentiala'])),
                                ('Participanti', Form(['membrii'])),
                                ('Resurse', Form(['res_fin', 'res_logistice'])),
                                ('Faze', Form(['faze']))
        ])
        field_attributes = dict(ResurseUmane.Admin.field_attributes)
        form_actions = [RapoarteActivitati()]

    class Admin2(EntityAdmin):
        verbose_name = 'Calendar activitati'
        list_display = ['nume', 'coordonator', 'aprobata']

        def get_query(self):
            session = Session
            return session.query(Activitate).join(ResurseUmane).filter(ResurseUmane.id==1) # todo schimbat cu userul
                                                                                           # curent

    class Admin3(EntityAdmin):
        verbose_name = 'Proiect Departament'
        verbose_name_plural = 'Proiecte Departament'

        list_display = ['nume', 'coordonator', 'tip']

        def get_query(self):
            session = Session
            return session.query(Activitate).filter(Activitate.confidentiala==False).filter(Activitate.aprobata==True)


        form_actions = [None]


    Admin3 = not_editable_admin(Admin3)

# subclasa care contine doar granturi
class Granturi(Activitate):
    __tablename__ = None

    __mapper_args__ = {
        'polymorphic_identity': 'grant'
    }

    class Admin(Activitate.Admin):
        verbose_name = 'Grant'
        verbose_name_plural = 'Granturi'


class Cercuri(Activitate):
    __tablename__ = None

    __mapper_args__ = {
        'polymorphic_identity': 'cerc'
    }

    class Admin(Activitate.Admin):
        verbose_name = 'Cerc'
        verbose_name_plural = 'Cercuri'

    #todo se adauga teme

# chestiile necesare pentru a face viewuri custom
class CalendarActivitatiAction(Action):
    verbose_name = "Calendar activitati"

    def model_run(self, model_context):
        yield CalendarActivitatiGUI()

# todo add orar cursuri
class CalendarActivitatiGUI(ActionStep):
    def __init__(self):
        pass

    def gui_run(self, gui_context):
        gui_context.workspace._tab_widget.clear()
        activi_table = ModelTree()
        mi = ModelItem(activi_table,['Orar','Activitati'],['Orar','Activitati'])
        activi_table.addTopLevelItem(mi)
        gui_context.workspace._tab_widget.addTab(activi_table, "Calendar activitate")


