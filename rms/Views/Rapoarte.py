from camelot.admin.action import Action
import rms

__author__ = 'Roland'


class RapoarteActivitati(Action):
    verbose_name = "Rapoarte folosire activitati"

    def model_run(self, model_context):
        from camelot.view.action_steps import PrintHtml
        import datetime
        import os
        from jinja import Environment, FileSystemLoader
        from pkg_resources import resource_filename

        fileloader = FileSystemLoader(resource_filename(rms.__name__, 'templates'))
        e = Environment(loader=fileloader)
        activitate = model_context.get_object()
        context = {
            'header': activitate.nume,
            'title': 'Raport activitate',
            'style': '.label { font-weight:bold; }',
            'coordonator': activitate.coordonator,
            'aprobata': activitate.aprobata,
            'membrii': activitate.membrii,
            'res_fin': activitate.res_fin,
            'res_log': activitate.res_logistice,
            'footer': str(datetime.datetime.now().year)
        }
        t = e.get_template('activitate.html')
        yield PrintHtml(t.render(context))


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

class RaportResurseUmane(Action):
    verbose_name = "Rapoarte folosire resurse umane"

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
            'title': 'Raport resurse umane',
            'style': '.label { font-weight:bold; }',
            'persoana': resursa,
            'footer': str(datetime.datetime.now().year)
        }
        t = e.get_template('resurse_umane.html')
        yield PrintHtml(t.render(context))