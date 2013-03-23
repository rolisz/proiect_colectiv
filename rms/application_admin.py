
from camelot.view.art import Icon
from camelot.admin.application_admin import ApplicationAdmin
from camelot.admin.section import Section
from camelot.core.utils import ugettext_lazy as _

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
                          items = [] ),
                 Section( _('Configuration'),
                          self,
                          Icon('tango/22x22/categories/preferences-system.png'),
                          items = [Memento, Translation] )
                ]
    