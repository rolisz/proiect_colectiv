from camelot import model
from camelot.admin.action import OpenNewView
from camelot.admin.not_editable_admin import not_editable_admin
from camelot.view.forms import TabForm, Form
from sqlalchemy.schema import Column
from camelot.admin.entity_admin import EntityAdmin
from camelot.core.orm import Entity, ManyToMany, Session, OneToMany, ManyToOne, Field
from sqlalchemy import Unicode, Boolean, String, Text
from rms.Model.ResurseUmane import ResurseUmane
from rms.Views.Rapoarte import RapoarteActivitati


class NewActivitate(OpenNewView):
    verbose_name = 'Transmite cerere activitate noua'

class Activitate(Entity):
    __tablename__ = 'activitati'

    tip = Column(String(30))
    __mapper_args__ = {'polymorphic_on': tip}

    nume = Field(Unicode(50), required=True)
    descriere = Column(Text(100))
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
        list_filter = ['faze.data_inceput', 'faze.data_sfarsit']
        form_display = TabForm([('Importante', Form(['nume', 'coordonator', 'descriere', 'confidentiala'])),
                                ('Participanti', Form(['membrii'])),
                                ('Resurse', Form(['res_fin', 'res_logistice'])),
                                ('Faze', Form(['faze']))
        ])
        field_attributes = {
            'res_fin': {'name': 'Resurse Financiare'},
            'res_logistice': {'name': 'Resurse Logistice'}
        }
        form_actions = [RapoarteActivitati()]

    class AdminCadru(EntityAdmin):
        verbose_name = 'Calendar activitati'
        list_display = ['nume', 'descriere', 'aprobata']
        form_display = ['nume', 'descriere']
        field_attributes = {
            'aprobata': {'editable': False}
        }

        def get_query(self):
            session = Session
            user = session.query(ResurseUmane).filter(
                ResurseUmane.username == model.authentication.get_current_authentication().username).first()
            return session.query(Activitate).join(ResurseUmane).filter(
                ResurseUmane.id == user.id)

    class AdminPublic(EntityAdmin):
        verbose_name = 'Proiect Departament'
        verbose_name_plural = 'Proiecte Departament'

        list_display = ['nume', 'coordonator', 'descriere']

        def get_query(self):
            session = Session
            return session.query(self.entity).filter(self.entity.confidentiala == False).filter(
                self.entity.aprobata == True)

        def get_related_admin(self, cls):
            if cls == Granturi:
                return Granturi.AdminPublic(self, cls)
            elif cls == Cercuri:
                return Cercuri.AdminPublic(self, cls)
            elif cls == EvenimenteAdministrative:
                return EvenimenteAdministrative.AdminPublic(self, cls)
            else:
                return cls.Admin


    AdminPublic = not_editable_admin(AdminPublic)

# subclasa care contine doar granturi
class Granturi(Activitate):
    __tablename__ = None

    __mapper_args__ = {
        'polymorphic_identity': 'grant'
    }

    class Admin(Activitate.Admin):
        verbose_name = 'Grant'
        verbose_name_plural = 'Granturi'

    class AdminPublic(Activitate.AdminPublic):
        verbose_name = 'Granturi Departament'
        verbose_name_plural = 'Granturi Departament'

        list_display = ['nume', 'coordonator', 'descriere']

        def get_query(self):
            session = Session
            return session.query(Granturi).filter(Granturi.confidentiala == False).filter(
                Granturi.aprobata == True)

    AdminPublic = not_editable_admin(AdminPublic)

class Cercuri(Activitate):
    __tablename__ = None

    __mapper_args__ = {
        'polymorphic_identity': 'cerc'
    }

    program_studiu = ManyToOne('ProgramStudiu')
    class Admin(Activitate.Admin):
        verbose_name = 'Cerc'
        verbose_name_plural = 'Cercuri'

        list_display = ['nume', 'coordonator', 'program_studiu', 'descriere']
        form_display = TabForm([('Importante', Form(['nume', 'coordonator', 'descriere','program_studiu'])),
                                ('Participanti', Form(['membrii']))])

    class AdminPublic(Activitate.AdminPublic):
        verbose_name = 'Cerc Departament'
        verbose_name_plural = 'Cercuri Departament'

        list_display = ['nume', 'coordonator', 'program_studiu', 'descriere']



class EvenimenteAdministrative(Activitate):
    __tablename__ = None

    __mapper_args__ = {
        'polymorphic_identity': 'administrative'
    }

    class Admin(Activitate.Admin):
        verbose_name = 'Eveniment administrativ'
        verbose_name_plural = 'Evenimente administrative'

    class AdminPublic(Activitate.AdminPublic):
        verbose_name = 'Eveniment administrativ'
        verbose_name_plural = 'Evenimente administrative'