import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from flask.ext.script import Manager, Server
from flask_blog import app

manager = Manager(app)
manager.add_command("runserver", Server(use_debugger=True, use_reloader=True))

if __name__ == '__main__':
	manager.run()