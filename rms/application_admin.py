from camelot import model
from camelot.admin.action import OpenTableView, OpenNewView
from camelot.view.art import Icon
from camelot.admin.application_admin import ApplicationAdmin
from camelot.admin.section import Section
from camelot.core.utils import ugettext_lazy as _
from Model.Activitate import *
from Model.Task import *
from Model.FazeActivitate import *
from Model.Orar import *
from Model.ResurseFinanciare import *
from Model.ResurseLogistice import *
from Model.ResurseUmane import *
from Model.ResurseActivitate import *
from Model.ProgramStudiu import ProgramStudiu
from rms.Model import ResurseLogistice
from rms.Model.OreSuplimentare import OreSuplimentare
from rms.Model.Discipline import Discipline
from rms.Views.ResurseDepartament import ObtineResurseDepartament
from rms.Views.import_orar import ImportOrar
from rms.Views.import_state import ImportState
from rms.Views.CalendarActivitati import CalendarActivitatiAction

class MyApplicationAdmin(ApplicationAdmin):
    name = 'Resource Management System'
    application_url = 'https://github.com/rolisz/proiect_colectiv'
    help_url = 'https://github.com/rolisz/proiect_colectiv/wiki'
    author = 'Roland'
    domain = 'http://github.com'

    # def get_toolbar_actions(self, area):
    #     print(area)
    #     return None

    # def get_related_admin(self, cls):
    #     print(cls)
    #     return cls.Admin

    def get_sections(self):
        print(model.authentication.get_current_authentication().username)
        session = Session
        user = session.query(ResurseUmane).filter(
            ResurseUmane.username == model.authentication.get_current_authentication().username).first()
        return [Section(_('Caracteristici publice'),
                            self,
                            Icon('tango/22x22/apps/system-users.png'),
                            items=[OpenTableView(Activitate.AdminPublic(self,Activitate)),CalendarActivitatiAction(),ObtineResurseDepartament()]),
                Section(_('Caracteristici administrative'),
                            self,
                            Icon('tango/22x22/apps/system-users.png'),
                            items=[ResurseUmane, ResurseFinanciare, ResursaLogistica,ImportOrar(), ImportState()]),
                Section(_('Caracteristici pentru cadru didactic'),
                            self,
                            Icon('tango/22x22/apps/system-users.png'),
                            items=[CalendarActivitatiAction(), NewActivitate(Activitate.AdminCadru(self,Activitate)), NewTask(Task.AdminCadru(self,Task))]),
                Section(_('Caracteristici pentru director'),
                            self,
                            Icon('tango/22x22/apps/system-users.png'),
                            items=[ProgramStudiu, Activitate, Task, ResursaLogistica, ResurseUmane])]
        if user is None or user.functie == 'Student':
            return [Section(_('Caracteristici publice'),
                            self,
                            Icon('tango/22x22/apps/system-users.png'),
                            items=[OpenTableView(Activitate.AdminPublic(self,Activitate)),ObtineResurseDepartament])]
        if user.functie == 'Administrator':
            return [Section(_('Caracteristici administrative'),
                            self,
                            Icon('tango/22x22/apps/system-users.png'),
                            items=[ResurseUmane, ResurseFinanciare, ResursaLogistica,ImportOrar(), ImportState()])]
        if user.functie == 'Profesor':
            return [Section(_('Caracteristici pentru cadre didactice'),
                            self,
                            Icon('tango/22x22/apps/system-users.png'),
                            items=[CalendarActivitatiAction(), OpenTableView(Activitate.AdminCadru(self,Activitate)), Task])]
        if user.functie == 'Director':
            return [Section(_('Caracteristici pentru  directorul de departament'),
                            self,
                            Icon('tango/22x22/apps/system-users.png'),
                            items=[ProgramStudiu, Activitate, Task])]

