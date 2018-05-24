from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app import create_app, db
from app.models import User, Pitch, Comment


#creating app instance
app = create_app('development')

manage = Manager(app)
Migrate = Migrate(app, db)

manage.add_command('server', Server)
manage.add_command('db', MigrateCommand)


@manage.command
def test():
    '''
    Running unit tests
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manage.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Pitch=Pitch, Comment=Comment)


if __name__ == '__main__':
    manage.run()