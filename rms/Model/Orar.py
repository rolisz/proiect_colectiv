from sqlalchemy.schema import Column
import sqlalchemy.types
from camelot.admin.entity_admin import EntityAdmin
from camelot.core.orm import Entity
from sqlalchemy import Unicode, Date, Integer, Boolean, String
from sqlalchemy.orm import relationship
from sqlalchemy.schema import ForeignKey

zile = {'Luni': 1, 'Marti': 2, 'Miercuri': 3, 'Joi': 4, ' Vineri': 5}

class Orar(Entity):
    __tablename__ = 'orar'

    zi = Column(Integer, nullable=False)
    ora = Column(String(30), nullable=False)
    frecventa = Column(Integer, nullable=False)
    sala = Column(String(6), nullable=False)
    anul = Column(String(10), nullable=False)
    formatia = Column(String(5), nullable=False)
    tip = Column(Integer, nullable=False)
    disciplina = Column(String(30), nullable=False)

    def __init__(self, zi=None, ora=None, frecventa=None, sala=None,
                 anul=None, formatia=None, tip=None, disciplina=None):
        if zi:
            self.zi = zile[zi]
            self.ora = ora
            self.frecventa = frecventa
            self.sala = sala
            self.anul = anul
            self.formatia = formatia
            if tip == 'L':
                self.tip = 1
            elif tip == 'S':
                self.tip = 2
            elif tip == 'C':
                self.tip = 3
            else:
                raise Exception("Tip de ora invalid")
            self.disciplina = disciplina


    def __unicode__(self):
        return self.sala or 'Unknown'

    class Admin(EntityAdmin):
        verbose_name = 'Orar'
        verbose_name_plural = 'Orar'
        list_display = ['zi', 'ora', 'frecventa', 'sala', 'anul', 'formatia', 'tip', 'disciplina']
        field_attributes = {
            'zi': {'choices': lambda o: [(v,k) for k,v in zile.items()]
            },
            'frecventa': {'choices': lambda o: [(0, 'Saptamanal'),
                                                (1, 'Saptamana para'),
                                                (2, 'Saptamana impara')]},
            'tip': {'choices': lambda o: [(1, 'Laborator'),
                                          (2, 'Seminar'),
                                          (3, 'Curs')]}
        }
    class Admin2(EntityAdmin):
            verbose_name = 'Orar'
            verbose_name_plural = 'Orar'
            list_display = ['zi', 'ora', 'frecventa', 'sala', 'anul', 'formatia', 'tip', 'disciplina']
            field_attributes = {    
            'zi': {'choices': lambda o: [(v,k) for k,v in zile.items()]
            },
            'frecventa': {'choices': lambda o: [(0, 'Saptamanal'),
                                                (1, 'Saptamana para'),
                                                (2, 'Saptamana impara')]},
            'tip': {'choices': lambda o: [(1, 'Laborator'),
                                          (2, 'Seminar'),
                                          (3, 'Curs')]}
        }
    Admin2 = not_editable_admin(Admin2)
