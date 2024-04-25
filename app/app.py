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
from io import BytesIO
from flask_migrate import Migrate



####################### FLASK APP CONFIGURATION ########################
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')
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
    migrate = Migrate(app, db)

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


@app.route('/upload/<int:project_id>', methods=['POST'])
def upload_file(project_id):
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        if not os.path.exists(UPLOAD_FOLDER + '/' + str(project_id)):
            os.makedirs(UPLOAD_FOLDER + '/' + str(project_id))
        app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER + '/' + str(project_id)
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        decompress_file(filename)
        save_zip_to_db(filename)
        newProjectID = project_id
        xml_file_path = find_xml_file(app.config['UPLOAD_FOLDER']) 
        if xml_file_path:
            output_file_path = os.path.join(app.config['UPLOAD_FOLDER'], 'output.txt')
            componentList = parseXML(xml_file_path, output_file_path, newProjectID)
            for i in componentList: 
                db.session.add(i)
                db.session.commit()
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

from parse import parseXML

# Create a new project
@app.route('/project', methods=['POST'])
def create_project():
    data = request.get_json()
    project = Projects(project=data['name'])
    db.session.add(project)
    db.session.commit()
    return {'id': project.id}

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

# Get [Li-Ion Batt] components for a specific project
@app.route('/batteries/<int:project_id>', methods=['GET'])
def get_batteries(project_id):
    batteries = Component.query.filter_by(projectId=project_id, componentType='[Li-Ion Batt]').all()
    return jsonify([battery.json() for battery in batteries])

# Get [PS] components for a specific project
@app.route('/power_supplies/<int:project_id>', methods=['GET'])
def get_power_supplies(project_id):
    power_supplies = Component.query.filter_by(projectId=project_id, componentType='[PS]').all()
    return jsonify([power_supply.json() for power_supply in power_supplies])

# Get [Controller] components for a specific project
@app.route('/controllers/<int:project_id>', methods=['GET'])
def get_controllers(project_id):
    controllers = Component.query.filter_by(projectId=project_id, componentType='[Controller]').all()
    return jsonify([controller.json() for controller in controllers])

####################### TID Tables ########################
# Get battery Addresses for a specific project
@app.route('/battery_addresses/<int:project_id>', methods=['GET'])
def get_battery_addresses(project_id):
    battery_addresses = BatteryAddresses.query.filter_by(projectID=project_id).all()
    return jsonify([battery_addresses.json() for battery_addresses in battery_addresses])

# Post battery Addresses for a specific project
@app.route('/battery_addresses', methods=['POST'])
def post_battery_addresses():
    data = request.get_json()
    battery_addresses = BatteryAddresses(projectID=data['projectID'], battery=data['battery'], rs485_address=data['rs485_address'])
    db.session.add(battery_addresses)
    db.session.commit()
    return {'id': battery_addresses.id}


# Get battery Default for a specific project
@app.route('/battery_default/<int:project_id>', methods=['GET'])
def get_battery_default(project_id):
    battery_default = BatteryDefault.query.filter_by(projectID=project_id).all()
    return jsonify([battery_default.json() for battery_default in battery_default])

# Post battery Default for a specific project
@app.route('/battery_default', methods=['POST'])
def post_battery_default():
    data = request.get_json()
    battery_default = BatteryDefault(projectID=data['projectID'], battery=data['battery'], capacity=data['capacity'], discharge_current=data['discharge_current'])
    db.session.add(battery_default)
    db.session.commit()
    return {'id': battery_default.id}

# Get ChargeMode for a specific project
@app.route('/charge_mode/<int:project_id>', methods=['GET'])
def get_charge_mode(project_id):
    charge_mode = ChargeMode.query.filter_by(projectID=project_id).all()
    return jsonify([charge_mode.json() for charge_mode in charge_mode])

# Post ChargeMode for a specific project
@app.route('/charge_mode', methods=['POST'])
def post_charge_mode():
    data = request.get_json()
    charge_mode = ChargeMode(projectID=data['projectID'], power_supply=data['power_supply'], battery=data['battery'], voltage_setting=data['voltage_setting'], ovp=data['ovp'], current_setting=data['current_setting'], current_limit=data['current_limit'], red_green_voltage_limits=data['red_green_voltage_limits'], red_green_current_limits=data['red_green_current_limits'])
    db.session.add(charge_mode)
    db.session.commit()
    return {'id': charge_mode.id}

# Get Devices for a specific project
@app.route('/devices/<int:project_id>', methods=['GET'])
def get_devices(project_id):
    devices = Devices.query.filter_by(projectID=project_id).all()
    return jsonify([devices.json() for devices in devices])

# Post Devices for a specific project
@app.route('/devices', methods=['POST'])
def post_devices():
    data = request.get_json()
    devices = Devices(projectID=data['projectID'], device=data['device'], sampling_rate=data['sampling_rate'])
    db.session.add(devices)
    db.session.commit()
    return {'id': devices.id}

