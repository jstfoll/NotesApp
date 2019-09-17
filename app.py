from flask import Flask,request,url_for,redirect,render_template,flash, send_from_directory
import os
import jinja2
import json
import datetime
from werkzeug.utils import secure_filename
from pathlib import Path
import platform
import requests

app = Flask(__name__, static_url_path='')
if platform.system() == 'Windows':
    UPLOAD_FOLDER = Path(__file__).parent.joinpath('uploads')
else:
    UPLOAD_FOLDER = r'uploads'

ALLOWED_EXTENSIONS = set(['docx','xlsx','txt','png','pdf','jpeg','pptx','doc','ppt'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/img/<path:path>')
def staic_img(path):
    return send_from_directory('static/img', path)

@app.route('/')
def homepage():
    db={ "Semester-1": { "Engg Physics": [ "Module-1", "Module-2", "Module-3", "Module-4", "Module-5" ], "Basic Electrical": [ "Module-1", "Module-2", "Module-3", "Module-4", "Module-5" ], "EGDL": [ "Module-1", "Module-2", "Module-3", "Module-4", "Module-5" ], "CIVIL Engg": [ "Module-1", "Module-2", "Module-3", "Module-4", "Module-5" ], "English": [ "Module-1", "Module-2", "Module-3", "Module-4", "Module-5" ], "Mathematics-1": [ "Module-1", "Module-2", "Module-3", "Module-4", "Module-5" ] }, "Semester-2": { "Mathematics-2": [ "Module-1", "Module-2", "Module-3", "Module-4", "Module-5" ], "Engg Chemistry": [ "Module-1", "Module-2", "Module-3", "Module-4", "Module-5" ], "Elements Mechanical Engg": [ "Module-1", "Module-2", "Module-3", "Module-4", "Module-5" ], "CPS": [ "Module-1", "Module-2", "Module-3", "Module-4", "Module-5" ], "Basic Electronics": [ "Module-1", "Module-2", "Module-3", "Module-4", "Module-5" ], "English": [ "Module-1", "Module-2", "Module-3", "Module-4", "Module-5" ] }, "Semester-3": { "Mathematics 3": [ "Module-1", "Module-2", "Module-3", "Module-4", "Module-5" ], "Data Structures": [ "Module-1", "Module-2", "Module-3", "Module-4", "Module-5" ], "Software Engineering": [ "Module-1", "Module-2", "Module-3", "Module-4", "Module-5" ], "Computer Organisation": [ "Module-1", "Module-2", "Module-3", "Module-4", "Module-5" ], "Analog and Digital Electronics": [ "Module-1", "Module-2", "Module-3", "Module-4", "Module-5" ], "Discrete Mathematical Structures": [ "Module-1", "Module-2", "Module-3", "Module-4", "Module-5" ] } }
    return render_template('upload.html',db=db)


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        
        if 'file' not in request.files:
            flash('No file uploaded')
            return redirect(request.url)
        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        data = request.form.to_dict(flat= True)
        if any(value == '' for value in data.values()):
            flash("All fields are mandatory")
            return redirect(url_for('.upload'))
        filename=''
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filename=filename.split('.')[-1]
            ffname=data['Semester']+'//'+data['Subject']+'//'+data['Module']
            ffname1=data['file_name'].replace(' ','_')+'.'+filename
            if(os.path.exists(os.path.join(app.config['UPLOAD_FOLDER'],ffname))):
                file.save(str(os.path.join(app.config['UPLOAD_FOLDER'],ffname,ffname1)))
            else:
                os.makedirs(os.path.join(app.config['UPLOAD_FOLDER'],ffname))
                file.save(str(os.path.join(app.config['UPLOAD_FOLDER'],ffname,ffname1)))
            print("***************************")
            print(f"File {data['file_name']+'.'+filename} Saved")
            print("***************************")

        
        data = request.form.to_dict(flat= True)
        print(data)
        return render_template("success.html",file=data['file_name']+'.'+filename)

# @app.route('/<name>')
# def personal(name):
# 	return 'hello '+name+' world'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


	
if __name__=='__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)