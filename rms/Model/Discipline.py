from sqlalchemy.schema import Column
from camelot.admin.entity_admin import EntityAdmin
from camelot.core.orm import Entity, ManyToOne, OneToMany, ManyToMany
from sqlalchemy import Unicode, Integer, String

class Discipline(Entity):
    __tablename__ = 'discipline'

    disc = Column(String(10))
    sectia = Column(String(10))
    anul = Column(Integer)
    curs_sem1 = Column(Integer)
    sem_sem1 = Column(Integer)
    lab_sem1 = Column(Integer)
    curs_sem2 = Column(Integer)
    sem_sem2 = Column(Integer)
    lab_sem2 = Column(Integer)
    titular = ManyToOne('Profesor')
    orar = OneToMany('Orar')
    programe_studii = ManyToOne('ProgramStudiu')


    def __init__(self, disc=None, sectia=None, anul=None, curs_sem1=None,
                 sem_sem1=None, lab_sem1=None, curs_sem2=None, sem_sem2=None,
                 lab_sem2=None):
        if disc:
            self.disc = disc
            self.sectia = sectia
            self.anul = anul
            self.curs_sem1 = curs_sem1
            self.sem_sem1 = sem_sem1
            self.lab_sem1 = lab_sem1
            self.curs_sem2 = curs_sem2
            self.sem_sem2 = sem_sem2
            self.lab_sem2 = lab_sem2

    def __unicode__(self):
        return self.disc or 'Unknown'

    class Admin(EntityAdmin):
        verbose_name = 'Disciplina'
        verbose_name_plural = 'Discipline'
        list_display = ['disc', 'sectia', 'anul', 'curs_sem1', 'sem_sem1',
                        'lab_sem1', 'curs_sem2', 'sem_sem2', 'lab_sem2', 'titular']
        field_attributes = {
            'disc': {'name': 'Disciplina'},
            'curs_sem1': {'name': 'Ore curs semestrul 1'},
            'sem_sem1': {'name': 'Ore seminar semestrul 1'},
            'lab_sem1': {'name': 'Ore laborator semestrul 1'},
            'curs_sem2': {'name': 'Ore curs semestrul 2'},
            'sem_sem2': {'name': 'Ore seminar semestrul 1'},
            'lab_sem2': {'name': 'Ore laborator semestrul 1'}
        }

    class AdminProf(Admin):
        list_display = ['disc', 'sectia', 'anul', 'curs_sem1', 'sem_sem1',
                        'lab_sem1', 'curs_sem2', 'sem_sem2', 'lab_sem2']

    class AdminProgram(Admin):
        list_display = ['disc', 'anul', 'curs_sem1', 'sem_sem1',
                        'lab_sem1', 'curs_sem2', 'sem_sem2', 'lab_sem2']

