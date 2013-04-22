from sqlalchemy.schema import Column
from camelot.admin.entity_admin import EntityAdmin
from camelot.core.orm import Entity
from sqlalchemy import Unicode, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey
from rms.Model import ResurseUmane


class OreSuplimentare(Entity):
    __tablename__ = 'ore_suplimentare'

    preg_admitere = Column(Integer)
    comisii_absolvire = Column(Integer)
    consultatii = Column(Integer)
    examene = Column(Integer)
    indr_lucr_disert = Column(Integer)
    indr_lucr_lic = Column(Integer)
    indr_proiect = Column(Integer)
    lucr_control = Column(Integer)
    seminarii_cerc = Column(Integer)
    id_profesor = Column(Integer,ForeignKey('resurse_umane.id'))

    profesor = relationship('ResurseUmane')

    def __init__(self, preg_admitere=None, comisii_absolvire=None, consultatii=None, examene=None,
                 indr_lucr_disert=None, indr_lucr_lic=None, indr_proiect=None, lucr_control=None,  seminarii_cerc=None):
        if preg_admitere:
            self.preg_admitere = preg_admitere
            self.comisii_absolvire = comisii_absolvire
            self.consultatii = consultatii
            self.examene = examene
            self.indr_lucr_disert = indr_lucr_disert
            self.indr_lucr_lic = indr_lucr_lic
            self.indr_proiect = indr_proiect
            self.lucr_control = lucr_control
            self.seminarii_cerc = seminarii_cerc

    def __unicode__(self):
        return self.profesor or 'Unknown'

    # @todo fix this
    class Admin(EntityAdmin):
        verbose_name = 'Ore Sup'
        verbose_name_plural = 'Ore SUp'
        list_display = ['profesor', 'preg_admitere', 'comisii_absolvire', 'consultatii', 'examene', 'indr_lucr_disert',
                        'indr_lucr_lic', 'indr_proiect', 'lucr_control', 'seminarii_cerc']
