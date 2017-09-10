from app import create_app
from flask_script import Manager

app = create_app()
manager = Manager(app)


if __name__ == '__main__':
#    manager.run()
    from livereload import Server
    lvrld = Server(app.wsgi_app)
    lvrld.watch('**/*.*')
    lvrld.serve(open_url=True)


@manager.command
def dev():
    from livereload import Server
    lvrld = Server(app.wsgi_app)
    lvrld.watch('**/*.*')
    lvrld.serve(open_url=False)