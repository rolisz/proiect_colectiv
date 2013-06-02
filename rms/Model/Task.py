from camelot.view.forms import TabForm, Form
from sqlalchemy.schema import Column
from camelot.admin.entity_admin import EntityAdmin
from camelot.core.orm import Entity, ManyToOne
from sqlalchemy import Unicode, Date, Integer, Boolean

class Task(Entity):
    __tablename__ = 'taskuri'

    nume = Column(Unicode(30))
    descriere = Column(Unicode(200))
    aprobat = Column(Boolean)
    faze_activitate = ManyToOne('FazeActivitate')
    membrii = ManyToOne("ResurseUmane", inverse="taskuri")

    def __unicode__(self):
        return self.nume + ' ' + self.descriere or 'Unknown'

    class Admin(EntityAdmin):
        verbose_name = 'Task'
        verbose_name_plural = 'Taskuri'
        list_display = ['nume', 'descriere', 'aprobat']
        form_display = TabForm([('Importante', Form(['nume', 'descriere'])),
                                ('Participanti', Form(['membrii']))])

