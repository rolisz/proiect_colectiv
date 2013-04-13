from camelot.view.art import Icon
from camelot.admin.application_admin import ApplicationAdmin
from camelot.admin.section import Section
from camelot.core.utils import ugettext_lazy as _
from Model.Activitate import *
from Model.Task import *
from Model.EchipaActivitate import *
from Model.MembruTask import *
from Model.FazeActivitate import *
from Model.Orar import *
from Model.ResurseFinanciare import *
from Model.ResurseUmane import *
from Model.ResurseActivitate import *
from Model.ProgramStudiu import ProgramStudiu
from Public.ResurseDepartament import *
from Public.ProiecteDepartament import *
from Public.CalendarActivitati import *


class MyApplicationAdmin(ApplicationAdmin):
    name = 'Resource Management System'
    application_url = 'https://github.com/rolisz/proiect_colectiv'
    help_url = 'https://github.com/rolisz/proiect_colectiv/wiki'
    author = 'Roland'
    domain = 'http://github.com'

    def get_sections(self):
        return [Section(_('Caracteristici publice'),
                        self,
                        Icon('tango/22x22/apps/system-users.png'),
                        items=[Activitate, ResurseUmane, Granturi,FiltrareActivitatiAction()]),
                Section(_('Caracteristici administrative'),
                        self,
                        Icon('tango/22x22/apps/system-users.png'),
                        items=[]),
                Section(_('Caracteristici pentru directorul de departament'),
                        self,
                        Icon('tango/22x22/apps/system-users.png'),
                        items=[ProgramStudiu]),
                Section(_('Caracteristici pentru cadre didactice'),
                        self,
                        Icon('tango/22x22/apps/system-users.png'),
                        items=[]),

                ]
