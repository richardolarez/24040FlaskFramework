from flask_sqlalchemy import SQLAlchemy
from flask import current_app

db = SQLAlchemy(current_app)

########################################################## TID Table Models ##########################################################
class PowerSupply(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    battery_system = db.Column(db.String(255))
    voltage_setting = db.Column(db.Float)
    ovp = db.Column(db.Float)
    current_limit = db.Column(db.Float)
    red_green_limits = db.Column(db.String(255))

class UEIDaq(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    power_daq_layer = db.Column(db.String(255))
    bit = db.Column(db.String(255))
    pin = db.Column(db.String(255))
    signal = db.Column(db.String(255))
    initial = db.Column(db.String(255))

class TelemetryNetwork(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tlm_net_device = db.Column(db.String(255))
    ip_address = db.Column(db.String(255))
    sub_net_mask = db.Column(db.String(255))
    host_name = db.Column(db.String(255))

class PathsLoads(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    battery = db.Column(db.String(255))
    ptm_channel = db.Column(db.String(255))
    components = db.Column(db.String(255))
    current = db.Column(db.Float)
    range_ = db.Column(db.String(255))

class ChargeMode(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    battery = db.Column(db.String(255))
    voltage_setting = db.Column(db.Float)
    ovp = db.Column(db.Float)
    current_setting = db.Column(db.Float)
    current_limit = db.Column(db.Float)
    red_green_limits = db.Column(db.String(255))

class Devices(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device = db.Column(db.String(255))

class PowerSupplySummary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    part_number = db.Column(db.String(255))
    voltage = db.Column(db.Float)
    current = db.Column(db.Float)
    power = db.Column(db.Float)

class GSENetwork(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gse_net_device = db.Column(db.String(255))
    ip_address = db.Column(db.String(255))
    sub_net_mask = db.Column(db.String(255))
    host_name = db.Column(db.String(255))

class VehicleNetwork(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    device = db.Column(db.String(255))
    ip_address = db.Column(db.String(255))
    sub_net_mask = db.Column(db.String(255))
    host_name = db.Column(db.String(255))

class VehicleBattery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255))
    capacity = db.Column(db.Float)
    pn = db.Column(db.String(255))
    description2 = db.Column(db.String(255))
    capacity2 = db.Column(db.Float)
    pn2 = db.Column(db.String(255))

class BatteryAddresses(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    battery = db.Column(db.String(255))
    rs485_address = db.Column(db.String(255))