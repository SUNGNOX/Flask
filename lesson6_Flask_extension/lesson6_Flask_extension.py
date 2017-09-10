# -*- coding: utf-8 -*-
from flask import Flask, render_template
#Flask_script扩展包的Maanager
from flask.ext.script import Manager

app = Flask(__name__)
manager = Manager(app)
app.config['DEBUG']=True

@app.route('/')
def hello_world():
    return render_template('hello.html')


@manager.command
def hello():
    return 'Manager exercise!!!!!!'


@manager.command
def dev():
    #Server可以实现实时监控刷新
    from livereload import Server
    lvlod = Server(app.wsgi_app)
    lvlod.watch('**\*.*')
    lvlod.serve(open_url=True)

if __name__ == '__main__':
    manager.run()
#    app.run()
