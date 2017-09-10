# -*- coding: utf-8 -*-
from flask import Flask, render_template, request
from werkzeug.routing import BaseConverter
app = Flask(__name__)

class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex=items[0]#regex的属性名不能改动

app.url_map.converters['regex']=RegexConverter


@app.route('/')
def hello_world():
    return render_template('frame.html')


@app.route('/bottom/')
def bottom():
    return render_template('bottom.html')


@app.route('/<int:id>')
def dyn(id):
    return 'id is %d.' % id


@app.route('/<regex("[a-z]{3}"):user_name>')
def regx(user_name):
    return 'name is %s.' % user_name

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html', method=request.method)

if __name__ == '__main__':
    app.run(debug=True)