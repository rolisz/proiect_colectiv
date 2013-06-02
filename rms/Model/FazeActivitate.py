from camelot import model
from camelot.admin.not_editable_admin import not_editable_admin
from camelot.view.forms import TabForm, Form
from sqlalchemy.schema import Column
import sqlalchemy.types
from camelot.admin.entity_admin import EntityAdmin
from camelot.core.orm import Entity, ManyToOne, OneToMany, Session
from sqlalchemy import Unicode, Date, Integer, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey
from rms.Model.Activitate import Activitate
from rms.Model.ResurseUmane import ResurseUmane


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

    class AdminCadru(Admin):
        verbose_name = 'Calendar faze activitati'
        verbose_name_plural = 'Calendar faze activitati'
        list_filter = ['data_inceput', 'data_sfarsit']

        def get_query(self):
            session = Session
            user = session.query(ResurseUmane).filter(
                ResurseUmane.username == model.authentication.get_current_authentication().username).first()
            if user is not None and user.functie == 'Profesor':
                return session.query(FazeActivitate).join(Activitate).join(ResurseUmane).filter(
                ResurseUmane.id == user.id)
            else:
                return session.query(FazeActivitate).join(Activitate).filter(Activitate.confidentiala==False)


    AdminCadru = not_editable_admin(AdminCadru, deep=True)
