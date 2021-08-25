from app import create_app,db
from flask_script import Manager,Server
from flask_migrate import Migrate
from app.models import User,Subscriber,Comment,Blog

# creating an app instance
app = create_app('development')



manager = Manager(app)
manager.add_command('server',Server)

migrate = Migrate(app,db)
manager.add_command('db')


@app.shell_context_processor
def make_shell_context():
    return dict(app = app, db = db , User = User,Subscriber = Subscriber, Comment = Comment,Blog = Blog)

