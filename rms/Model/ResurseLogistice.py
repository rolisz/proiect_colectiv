from camelot.admin.entity_admin import EntityAdmin
from camelot.core.orm import Entity
from sqlalchemy import Column, Integer, String, ForeignKey

__author__ = 'Roland'


class ResursaLogistica(Entity):
    __tablename__ = 'resurse_logistice'

    id = Column(Integer, primary_key=True)
    type = Column(String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'resursa',
        'polymorphic_on': type
    }

    class Admin(EntityAdmin):
        verbose_name = 'Resursa'
        verbose_name_plural = 'Resurse'
        list_display = ['type']


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
        return self.nume + str(self.nr_locuri)

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

    __mapper_args__ = {
        'polymorphic_identity': 'echipament',
    }

    def __unicode__(self):
        return self.tip + str(self.cantitate)

    class Admin(EntityAdmin):
        verbose_name = 'Echipament'
        verbose_name_plural = 'Echipamente'
        list_display = ['tip', 'cantitate']