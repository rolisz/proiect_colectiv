from camelot import model
from camelot.admin.not_editable_admin import not_editable_admin
from sqlalchemy.schema import Column
import sqlalchemy.types
from camelot.admin.entity_admin import EntityAdmin
from camelot.core.orm import Entity, ManyToOne, Session
from sqlalchemy import Unicode, Date, Integer, Boolean, String
from rms.Model.Discipline import Discipline
from rms.Model.ResurseUmane import ResurseUmane, Profesor

zile = ['Luni', 'Marti', 'Miercuri', 'Joi', 'Vineri']

class Orar(Entity):
    __tablename__ = 'orar'

    zi = Column(Integer, nullable=False)
    ora = Column(String(30), nullable=False)
    frecventa = Column(Integer, nullable=False)
    sala = Column(String(6), nullable=False)
    anul = Column(String(10), nullable=False)
    formatia = Column(String(5), nullable=False)
    tip = Column(Integer, nullable=False)
    disciplina = ManyToOne('Discipline')
    disc = Column(String(20))

    def __init__(self, zi=None, ora=None, frecventa=None, sala=None,
                 anul=None, formatia=None, tip=None, disciplina=None):
        if zi:
            self.zi = zile.index(zi) + 1
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
            self.disc = disciplina


    def __unicode__(self):
        return self.sala + str(self.disciplina) or 'Unknown'

    class Admin(EntityAdmin):
        verbose_name = 'Orar'
        verbose_name_plural = 'Orar'
        list_display = ['zi', 'ora', 'frecventa', 'sala', 'anul', 'formatia', 'tip', 'disciplina']
        field_attributes = {
            'zi': {'choices': lambda o: [(k+1,v) for k,v in enumerate(zile)]
            },
            'frecventa': {'choices': lambda o: [(0, 'Saptamanal'),
                                                (1, 'Saptamana para'),
                                                (2, 'Saptamana impara')]},
            'tip': {'choices': lambda o: [(1, 'Laborator'),
                                          (2, 'Seminar'),
                                          (3, 'Curs')]}
        }

    class AdminCadru(Admin):

        def get_query(self):
            session = Session
            user = session.query(ResurseUmane).filter(
                ResurseUmane.username == model.authentication.get_current_authentication().username).first()
            if user is not None and user.functie == 'Profesor':
                return session.query(Orar).join(Discipline).join(Profesor).filter(
                    Profesor.id == user.id)
            else:
                return session.query(Orar)

    AdminCadru = not_editable_admin(AdminCadru)

    class AdminPublic(Admin):
        list_filter = ['disciplina', 'anul', 'formatia', 'zi']
    AdminPublic = not_editable_admin(AdminPublic)
