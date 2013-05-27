from camelot import model
from camelot.admin.action import OpenTableView
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


class MyApplicationAdmin(ApplicationAdmin):
    name = 'Resource Management System'
    application_url = 'https://github.com/rolisz/proiect_colectiv'
    help_url = 'https://github.com/rolisz/proiect_colectiv/wiki'
    author = 'Roland'
    domain = 'http://github.com'

    def get_sections(self):
        print(model.authentication.get_current_authentication().username)
        session = Session
        user = session.query(ResurseUmane).filter(
            ResurseUmane.username == model.authentication.get_current_authentication().username).first()
        sectii = []
        if user is None or user.functie == 'Student':
            return [Section(_('Caracteristici publice'),
                            self,
                            Icon('tango/22x22/apps/system-users.png'),
                            items=[Activitate, ResurseUmane, Granturi, ResurseFinanciare, ResursaLogistica,
                                   CalendarActivitatiAction(), ProgramStudiu, ImportOrar()])]
        if user.functie == 'Administrator':
            return [Section(_('Caracteristici administrative'),
                            self,
                            Icon('tango/22x22/apps/system-users.png'),
                            items=[])]
        if user.functie == 'Profesor':
            return [Section(_('Caracteristici pentru directorul de departament'),
                            self,
                            Icon('tango/22x22/apps/system-users.png'),
                            items=[ProgramStudiu])]
        if user.functie == 'Director':
            return [Section(_('Caracteristici pentru cadre didactice'),
                            self,
                            Icon('tango/22x22/apps/system-users.png'),
                            items=[Activitate, ResurseUmane, CalendarActivitatiAction()])]

