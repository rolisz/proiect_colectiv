from camelot.view.art import Icon
from camelot.admin.application_admin import ApplicationAdmin
from camelot.admin.section import Section
from camelot.core.utils import ugettext_lazy as _
from Model.Activitati import *
from Model.Task import *
from Model.EchipaActivitate import *
from Model.MembriTask import *
from Model.FazeActivitate import *
from Model.Orar import *
from Model.ResurseFinanciare import *
from Model.ResurseUmane import *
from Model.ResurseActivitate import *

from Model.ProgramStudiu import ProgramStudiu


from programe_studiu import ProgramStudiu


class MyApplicationAdmin(ApplicationAdmin):
  
    name = 'Resource Management System'
    application_url = 'https://github.com/rolisz/proiect_colectiv'
    help_url = 'https://github.com/rolisz/proiect_colectiv/wiki'
    author = 'Roland'
    domain = 'http://github.com'
    
    def get_sections(self):
        from camelot.model.memento import Memento
        from camelot.model.i18n import Translation
        return [ Section( _('My classes'),
                          self,
                          Icon('tango/22x22/apps/system-users.png'),
                          items = [ProgramStudiu] ),
                 Section( _('Configuration'),
                          self,
                          Icon('tango/22x22/categories/preferences-system.png'),
                          items = [Memento, Translation] )
                ]
    
