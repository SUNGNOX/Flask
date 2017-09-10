# -*- coding: utf-8 -*-
from flask import Flask, render_template
from flask.ext.script import Manager
from livereload import Server

app = Flask(__name__)
app.config['DEBUG'] = True
manager = Manager(app)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/serve')
def serve():
    return 'Hello World!'


@app.route('/about')
def about():
    return 'Hello World!'


@app.route('/context')
def context():
    return 'Hello World!'


@manager.command
def dev():
    live_server = Server(app.wsgi_app)
    live_server.watch('**/*.*') # 可用正则表达式
    live_server.serve(open_url=True)

if __name__ == '__main__':
    manager.run()