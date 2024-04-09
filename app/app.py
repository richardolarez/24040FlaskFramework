# app.py
from flask import Flask, render_template, request, redirect, url_for, flash, make_response, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_wtf.csrf import CSRFProtect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt
import os



####################### FLASK APP CONFIGURATION ########################
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Set the SECRET_KEY configuration option

app.app_context()
db = SQLAlchemy(app)


###################### Import the TID Models ########################
from models import User, Projects, TIDTableRelationships, ChargeMode, Devices, GSENetwork, PathsLoads, PowerSupply, PowerSupplySummary, TelemetryNetwork, VehicleBattery, VehicleNetwork, UEIDaq, BatteryAddresses, TIDTables, Component


####################### CREATE TABLES ########################
class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(255))
    file_content = db.Column(db.LargeBinary)
    
with app.app_context(): 
    db.create_all()


########################## Login Manager ########################
bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.route('/register', methods=["GET", "POST"])
def register():
# If the user made a POST request, create a new user
	if request.method == "POST":
		user = User(username=request.form.get("username"),
					password=request.form.get("password"))
          
		user.password = bcrypt.generate_password_hash(request.form.get("password")).decode('utf-8')
		# Add the user to the database
		db.session.add(user)
		# Commit the changes made
		db.session.commit()
		# Once user account created, redirect them
		# to login route (created later on)
		return redirect(url_for("login"))
	# Renders sign_up template if user made a GET requestß
	return render_template("sign_up.html")


@app.route("/login", methods=["GET", "POST"])
def login():
	# If a post request was made, find the user by 
	# filtering for the username
	if request.method == "POST":
		user = User.query.filter_by(
			username=request.form.get("username")).first()
		# Check if the password entered is the 
		# same as the user's password
		if bcrypt.check_password_hash(user.password, request.form.get("password")):
		# Use the login_user method to log in the user
			login_user(user)
			return redirect(url_for("menu"))
	# Redirect the user back to the home
	# (we'll create the home route in a moment)
	return render_template("login.html")


############################ File Uploads ########################
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        decompress_file(filename)
        save_zip_to_db(filename)
        xml_file_path = find_xml_file(app.config['UPLOAD_FOLDER']) 
        if xml_file_path:
            output_file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'visioObjects4.txt')
            componentList = parseXML(xml_file_path, output_file_path, 4) #The last arguement is the projectID
            for i in componentList: 
                db.session.add(i)
                db.session.commit()
            return '''
            <!doctype html>
            <title>File uploaded</title>
            <h1>File uploaded successfully</h1>
            <a href="/download/visioObjects4.txt">Download visioObjects4.txt</a>
            '''
        else:
            return 'No data.xml file found for parsing'

#This was also added to allow for downloading the txt file so that it was possible to see if it was generated correctly. 
@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename, as_attachment=True)


import zipfile


def decompress_file(filename):
    zip_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(app.config['UPLOAD_FOLDER'])
    return f'{filename} decompressed and uploaded successfully'


def save_zip_to_db(filename):
    zip_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    with open(zip_path, 'rb') as file:
        data = Data(file_name=filename, file_content=file.read())
        db.session.add(data)
        db.session.commit()

    return 'Zip file saved to database successfully'

############################ PARSING #######################
import Parser.XML_Parser as XMLParse


