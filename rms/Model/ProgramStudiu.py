from camelot.view.forms import Form, TabForm
from sqlalchemy.schema import Column
from camelot.admin.entity_admin import EntityAdmin
from camelot.core.orm import Entity, ManyToMany, OneToMany
from sqlalchemy import Unicode, Date, Integer, Text


class ProgramStudiu(Entity):
    __tablename__ = 'ProgramStudiu'

    nivel = Column(Integer, nullable=False, default=1)
    sectie = Column(Unicode(30))
    durata = Column(Integer, nullable=False, default=1)
    credite = Column(Integer, nullable=False, default=1)
    descriere = Column(Text(500))
    discipline = OneToMany('Discipline')
    cercuri = OneToMany('Cercuri')

    def __unicode__(self):
        return self.sectie or 'Unknown'

    class Admin(EntityAdmin):
        verbose_name = 'Programe Studiu'
        verbose_name_plural = 'Programe Studiu'
        list_display = ['nivel', 'sectie', 'durata', 'credite', 'descriere']
        form_display = TabForm([('Detalii program studiu', Form(list_display)),
                                ('Materii predate', Form(['discipline']))])
        field_attributes = {'nivel': {'choices': lambda o: [(1, 'Licenta'), (2, 'Master')]},
                            'credite': {'minimum': 0, 'maximum': 180},
                            'durata': {
                            'choices': lambda o: [(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6')]}}

