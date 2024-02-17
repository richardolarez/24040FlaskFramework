# app.py
from flask import Flask, render_template, request, redirect, url_for 
from flask_sqlalchemy import SQLAlchemy
from os import environ

####################### FLASK APP CONFIGURATION ########################
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DB_URL')
app.app_context()
db = SQLAlchemy(app)

###################### Import the TID Models ########################
from models.TIDTables import ChargeMode, Devices, GSENetwork, PathsLoads, PowerSupply, PowerSupplySummary, TelemetryNetwork, VehicleBattery, VehicleNetwork, UEIDaq, BatteryAddresses

####################### CREATE TABLES ########################
with app.app_context(): 
    db.create_all()

####################### ROUTES ########################
# Test Route
@app.route('/test', methods=['GET'])
def test():
    return {'message': 'Test route works!'}

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/edv')
def edv():
    return render_template('EDV.html')

@app.route('/menu')
def menu():
    return render_template('menu.html')



if __name__ == '__main__':
    app.run()