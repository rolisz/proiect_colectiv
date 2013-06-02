from rms.Model.Discipline import Discipline

__author__ = 'Roland'

from camelot.admin.action import Action


class ImportException(Exception):
    pass


class ImportOrar(Action):
    verbose_name = 'Importare orar'

    def model_run(self, model_context):
        from camelot.view.action_steps import (SelectFile,
                                               UpdateProgress,
                                               Refresh,
                                               FlushSession)

        select_files = SelectFile('Txt Files (*.txt *.csv);;All Files (*)')
        select_files.single = False
        file_names = yield select_files
        file_count = len(file_names)

        import os
        from camelot.core.orm import Session
        from rms.Model.Orar import Orar

        session = Session()

        for i, file_name in enumerate(file_names):
            yield UpdateProgress(i, file_count)
            title = os.path.splitext(os.path.basename(file_name))[0]
            print(file_name)
            for line in open(file_name):
                vals = line.split(';')[:-1]
                if len(vals) != 8:
                    raise ImportException("Fisierul nu e dat bine")
                if vals[2] not in ['0', '1', '2']:
                    raise ImportException("Frecventa nu e data bine")
                print(vals)
                orar = Orar(*vals)
                print(orar)
                session.add(orar)
                disc = session.query(Discipline).filter(Discipline.disc==orar.disc).first()
                if disc:
                    orar.disciplina = disc
                    session.flush()

        yield FlushSession(session)
        # begin refresh
        yield Refresh()
        # end refresh