# Get External Mode for a specific project
@app.route('/external_mode/<int:project_id>', methods=['GET'])
def get_external_mode(project_id):
    external_mode = ExternalMode.query.filter_by(projectID=project_id).all()
    return jsonify([external_mode.json() for external_mode in external_mode])

# Post External Mode for a specific project
@app.route('/external_mode', methods=['POST'])
def post_external_mode():
    data = request.get_json()
    external_mode = ExternalMode(projectID=data['projectID'], power_supply=data['power_supply'], battery=data['battery'], voltage_setting=data['voltage_setting'], ovp=data['ovp'], current_setting=data['current_setting'], current_limit=data['current_limit'], red_green_voltage_limits=data['red_green_voltage_limits'], red_green_current_limits=data['red_green_current_limits'])
    db.session.add(external_mode)
    db.session.commit()
    return {'id': external_mode.id}

# Get GSENetwork for a specific project
@app.route('/gse_network/<int:project_id>', methods=['GET'])
def get_gse_network(project_id):
    gse_network = GSENetwork.query.filter_by(projectID=project_id).all()
    return jsonify([gse_network.json() for gse_network in gse_network])

# Post GSENetwork for a specific project
@app.route('/gse_network', methods=['POST'])
def post_gse_network():
    data = request.get_json()
    gse_network = GSENetwork(projectID=data['projectID'], gse_net_device=data['gse_net_device'], ip_address=data['ip_address'], sub_net_mask=data['sub_net_mask'], host_name=data['host_name'])
    db.session.add(gse_network)
    db.session.commit()
    return {'id': gse_network.id}

# Get PathsLoads for a specific project
@app.route('/paths_loads/<int:project_id>', methods=['GET'])
def get_paths_loads(project_id):
    paths_loads = PathsLoads.query.filter_by(projectID=project_id).all()
    return jsonify([paths_loads.json() for paths_loads in paths_loads])

# Post PathsLoads for a specific project
@app.route('/paths_loads', methods=['POST'])
def post_paths_loads():
    data = request.get_json()
    paths_loads = PathsLoads(projectID=data['projectID'], power_supply=data['power_supply'], battery=data['battery'], ptm_channel=data['ptm_channel'], components=data['components'], current=data['current'], range_=data['range_'])
    db.session.add(paths_loads)
    db.session.commit()
    return {'id': paths_loads.id}

# Get Power Bus Config for a specific project
@app.route('/power_bus_config/<int:project_id>', methods=['GET'])
def get_power_bus_config(project_id):
    power_bus_config = PowerBusConfig.query.filter_by(projectID=project_id).all()
    return jsonify([power_bus_config.json() for power_bus_config in power_bus_config])

# Post Power Bus Config for a specific project
@app.route('/power_bus_config', methods=['POST'])
def post_power_bus_config():
    data = request.get_json()
    power_bus_config = PowerBusConfig(projectID=data['projectID'], power_supply=data['power_supply'], battery=data['battery'], component=data['component'], ext_pwr=data['ext_pwr'], int_pwr=data['int_pwr'], bus_v_low=data['bus_v_low'], bus_v_high=data['bus_v_high'], bus_i_low=data['bus_i_low'], bus_i_high=data['bus_i_high'])
    db.session.add(power_bus_config)
    db.session.commit()
    return {'id': power_bus_config.id}

# Get PowerSupply for a specific project
@app.route('/power_supply/<int:project_id>', methods=['GET'])
def get_power_supply(project_id):
    power_supply = PowerSupply.query.filter_by(projectID=project_id).all()
    return jsonify([power_supply.json() for power_supply in power_supply])

# Post PowerSupply for a specific project
@app.route('/power_supply', methods=['POST'])
def post_power_supply():
    data = request.get_json()
    power_supply = PowerSupply(projectID=data['projectID'], power_supply=data['power_supply'], battery_system=data['battery_system'], voltage_setting=data['voltage_setting'], ovp=data['ovp'], current_limit=data['current_limit'], red_green_voltage_limits=data['red_green_voltage_limits'], red_green_current_limits=data['red_green_current_limits'])
    db.session.add(power_supply)
    db.session.commit()
    return {'id': power_supply.id}

# Get Power Supply Summary for a specific project
@app.route('/power_supply_summary/<int:project_id>', methods=['GET'])
def get_power_supply_summary(project_id):
    power_supply_summary = PowerSupplySummary.query.filter_by(projectID=project_id).all()
    return jsonify([power_supply_summary.json() for power_supply_summary in power_supply_summary])

# Post Power Supply Summary for a specific project
@app.route('/power_supply_summary', methods=['POST'])
def post_power_supply_summary():
    data = request.get_json()
    power_supply_summary = PowerSupplySummary(projectID=data['projectID'], part_number=data['part_number'], voltage=data['voltage'], current=data['current'], power=data['power'])
    db.session.add(power_supply_summary)
    db.session.commit()
    return {'id': power_supply_summary.id}

