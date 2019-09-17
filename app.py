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

ALLOWED_EXTENSIONS = set(['xml','xlsx'])
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/img/<path:path>')
def staic_img(path):
    return send_from_directory('static/img', path)

@app.route('/')
def homepage():
    db={'Semester-1':{'S1Subject-1':['Module-1','Module-2','Module-3','Module-4'],'S1Subject-2':['Module-1','Module-2','Module-3','Module-4'],'S1Subject-3':['Module-1','Module-2','Module-3','Module-4']},'Semester-2':{'S2Subject-1':['Module-1','Module-2','Module-3','Module-4'],'S2Subject-2':['Module-1','Module-2','Module-3','Module-4'],'S2Subject-3':['Module-1','Module-2','Module-3','Module-4']},'Semester-3':{'S3Subject-1':['Module-1','Module-2','Module-3','Module-4'],'S3Subject-2':['Module-1','Module-2','Module-3','Module-4'],'S3Subject-3':['Module-1','Module-2','Module-3','Module-4']},'Semester-4':{'S4Subject-1':['Module-1','Module-2','Module-3','Module-4'],'S4Subject-2':['Module-1','Module-2','Module-3','Module-4'],'S4Subject-3':['Module-1','Module-2','Module-3','Module-4']}}
    return render_template('upload.html',db=db)

@app.route('/creator')
def creator():
	return render_template('create.html')

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

        print(request.form)
        data = request.form.to_dict(flat= True)
        page=data["template"]
        lang=data["lang"] 
        if 'base_country' in data:
            bc=data['base_country']
        else:
            bc = ""
        if 'dest_country' in data:
            dc=data['dest_country']
        else:
            dc = ""
        print("****************************************")
        print(bc,dc)
        print("****************************************")
        convert=True
        if(bc=='' and dc==''):
            convert=False
        print(convert)

        if any(value == '' for value in data.values()):
            flash("All fields are mandatory")
            return redirect(url_for('.upload'))

        filename=''
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
        # print("******************************************")
        # print(os.path.join(app.config['UPLOAD_FOLDER'],filename ))
        md=template.stepify(os.path.join(app.config['UPLOAD_FOLDER'],filename),convert,bc,dc )
        title=list(md.keys())[0]
        prerequisites=[]
        steps=md[title]
        # print(steps)
        today = datetime.date.today()
        # title='Customer Project Management - Project-Based Services'
        description='''The Customer Project Management scope item realizes the key steps of the end-to-end process for Project Services. It integrates sales orders with project management,
        allowing you to create customer invoices for time and expenses - including external services - recorded against a customer project. Invoices can be created on a time and materials basis, a fixed-price basis, or a combination of both or as periodic services. You can also derive contract values and show whether the contract margin is on plan. After the customer invoice is issued, customer payments can be monitored. During period-end closing activities, accounting and financial close activities can be performed. This scope item also supports the analysis of project profitability based on project costs and revenues.
        This document provides a detailed procedure for testing the scope item after solution deployment, reflecting the predefined scope of the solution. Each process step is covered in its own section, providing the system interactions (that is, test steps) in a table view. Steps that are not in scope of the process but are needed for testing are marked accordingly (see the Test Step column). Customer-project-specific steps must be added.'''
        sections=[{'title': 'Create a New Customer Project', 'steps': ['']}]
        caldict={}
        for step in steps.keys():
            caldict[step]=[]
            for line in steps[step]:
                caldict[step].append(template.intermidify(line[2],line[1],line[0],line[3]))
                #Making call to Fiori Apps Library for pre-requisites
                if(line[2]=='AppTag' and len(line[1])>1):
                    url_test = "https://fioriappslibrary.hana.ondemand.com/sap/fix/externalViewer/services/SingleApp.xsodata/InputFilterParam(InpFilterValue='"+line[1]+"')/Results?$filter=substringof('SAP S/4HANA', releaseName) and (RoleNameCombined ne 'null')"
                    r = requests.get(url_test, headers={'Accept':'application/json'})
                    r_json = r.json()
                    try:
                        if(len(r_json['d']['results'])==1):
                            for value in r_json['d']['results']:
                                prerequisites.append([value['AppName'].split(','),value['BusinessRoleOAMName'].split('|'),re.compile(regex).split(value['BusinessRoleNameCombined'].strip('$')),value['ApplicationComponent']])
                                break
                        else:
                            for value in r_json['d']['results'][1:]:
                                prerequisites.append([value['AppName'].split(','),value['BusinessRoleOAMName'].split('|'),re.compile(regex).split(value['BusinessRoleNameCombined'].strip('$')),value['ApplicationComponent']])
                                break
                    except:
                        pass
        
        if lang != 'en':
            for step in caldict.keys():
                caldict[step] = template.translate(lang, caldict[step])

        # print(f'Caldict: {caldict}')
        fdict={}
        fdict[title]=caldict
        # print(fdict)
        # print("***********************************")
        # print(page)
        # print("***********************************")
        if(str(page)=="1"):
            return render_template('document.html', title=list(fdict.keys())[0], description=description, dict=fdict, date= today, prereq=prerequisites ,sections=fdict[list(fdict.keys())[0]])
        if(str(page)=="2"):
            return render_template('new_document.html', title=list(fdict.keys())[0], description=description, dict=fdict, date= today, prereq=prerequisites , sections=fdict[list(fdict.keys())[0]])


# @app.route('/<name>')
# def personal(name):
# 	return 'hello '+name+' world'

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


	
if __name__=='__main__':
	app.run(host='0.0.0.0', port=8080, debug=True)