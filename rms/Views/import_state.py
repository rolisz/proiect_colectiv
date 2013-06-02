from rms.Model.ResurseUmane import Profesor

__author__ = 'Roland'

from camelot.admin.action import Action


class ImportException(Exception):
    pass


class ImportState(Action):
    verbose_name = 'Importare stat functii'

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
        from rms.Model.ResurseUmane import ResurseUmane
        from rms.Model.Discipline import Discipline
        from rms.Model.OreSuplimentare import OreSuplimentare

        session = Session()

        for i, file_name in enumerate(file_names):
            yield UpdateProgress(i, file_count)
            print(file_name)
            f = open(file_name)
            info_prof = f.readline().split(";")[:-1]
            print(info_prof)
            prof = Profesor(**info_prof)
            session.add(prof)
            for line in f:
                if line[-1] == ';':
                    vals = line[:-1].split(',')
                else:
                    vals = line[:-2].split(',')


                print(vals)
                try:
                    vals[0] = int(vals[0])
                    oresup = OreSuplimentare(*vals)
                    oresup.profesor = prof
                    session.add(oresup)
                except ValueError:
                    disc = Discipline(*vals)
                    disc.profesor = prof
                    session.add(disc)
        yield FlushSession(session)
        # begin refresh
        yield Refresh()
        # end refresh