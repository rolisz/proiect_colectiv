from camelot.view.forms import TabForm, Form
from sqlalchemy.schema import Column
import sqlalchemy.types
from camelot.admin.entity_admin import EntityAdmin
from camelot.core.orm import Entity, ManyToOne, OneToMany
from sqlalchemy import Unicode, Date, Integer, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey


class FazeActivitate(Entity):
    __tablename__ = 'faze_activitati'

    nume = Column(Unicode(30))
    descriere = Column(Unicode(200))
    data_inceput = Column(Date)
    data_sfarsit = Column(Date)

    task = OneToMany('Task')
    activitate = ManyToOne('Activitate')

    def __unicode__(self):
        return unicode(self.activitate) or 'Unknown'

    class Admin(EntityAdmin):
        verbose_name = 'Faza Activitate'
        verbose_name_plural = 'Faze Activitati'
        list_display = ['nume', 'descriere', 'data_inceput', 'data_sfarsit']

        form_display = TabForm([('Importante', Form(['nume', 'descriere', 'data_inceput', 'data_sfarsit'])),
                                ('Taskuri', Form(['task']))]
                               )
    class Admin2(EntityAdmin):
        verbose_name = 'Calendar'
        verbose_name_plural = 'Calendar'
        list_display = ['data_inceput','nume', 'descriere', 'data_sfarsit']
    Admin2 = not_editable_admin(Admin2)
