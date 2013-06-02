
import logging
from camelot.core.conf import settings, SimpleSettings
from sqlalchemy.orm import Session
from rms.Model.ResurseUmane import Profesor, Director

logging.basicConfig( level = logging.ERROR )
logger = logging.getLogger( 'main' )

# begin custom settings
def baga_date():
    from camelot.model.fixture import Fixture
    # session = Session()
    Fixture.insert_or_update_fixture(Profesor, fixture_key = 'prof',
                            values = dict(username="tzutzu",nume="Dan Suciu", doctorat=True, den_post="Lector",titular=True))
    Fixture.insert_or_update_fixture(Director, fixture_key = 'director',
                            values = dict(username="Roland",nume="Szabo Roland", doctorat=True))


class MySettings( SimpleSettings ):

    # add an ENGINE or a CAMELOT_MEDIA_ROOT method here to connect
    # to another database or change the location where files are stored
    #
    def ENGINE( self ):
        from sqlalchemy import create_engine
        return create_engine( 'sqlite:///model-data.sqlite' )
    
    def setup_model( self ):
        """This function will be called at application startup, it is used to 
        setup the model"""
        from camelot.core.sql import metadata
        from sqlalchemy.orm import configure_mappers
        metadata.bind = self.ENGINE()
        import camelot.model.authentication
        import camelot.model.i18n
        import camelot.model.memento
        import camelot.model.fixture
        import rms.model
        configure_mappers()
        metadata.create_all()
        baga_date()

my_settings = MySettings( 'Roland', 'Resource Management System' )

settings.append( my_settings )
# end custom settings

def start_application():
    from camelot.view.main import main
    from rms.application_admin import MyApplicationAdmin
    main(MyApplicationAdmin())

if __name__ == '__main__':
    start_application()
    