from flask import Flask,request,url_for,redirect,render_template,flash, send_from_directory
import os
import jinja2
import json
import datetime
from werkzeug.utils import secure_filename
from pathlib import Path
import templater as template
import platform
import requests
import verbose
import re
regex = r"\$[ \*,]+\$"
app = Flask(__name__, static_url_path='')
if platform.system() == 'Windows':
    UPLOAD_FOLDER = Path(__file__).parent.joinpath('uploads')
else:
    UPLOAD_FOLDER = r'uploads'

ALLOWED_EXTENSIONS = set(['docx','xlsx','txt','png'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/img/<path:path>')
def staic_img(path):
    return send_from_directory('static/img', path)

@app.route('/')
def homepage():
    db={'Semester-1':{'S1Subject-1':['Module-1','Module-2','Module-3','Module-4'],'S1Subject-2':['Module-1','Module-2','Module-3','Module-4'],'S1Subject-3':['Module-1','Module-2','Module-3','Module-4']},'Semester-2':{'S2Subject-1':['Module-1','Module-2','Module-3','Module-4'],'S2Subject-2':['Module-1','Module-2','Module-3','Module-4'],'S2Subject-3':['Module-1','Module-2','Module-3','Module-4']},'Semester-3':{'S3Subject-1':['Module-1','Module-2','Module-3','Module-4'],'S3Subject-2':['Module-1','Module-2','Module-3','Module-4'],'S3Subject-3':['Module-1','Module-2','Module-3','Module-4']},'Semester-4':{'S4Subject-1':['Module-1','Module-2','Module-3','Module-4'],'S4Subject-2':['Module-1','Module-2','Module-3','Module-4'],'S4Subject-3':['Module-1','Module-2','Module-3','Module-4']}}
    return render_template('upload.html',db=db)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file uploaded')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        
        data = request.form.to_dict(flat= True)
        print(data)

# @app.route('/<name>')
# def personal(name):
# 	return 'hello '+name+' world'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


	
if __name__=='__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)