# -*- coding: utf-8 -*-
from flask_uploads import UploadSet, IMAGES, configure_uploads, ALL
from flask import request, Flask, redirect, url_for, render_template, abort
import os

app = Flask(__name__)
app.config['UPLOADED_PHOTO_DEST'] = os.path.dirname(os.path.abspath(__file__))
app.config['UPLOADED_PHOTO_ALLOW'] = IMAGES
#def dest(name):
#    return '{}/{}'.format(UPLOAD_DEFAULT_DEST, name)
#app.config['UPLOAD_PHOTO_URL'] = 'http://localhost:5000/'
photos = UploadSet('PHOTO')


configure_uploads(app, photos)

@app.route('/', methods=['POST', 'GET'])
def upload():
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        return redirect(url_for('show', name=filename))
    return render_template('upload.html')


@app.route('/photo/<name>')
def show(name):
    if name is None:
        abort(404)
    url = photos.url(name)
    return render_template('SHOW.html', url=url, name=name)

app.run()
