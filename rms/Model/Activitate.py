from sqlalchemy.schema import Column
from camelot.admin.entity_admin import EntityAdmin
from camelot.core.orm import Entity, ManyToMany
from sqlalchemy import Unicode, Date, Integer, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey


class Activitate(Entity):
    __tablename__ = 'activitati'

    id_coordonator = Column(Integer, ForeignKey('resurse_umane.id'))
    nume = Column(Unicode(50))
    coordonator = relationship('ResurseUmane')
    tip = Column(Integer)
    aprobata = Column(Boolean)

    echipa_activitate = relationship('EchipaActivitate')
    faze_activitate = relationship('FazeActivitate')
    resurse_activitate = relationship('ResurseActivitate')

    def __unicode__(self):
        return self.echipa_activitate or 'Unknown'

    class Admin(EntityAdmin):
        verbose_name = 'Activitate'
        verbose_name_plural = 'Activitati'
        list_display = ['coordonator', 'tip', 'aprobata', 'echipa_activitate',
                        'faze_activitate']

        form_display = ['coordonator', 'tip']
