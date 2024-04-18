# app.py
from flask import Flask, render_template, request, redirect, url_for, flash, make_response, jsonify, send_from_directory, send_file
from flask_sqlalchemy import SQLAlchemy
from os import environ
from flask_wtf.csrf import CSRFProtect
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt
from docx import Document
import os



####################### FLASK APP CONFIGURATION ########################
app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5432/postgres"
app.config['SECRET_KEY'] = 'your_secret_key_here'  # Set the SECRET_KEY configuration option

app.app_context()
db = SQLAlchemy(app)


###################### Import the TID Models ########################
from models import User, Projects, ChargeMode, PowerBusConfig, ExternalMode, Devices, GSENetwork, PathsLoads, PowerSupply, PowerSupplyAssign, PowerSupplySummary, TelemetryNetwork, VehicleBattery, VehicleNetwork, UEIDaq, BatteryAddresses, BatteryDefault, TIDTables, Component

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

def find_xml_file(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == 'data.xml':
                return os.path.join(root, file)
    return None


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

####################### TID Tables ########################
# Get battery Addresses for a specific project
@app.route('/battery_addresses/<int:project_id>', methods=['GET'])
def get_battery_addresses(project_id):
    battery_addresses = BatteryAddresses.query.filter_by(projectID=project_id).all()
    return jsonify([battery_addresses.json() for battery_addresses in battery_addresses])

# Save Changes to Battery Addresses
@app.route('/battery_addresses', methods=['POST'])
def save_battery_addresses():
    data = request.get_json()
    for battery_address in data:
        battery = BatteryAddresses.query.get(battery_address['id'])
        battery.battery = battery_address['battery']
        battery.rs485_address = battery_address['rs485_address']
        db.session.commit()
    return {'message': 'Battery Addresses saved successfully'}

# Get battery Default for a specific project
@app.route('/battery_default/<int:project_id>', methods=['GET'])
def get_battery_default(project_id):
    battery_default = BatteryDefault.query.filter_by(projectID=project_id).all()
    return jsonify([battery_default.json() for battery_default in battery_default])

# Get ChargeMode for a specific project
@app.route('/charge_mode/<int:project_id>', methods=['GET'])
def get_charge_mode(project_id):
    charge_mode = ChargeMode.query.filter_by(projectID=project_id).all()
    return jsonify([charge_mode.json() for charge_mode in charge_mode])

# Get Devices for a specific project
@app.route('/devices/<int:project_id>', methods=['GET'])
def get_devices(project_id):
    devices = Devices.query.filter_by(projectID=project_id).all()
    return jsonify([devices.json() for devices in devices])

# Get GSENetwork for a specific project
@app.route('/gse_network/<int:project_id>', methods=['GET'])
def get_gse_network(project_id):
    gse_network = GSENetwork.query.filter_by(projectID=project_id).all()
    return jsonify([gse_network.json() for gse_network in gse_network])

# Get PathsLoads for a specific project
@app.route('/paths_loads/<int:project_id>', methods=['GET'])
def get_paths_loads(project_id):
    paths_loads = PathsLoads.query.filter_by(projectID=project_id).all()
    return jsonify([paths_loads.json() for paths_loads in paths_loads])

# Get Power Bus Config for a specific project
@app.route('/power_bus_config/<int:project_id>', methods=['GET'])
def get_power_bus_config(project_id):
    power_bus_config = PowerBusConfig.query.filter_by(projectID=project_id).all()
    return jsonify([power_bus_config.json() for power_bus_config in power_bus_config])

# Get PowerSupply for a specific project
@app.route('/power_supply/<int:project_id>', methods=['GET'])
def get_power_supply(project_id):
    power_supply = PowerSupply.query.filter_by(projectID=project_id).all()
    return jsonify([power_supply.json() for power_supply in power_supply])

# Get Power Supply Summary for a specific project
@app.route('/power_supply_summary/<int:project_id>', methods=['GET'])
def get_power_supply_summary(project_id):
    power_supply_summary = PowerSupplySummary.query.filter_by(projectID=project_id).all()
    return jsonify([power_supply_summary.json() for power_supply_summary in power_supply_summary])

# Get Power Supply Assignments for a specific project
@app.route('/power_supply_assign/<int:project_id>', methods=['GET'])
def get_power_supply_assign(project_id):
    power_supply_assign = PowerSupplyAssign.query.filter_by(projectID=project_id).all()
    return jsonify([power_supply_assign.json() for power_supply_assign in power_supply_assign])

# Get Telemetry Network for a specific project
@app.route('/telemetry_network/<int:project_id>', methods=['GET'])
def get_telemetry_network(project_id):
    telemetry_network = TelemetryNetwork.query.filter_by(projectID=project_id).all()
    return jsonify([telemetry_network.json() for telemetry_network in telemetry_network])

# Get UEIDaq for a specific project
@app.route('/uei_daq/<int:project_id>', methods=['GET'])
def get_uei_daq(project_id):
    uei_daq = UEIDaq.query.filter_by(projectID=project_id).all()
    return jsonify([uei_daq.json() for uei_daq in uei_daq])

# Get Vehicle Battery for a specific project
@app.route('/vehicle_battery/<int:project_id>', methods=['GET'])
def get_vehicle_battery(project_id):
    vehicle_battery = VehicleBattery.query.filter_by(projectID=project_id).all()
    return jsonify([vehicle_battery.json() for vehicle_battery in vehicle_battery])

# Get Vehicle Network for a specific project
@app.route('/vehicle_network/<int:project_id>', methods=['GET'])
def get_vehicle_network(project_id):
    vehicle_network = VehicleNetwork.query.filter_by(projectID=project_id).all()
    return jsonify([vehicle_network.json() for vehicle_network in vehicle_network])

######################## End of TID Tables ########################
    
# Get all components for a specific project
@app.route('/components/<int:project_id>', methods=['GET'])
def get_components(project_id):
    components = Component.query.filter_by(projectId=project_id).all()
    return jsonify([component.json() for component in components])

from parse import parseXML

# Create a new project
@app.route('/project', methods=['POST'])
def create_project():
    data = request.get_json()
    project = Projects(project=data['name'])
    db.session.add(project)
    db.session.commit()
    newProjectID = project.id
    xml_file_path = find_xml_file(app.config['UPLOAD_FOLDER']) 
    if xml_file_path:
        output_file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'visioObjects4.txt')
        componentList = parseXML(xml_file_path, output_file_path, newProjectID)
        for i in componentList: 
            db.session.add(i)
            db.session.commit()
    return {'id': project.id}


####################### Export Project ########################
from exportProject import export_Project

@app.route('/export_project/<int:project_id>', methods=['GET'])
def export_project(project_id):
    doc_path = os.path.join(app.root_path, 'generated_document.docx')
    export_Project(project_id, doc_path)
    return send_file(doc_path, as_attachment=True)

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