# Get Power Supply Assignments for a specific project
@app.route('/power_supply_assign/<int:project_id>', methods=['GET'])
def get_power_supply_assign(project_id):
    power_supply_assign = PowerSupplyAssign.query.filter_by(projectID=project_id).all()
    return jsonify([power_supply_assign.json() for power_supply_assign in power_supply_assign])

# Post Power Supply Assignments for a specific project
@app.route('/power_supply_assign', methods=['POST'])
def post_power_supply_assign():
    data = request.get_json()
    power_supply_assign = PowerSupplyAssign(projectID=data['projectID'], power_supply=data['power_supply'], battery=data['battery'], devices=data['devices'], ext_pwr=data['ext_pwr'], batt_chg=data['batt_chg'], control=data['control'], monitor=data['monitor'])
    db.session.add(power_supply_assign)
    db.session.commit()
    return {'id': power_supply_assign.id}

# Get Telemetry Network for a specific project
@app.route('/telemetry_network/<int:project_id>', methods=['GET'])
def get_telemetry_network(project_id):
    telemetry_network = TelemetryNetwork.query.filter_by(projectID=project_id).all()
    return jsonify([telemetry_network.json() for telemetry_network in telemetry_network])

# Post Telemetry Network for a specific project
@app.route('/telemetry_network', methods=['POST'])
def post_telemetry_network():
    data = request.get_json()
    telemetry_network = TelemetryNetwork(projectID=data['projectID'], tlm_net_device=data['tlm_net_device'], ip_address=data['ip_address'], sub_net_mask=data['sub_net_mask'], host_name=data['host_name'])
    db.session.add(telemetry_network)
    db.session.commit()
    return {'id': telemetry_network.id}

# Get UEIDaq for a specific project
@app.route('/uei_daq/<int:project_id>', methods=['GET'])
def get_uei_daq(project_id):
    uei_daq = UEIDaq.query.filter_by(projectID=project_id).all()
    return jsonify([uei_daq.json() for uei_daq in uei_daq])

# Post UEIDaq for a specific project
@app.route('/uei_daq', methods=['POST'])
def post_uei_daq():
    data = request.get_json()
    uei_daq = UEIDaq(projectID=data['projectID'], power_daq_layer=data['power_daq_layer'], bit=data['bit'], pin=data['pin'], signal=data['signal'], initial=data['initial'])
    db.session.add(uei_daq)
    db.session.commit()
    return {'id': uei_daq.id}

# Get Vehicle Battery for a specific project
@app.route('/vehicle_battery/<int:project_id>', methods=['GET'])
def get_vehicle_battery(project_id):
    vehicle_battery = VehicleBattery.query.filter_by(projectID=project_id).all()
    return jsonify([vehicle_battery.json() for vehicle_battery in vehicle_battery])

# Post Vehicle Battery for a specific project
@app.route('/vehicle_battery', methods=['POST'])
def post_vehicle_battery():
    data = request.get_json()
    vehicle_battery = VehicleBattery(projectID=data['projectID'], battery=data['battery'], psv=data['psv'], ueiv=data['ueiv'], batv=data['batv'], cell=data['cell'], temp=data['temp'], loadv=data['loadv'], loadi=data['loadi'])
    db.session.add(vehicle_battery)
    db.session.commit()
    return {'id': vehicle_battery.id}

# Get Vehicle Network for a specific project
@app.route('/vehicle_network/<int:project_id>', methods=['GET'])
def get_vehicle_network(project_id):
    vehicle_network = VehicleNetwork.query.filter_by(projectID=project_id).all()
    return jsonify([vehicle_network.json() for vehicle_network in vehicle_network])

# Post Vehicle Network for a specific project
@app.route('/vehicle_network', methods=['POST'])
def post_vehicle_network():
    data = request.get_json()
    vehicle_network = VehicleNetwork(projectID=data['projectID'], device=data['device'], ip_address=data['ip_address'], sub_net_mask=data['sub_net_mask'], host_name=data['host_name'])
    db.session.add(vehicle_network)
    db.session.commit()
    return {'id': vehicle_network.id}

######################## End of TID Tables ########################
    
# Get all components for a specific project
@app.route('/components/<int:project_id>', methods=['GET'])
def get_components(project_id):
    components = Component.query.filter_by(projectId=project_id).all()
    return jsonify([component.json() for component in components])




####################### Export Project ########################
from exportProject import export_Project
from flask import send_file

@app.route('/export_project/<int:project_id>', methods=['GET'])
def export_project(project_id):
    # Export the project and get the byte content of the document
    doc_content = export_Project(project_id)
    
    # Send the byte content of the document as a file attachment with specified filename
    return send_file(BytesIO(doc_content),
                     mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document',
                     as_attachment=True,
                     download_name='generated_document.docx')
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