from camelot.admin.action import Action
from camelot.admin.entity_admin import EntityAdmin
from camelot.admin.not_editable_admin import not_editable_admin
from camelot.core.orm import Entity, ManyToMany, Session
from sqlalchemy import Column, Integer, String, ForeignKey
import rms

__author__ = 'Roland'


class RaportResurse(Action):
    verbose_name = "Rapoarte folosire resurse"

    def model_run(self, model_context):
        from camelot.view.action_steps import PrintHtml
        import datetime
        import os
        from jinja import Environment, FileSystemLoader
        from pkg_resources import resource_filename

        fileloader = FileSystemLoader(resource_filename(rms.__name__, 'templates'))
        e = Environment(loader=fileloader)
        resursa = model_context.get_object()
        context = {
            'header': resursa.nume,
            'title': 'Raport resurse',
            'style': '.label { font-weight:bold; }',
            'activitati': resursa.activitati,
            'footer': str(datetime.datetime.now().year)
        }
        t = e.get_template('resurse_logistice.html')
        yield PrintHtml(t.render(context))


class ResursaLogistica(Entity):
    __tablename__ = 'resurse_logistice'

    id = Column(Integer, primary_key=True)
    type = Column(String(50))

    activitati = ManyToMany('Activitate')
    __mapper_args__ = {
        'polymorphic_identity': 'resursa',
        'polymorphic_on': type
    }

    class Admin(EntityAdmin):
        verbose_name = 'Resursa'
        verbose_name_plural = 'Resurse'
        list_display = ['type']
        form_actions = [RaportResurse()]

    class Admin2(EntityAdmin):
        verbose_name = 'Resursa Logistica'
        verbose_name_plural = 'Resurse Logistice'
        list_display = ['id', 'type']

    Admin2 = not_editable_admin(Admin2)

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
        return self.nume + " " + str(self.nr_locuri)

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
        return self.tip + " " + str(self.cantitate)

    class Admin(EntityAdmin):
        verbose_name = 'Echipament'
        verbose_name_plural = 'Echipamente'
        list_display = ['tip', 'cantitate']