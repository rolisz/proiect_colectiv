from camelot.admin.entity_admin import EntityAdmin
from camelot.admin.not_editable_admin import not_editable_admin
from camelot.core.orm import Entity, ManyToMany
from sqlalchemy import Column, Integer, String, ForeignKey
from rms.Views.Rapoarte import RaportResurse

__author__ = 'Roland'

class ResursaLogistica(Entity):
    __tablename__ = 'resurse_logistice'

    type = Column(String(50))

    activitati = ManyToMany('Activitate')
    __mapper_args__ = {
        'polymorphic_identity': 'resursa',
        'polymorphic_on': type
    }

    class Admin(EntityAdmin):
        verbose_name = 'Resursa Logistica'
        verbose_name_plural = 'Resurse Logistice'
        list_display = ['type']
        form_actions = [RaportResurse()]

    class AdminPublic(EntityAdmin):
        verbose_name = 'Resursa Logistica'
        verbose_name_plural = 'Resurse Logistice'
        list_display = ['type']
        form_actions = [RaportResurse()]

    AdminPublic = not_editable_admin(AdminPublic, actions=False)


class Sala(ResursaLogistica):
    __tablename__ = 'sali'

    #todo celelalte coloane si dropdownuri pt ele
    id = Column(Integer, ForeignKey('resurse_logistice.id'), primary_key=True)
    nr_locuri = Column(Integer)
    nume = Column(String(20))

    __mapper_args__ = {
        'polymorphic_identity': 'sala',
    }

    def __unicode__(self):
        return str(self.nume) + " " + str(self.nr_locuri)

    class Admin(EntityAdmin):
        verbose_name = 'Sala'
        verbose_name_plural = 'Sali'
        list_display = ['nr_locuri', 'nume']


class Echipament(ResursaLogistica):
    __tablename__ = 'echipamente'

    #todo celelalte coloane si dropdownuri pt ele
    id = Column(Integer, ForeignKey('resurse_logistice.id'), primary_key=True)
    tip = Column(String(20))
    cantitate = Column(Integer)

    @property
    def nume(self):
        return self.tip

    __mapper_args__ = {
        'polymorphic_identity': 'echipament',
    }

    def __unicode__(self):
        return str(self.tip) + " " + str(self.cantitate)

    class Admin(EntityAdmin):
        verbose_name = 'Echipament'
        verbose_name_plural = 'Echipamente'
        list_display = ['tip', 'cantitate']
        field_attributes = {
            'tip': {'choices': lambda o: [('Scaun', 'Scaun'), ('Proiector', 'Proiector'), ('Calculator', 'Calculator')],
                    'default': 'Scaun'}
        }