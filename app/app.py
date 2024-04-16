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
# app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/postgres"
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Set the SECRET_KEY configuration option

app.app_context()
db = SQLAlchemy(app)


###################### Import the TID Models ########################
from models import User, Projects, TIDTableRelationships, ChargeMode, Devices, GSENetwork, PathsLoads, PowerSupply, PowerSupplySummary, TelemetryNetwork, VehicleBattery, VehicleNetwork, UEIDaq, BatteryAddresses, TIDTables, Component

############### TID Tables ################
tableNames = ['ChargeMode', 'Devices', 'GSENetwork', 'PathsLoads', 'PowerSupply', 'PowerSupplySummary', 'TelemetryNetwork', 'VehicleBattery', 'VehicleNetwork', 'UEIDaq', 'BatteryAddresses']


####################### CREATE TABLES ########################
class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(255))
    file_content = db.Column(db.LargeBinary)
    
with app.app_context(): 
    db.create_all()

####### Generate Test Data #######
# Only run this once to generate test data or after resetting the database
# from db_init import db_init
# with app.app_context():
#     db_init()



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
			return redirect(url_for("home_page"))
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
        return 'File uploaded successfully'

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

####################### APIs ########################
# Test Route
@app.route('/test', methods=['GET'])
def test():
    return {'message': 'Test route works!'}

# Get all projects
@app.route('/projects', methods=['GET'])
def get_projects():
    projects = Projects.query.all()
    return jsonify([project.json() for project in projects])

# Get all TID Tables for a specific project
@app.route('/tid_tables/<int:project_id>', methods=['GET'])
def get_tid_tables(project_id):

# tableNames = ['ChargeMode', 'Devices', 'GSENetwork', 'PathsLoads', 'PowerSupply', 'PowerSupplySummary', 'TelemetryNetwork', 'VehicleBattery', 'VehicleNetwork', 'UEIDaq', 'BatteryAddresses']

    tid_tables = {}
    tid_tables['ChargeMode'] = ChargeMode.query.filter_by(projectID=project_id).all()
    tid_tables['ChargeMode'] = [charge_mode.json() for charge_mode in tid_tables['ChargeMode']]
    tid_tables['Devices'] = Devices.query.filter_by(projectID=project_id).all()
    tid_tables['Devices'] = [device.json() for device in tid_tables['Devices']]
    tid_tables['GSENetwork'] = GSENetwork.query.filter_by(projectID=project_id).all()
    tid_tables['GSENetwork'] = [gse_network.json() for gse_network in tid_tables['GSENetwork']]
    tid_tables['PathsLoads'] = PathsLoads.query.filter_by(projectID=project_id).all()
    tid_tables['PathsLoads'] = [paths_loads.json() for paths_loads in tid_tables['PathsLoads']]
    tid_tables['PowerSupply'] = PowerSupply.query.filter_by(projectID=project_id).all()
    tid_tables['PowerSupply'] = [power_supply.json() for power_supply in tid_tables['PowerSupply']]
    tid_tables['PowerSupplySummary'] = PowerSupplySummary.query.filter_by(projectID=project_id).all()
    tid_tables['PowerSupplySummary'] = [power_supply_summary.json() for power_supply_summary in tid_tables['PowerSupplySummary']]
    tid_tables['TelemetryNetwork'] = TelemetryNetwork.query.filter_by(projectID=project_id).all()
    tid_tables['TelemetryNetwork'] = [telemetry_network.json() for telemetry_network in tid_tables['TelemetryNetwork']]
    tid_tables['VehicleBattery'] = VehicleBattery.query.filter_by(projectID=project_id).all()
    tid_tables['VehicleBattery'] = [vehicle_battery.json() for vehicle_battery in tid_tables['VehicleBattery']]
    tid_tables['VehicleNetwork'] = VehicleNetwork.query.filter_by(projectID=project_id).all()
    tid_tables['VehicleNetwork'] = [vehicle_network.json() for vehicle_network in tid_tables['VehicleNetwork']]
    tid_tables['UEIDaq'] = UEIDaq.query.filter_by(projectID=project_id).all()
    tid_tables['UEIDaq'] = [uei_daq.json() for uei_daq in tid_tables['UEIDaq']]
    tid_tables['BatteryAddresses'] = BatteryAddresses.query.filter_by(projectID=project_id).all()
    tid_tables['BatteryAddresses'] = [battery_addresses.json() for battery_addresses in tid_tables['BatteryAddresses']]
    return jsonify(tid_tables)

# Get ChargeMode for a specific project
@app.route('/charge_mode/<int:project_id>', methods=['GET'])
def get_charge_mode(project_id):
    charge_mode = ChargeMode.query.filter_by(projectID=project_id).all()
    return jsonify([charge_mode.json() for charge_mode in charge_mode])
    
# Get all components for a specific project
@app.route('/components/<int:project_id>', methods=['GET'])
def get_components(project_id):
    components = Component.query.filter_by(projectId=project_id).all()
    return jsonify([component.json() for component in components])

# Create a new project
@app.route('/project', methods=['POST'])
def create_project():
    data = request.get_json()
    project = Projects(project=data['name'])
    db.session.add(project)
    db.session.commit()
    newProjectID = project.id
    return {'id': project.id}


####################### Export Project ########################
from exportProject import export_Project

@app.route('/export_project/<int:project_id>', methods=['GET'])
def export_project(project_id):
    project = export_Project(project_id)
    response = make_response(jsonify(project))
    response.headers["Content-Disposition"] = f"attachment; filename=project_{project_id}.json"
    response.headers["Content-Type"] = "application/json"
    return response

####################### VIEWS / PAGE ROUTES ########################
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("login"))
 
@app.route("/")
def home():
    return redirect(url_for("login"))

@app.route('/edv')
def edv():
    return render_template('EDV.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')

@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/project')
def projects():
    return render_template('newProject.html')

####################### FILE UPLOADS ########################
# When a user submits the file upload form, the file is saved to the uploads/ 
# directory on the server. The user is then redirected to the /uploads/<filename> route,
# which serves the uploaded file.
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory('uploads', filename)


if __name__ == '__main__':
    app.run(debug = True)