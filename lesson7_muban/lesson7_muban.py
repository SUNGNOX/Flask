# -*- coding: utf-8 -*-
#本课程讲解的是模板的原理
#在jinja用过滤器‘\safe’禁止自动转义，还可以用template_filter装饰器定义过滤器
#context_processor装饰器定义上下文处理器，使python中的函数应用到html
from flask import Flask, render_template
from flask.ext.script import Manager
from livereload import Server
from markdown import markdown
app = Flask(__name__)
manager = Manager(app)


@manager.command
def dev():
    live_serve = Server(app.wsgi_app)
    live_serve.watch('E:\\python\\flask\\myproject\\lesson7_muban\\templates\\hello.html')
    live_serve.serve(open_url=True)


@app.route('/')
def hello_world():
    return render_template('hello.html', title='<h1>hello word!</h1>', body='## markdown!!')


@app.template_filter('md')
def mark2html(txt):
    return markdown(txt)


def readfile(file):
    with open(file) as f:
        text=reduce(lambda x,y:x+y, f.readlines())
    return text.decode('utf-8')


@app.context_processor
def cntxtp():
    return dict(readfile=readfile)


if __name__ == '__main__':
    manager.run()