#This function will find the xml file within the uploaded zip file folders
def find_xml_file(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == 'data.xml':
                return os.path.join(root, file)
    return None


def parseTXT(file_path, project_ID):
    checkNameList = ["[AV Network Switch]", "[Li-Ion Batt]", "[Controller]", "[DAQ-Digital]", "[DAQ-PPC]", "[Flight Computer]", "[GPS]", "[IMU]", "[Network Switch]", "[Ordnance]", "[PC - Server]", "[PDU]", "[Power Control Device]", "[PS]", "[TVC Controller]"]
    list1 = []
    for i in range(len(checkNameList)): 
        component_type = checkNameList[i]
        with open(file_path, 'r') as file:
            lines = file.readlines()
        parsed_data = []
        for j, line in enumerate(lines):
            if checkNameList[i] in line:
                start_index = max(0, j - 2)
                end_index = min(len(lines), j + 3)
                parsed_data.append(lines[start_index:end_index])
        for data in parsed_data:
            name_line = data[1].strip()  
            pn_line = data[3].strip()  
            unique_id_line = data[4].strip()
            obj_type = Component(name_line, unique_id_line, pn_line, component_type, project_ID)#The last argument is the projectID
            list1.append(obj_type)
    return list1


#This function will call the xmlParser and generate the txt file
def parseXML(input_file, output_file, project_id):
     XMLParse.run_XMLParser(input_file, output_file) 
     outputList = parseTXT(output_file, project_id)
     return outputList

######################## Get Component Functions #################### 
@app.route('/powerSupplies', methods=['GET'])
def getPowerSupplies(): 
     componentList = Component.query.filter_by(componentType='[PS]').all()
     return componentList

@app.route('/batteries', methods=['GET'])
def getBatteries(): 
     componentList = Component.query.filter_by(componentType='[Li-Ion Batt]').all()
     return componentList

@app.route('/powerControls', methods=['GET'])
def getPowerControls(): 
     componentList = Component.query.filter_by(componentType='[Power Control Device]').all()
     return componentList

@app.route('/DAQPPCs', methods=['GET'])
def getDAQPPC(): 
     componentList = Component.query.filter_by(componentType='[DAQ-PPC]').all()
     return componentList

@app.route('/flightComputers', methods=['GET'])
def getFlightComputers(): 
     componentList = Component.query.filter_by(componentType='[Flight Computers]').all()
     return componentList

@app.route('/ordnances', methods=['GET'])
def getOrdnance(): 
     componentList = Component.query.filter_by(componentType='[Ordnance]').all()
     return componentList

@app.route('/Controllers', methods=['GET'])
def getControllers(): 
     componentList = Component.query.filter_by(componentType='[Controller]').all()
     return componentList

@app.route('/pdus', methods=['GET'])
def getPdus(): 
     componentList = Component.query.filter_by(componentType='[PDU]').all()
     return componentList

@app.route('/DAQDigital', methods=['GET'])
def getDAQDigital(): 
     componentList = Component.query.filter_by(componentType='[DAQ-Digital]').all()
     return componentList

@app.route('/tvcControllers', methods=['GET'])
def getTvcControllers(): 
     componentList = Component.query.filter_by(componentType='[TVC Controller]').all()
     return componentList

@app.route('/GPS', methods=['GET'])
def getGPS(): 
     componentList = Component.query.filter_by(componentType='[GPS]').all()
     return componentList

@app.route('/networkSwitches', methods=['GET'])
def getNetworkSwitches(): 
     componentList = Component.query.filter_by(componentType='[Network Switch]').all()
     return componentList

@app.route('/IMUs', methods=['GET'])
def getIMUs(): 
     componentList = Component.query.filter_by(componentType='[IMU]').all()
     return componentList

@app.route('/avNetworkSwitches', methods=['GET'])
def getAvNetworkSwitches(): 
     componentList = Component.query.filter_by(componentType='[AV Network Switch]').all()
     return componentList

@app.route('/pcServers', methods=['GET'])
def getPCServers(): 
     componentList = Component.query.filter_by(componentType='[PC - Server]').all()
     return componentList

####################### APIs ########################
# Test Route
@app.route('/test', methods=['GET'])
def test():
    return {'message': 'Test route works!'}


####################### VIEWS / PAGE ROUTES ########################
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))
 
@app.route("/")
def home():
    return render_template("login.html")

@app.route('/edv')
def edv():
    return render_template('EDV.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')


####################### FILE UPLOADS ########################
# When a user submits the file upload form, the file is saved to the uploads/ 
# directory on the server. The user is then redirected to the /uploads/<filename> route,
# which serves the uploaded file.
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory('uploads', filename)

if __name__ == '__main__':
    app.run(debug = True)