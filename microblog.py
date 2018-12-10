# from app import app
# from app.models import db, User, Post
# @app.shell_context_processor
# def maka_shell_context():
#     return {'db':db, 'User':User, 'Post':Post}

from app import create_app, db, cli
from app.models import User, Post

app = create_app()
cli.register(app)


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}