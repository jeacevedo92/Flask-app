from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from application import application, db

#Commands to migrate
migrate = Migrate(application, db)
manager = Manager(application)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()


#Follow these commands to migrate your database
#python3 manage.py db init
#python3  manage.py db migrate
#python3 manage.py db upgrade
