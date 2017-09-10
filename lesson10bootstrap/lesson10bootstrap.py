# -*- coding: utf-8 -*-
from flask import Flask, render_template, flash, url_for, request, redirect
from livereload import Server
from werkzeug.utils import secure_filename
#from flask.ext.bootstrap import Bootstrap
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import *

from os import path
app = Flask(__name__)
Bootstrap(app)
app.config['DEBUG'] = True#若要实现自动加载页面，千万不能缺少这个
app.config.from_pyfile('config')

nav = Nav()
nav.register_element('top', Navbar(u'导航栏',
                     View(u'主页', 'index'),
                     View(u'服务', 'serve'),
                     View(u'关于', 'about'),
                     View(u'内容', 'context'),
                     View(u'登录', 'login')
                     ))
nav.init_app(app)


@app.route('/')
def hello_world():
    return render_template('index.html', name="WELCOM")


@app.route('/index')
def index():
    return render_template('index.html', name="WELCOM")

@app.route('/serve',methods=['GET', 'POST'])
def serve():
#    if request.method == 'GET':
 #       return render_template('upload.html')
    from upload_form import UploadForm
    uploadform = UploadForm()
    f = request.files['file']
    uploadpath = path.join('E:\python\upload', f.filename)
    f.save(uploadpath )
    return render_template('upload.html',uploadform=uploadform)


@app.route('/login', methods=['POST', 'GET'])#methods不要忘了s
def login():
    from forms import LoginForm
    form0 = LoginForm()
    flash(u'登陆成功!!')
    return render_template('login.html', title=u'登录', form0=form0)


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


def readfile(file):
    with open(file) as f:
        text=reduce(lambda x,y:x+y, f.readlines())
    return text.decode('utf-8')


@app.context_processor
def cntxtp():
    return dict(readfile=readfile)

if __name__ == '__main__':
    lvrld = Server(app.wsgi_app)
    lvrld.watch('**/base.html')
    lvrld.serve(open_url=True)
    app.run(debug=True)
