# -*- coding: utf-8 -*-
from flask import Flask, render_template, request, redirect, url_for,make_response,abort
from werkzeug.utils import secure_filename
from os import path
#请求响应及上传
app = Flask(__name__)


@app.route('/')
def hello_world():
    response = make_response(render_template('index.html'))
    response.set_cookie('username', '')
    return response


@app.route('/login', methods=['POST', 'GET'])#methods不要忘了s
def login():
    if request.method == 'POST':
        user = request.form.get('username')
        passwd = request.form.get('password')
    elif request.method == 'GET':
        user = request.form.get('username')
        passwd = request.form.get('password')
    return render_template('login.html', method=request.method, U=user, P=passwd)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']#files为字典类型
        abspath = path.abspath(path.dirname(__file__))
#        upload_path=path.join(abspath, 'static/upload')
        upload_path = path.join(abspath, 'static\upload', secure_filename(f.filename))#视频上的代码如上，这段为修改后的代码
        f.save(upload_path)
        return redirect(url_for('upload'))
    return render_template('upload.html')


@app.errorhandler(404)
def not_found():
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
