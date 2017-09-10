# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, url_for, redirect
from livereload import Server
from werkzeug.utils import secure_filename
from flask_nav import Nav
from flask_nav.elements import *
from os import path

app = Flask(__name__)
app.config['DEBUG'] = True#若要实现自动加载页面，千万不能缺少这个

nav = Nav()
nav.register_element('top', Navbar(u'导航栏',
                     View(u'服务', 'serve'),
                     View(u'关于', 'about'),
                     View(u'内容', 'context')
                     ))
nav.init_app(app)
@app.route('/')

@app.route('/')
def hello_world():
    return render_template('index.html', name="WELCOM")


@app.route('/serve',methods=['GET', 'POST'])
def serve():
    if request.method == 'GET':
        return render_template('upload.html')
    f = request.files['file']
#    basepath = path.abspath(path.dirname(__file__))
#    uploadpath = path.join(basepath, 'static\upload', secure_filename(f.filename))
    uploadpath = path.join('E:\python\upload', f.filename)
    f.save(uploadpath )
    return render_template('upload.html')


@app.route('/about')
def about():
    return 'Hello about!'


@app.route('/context')
def context():
    return 'Hello context!'


#自定义测试函数
@app.template_test('current_url')
def is_current_url(link):
    return link['href'] == url_for('context')
#    return link['href'] == request.url


if __name__ == '__main__':
    lvrld = Server(app.wsgi_app)
    lvrld.watch('**/*.html')
    lvrld.serve(open_url=True)
