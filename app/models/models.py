# models.py
from app import db

########################################################## TID Table Models ##########################################################
class PowerSupply(db.Model):
    __tablename__ = "PowerSupply"
    id = db.Column(db.Integer, primary_key=True)
    battery_system = db.Column(db.String(255))
    voltage_setting = db.Column(db.Float)
    ovp = db.Column(db.Float)
    current_limit = db.Column(db.Float)
    red_green_limits = db.Column(db.String(255))

    def __init__(self, battery_system, voltage_setting, ovp, current_limit, red_green_limits):
        self.battery_system = battery_system
        self.voltage_setting = voltage_setting
        self.ovp = ovp
        self.current_limit = current_limit
        self.red_green_limits = red_green_limits


class UEIDaq(db.Model):
    __tablename__ = "UEIDaq"
    id = db.Column(db.Integer, primary_key=True)
    power_daq_layer = db.Column(db.String(255))
    bit = db.Column(db.String(255))
    pin = db.Column(db.String(255))
    signal = db.Column(db.String(255))
    initial = db.Column(db.String(255))

    def __init__(self, power_daq_layer, bit, pin, signal, initial):
        self.power_daq_layer = power_daq_layer
        self.bit = bit
        self.pin = pin
        self.signal = signal
        self.initial = initial

class TelemetryNetwork(db.Model):
    __tablename__ = "TelemetryNetwork"
    id = db.Column(db.Integer, primary_key=True)
    tlm_net_device = db.Column(db.String(255))
    ip_address = db.Column(db.String(255))
    sub_net_mask = db.Column(db.String(255))
    host_name = db.Column(db.String(255))

    def __init__(self, tlm_net_device, ip_address, sub_net_mask, host_name):
        self.tlm_net_device = tlm_net_device
        self.ip_address = ip_address
        self.sub_net_mask = sub_net_mask
        self.host_name = host_name

class PathsLoads(db.Model):
    __tablename__ = "PathsLoads"
    id = db.Column(db.Integer, primary_key=True)
    battery = db.Column(db.String(255))
    ptm_channel = db.Column(db.String(255))
    components = db.Column(db.String(255))
    current = db.Column(db.Float)
    range_ = db.Column(db.String(255))

    def __init__(self, battery, ptm_channel, components, current, range_):
        self.battery = battery
        self.ptm_channel = ptm_channel
        self.components = components
        self.current = current
        self.range_ = range_

class ChargeMode(db.Model):
    __tablename__ = "ChargeMode"
    id = db.Column(db.Integer, primary_key=True)
    battery = db.Column(db.String(255))
    voltage_setting = db.Column(db.Float)
    ovp = db.Column(db.Float)
    current_setting = db.Column(db.Float)
    current_limit = db.Column(db.Float)
    red_green_limits = db.Column(db.String(255))

    def __init__(self, battery, voltage_setting, ovp, current_setting, current_limit, red_green_limits):
        self.battery = battery
        self.voltage_setting = voltage_setting
        self.ovp = ovp
        self.current_setting = current_setting
        self.current_limit = current_limit
        self.red_green_limits = red_green_limits

class Devices(db.Model):
    __tablename__ = "Devices"
    id = db.Column(db.Integer, primary_key=True)
    device = db.Column(db.String(255))

    def __init__(self, device): 
        self.device = device

class PowerSupplySummary(db.Model):
    __tablename__ = "PowerSupplySummary"
    id = db.Column(db.Integer, primary_key=True)
    part_number = db.Column(db.String(255))
    voltage = db.Column(db.Float)
    current = db.Column(db.Float)
    power = db.Column(db.Float)

    def __init__(self, part_number, voltage, current, power):  
        self.part_number = part_number
        self.voltage = voltage
        self.current = current
        self.power = power

class GSENetwork(db.Model):
    __tablename__ = "GSENetwork"
    id = db.Column(db.Integer, primary_key=True)
    gse_net_device = db.Column(db.String(255))
    ip_address = db.Column(db.String(255))
    sub_net_mask = db.Column(db.String(255))
    host_name = db.Column(db.String(255))

    def __init__(self, gse_net_device, ip_address, sub_net_mask, host_name):
        self.gse_net_device = gse_net_device
        self.ip_address = ip_address
        self.sub_net_mask = sub_net_mask
        self.host_name = host_name

class VehicleNetwork(db.Model):
    __tablename__ = "VehicleNetwork"
    id = db.Column(db.Integer, primary_key=True)
    device = db.Column(db.String(255))
    ip_address = db.Column(db.String(255))
    sub_net_mask = db.Column(db.String(255))
    host_name = db.Column(db.String(255))

    def __init__(self, device, ip_address, sub_net_mask, host_name):
        self.device = device
        self.ip_address = ip_address
        self.sub_net_mask = sub_net_mask
        self.host_name = host_name

class VehicleBattery(db.Model):
    __tablename__ = "VehicleBattery"
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(255))
    capacity = db.Column(db.Float)
    pn = db.Column(db.String(255))
    description2 = db.Column(db.String(255))
    capacity2 = db.Column(db.Float)
    pn2 = db.Column(db.String(255))

    def __init__(self, description, capacity, pn, description2, capacity2, pn2):
        self.description = description
        self.capacity = capacity
        self.pn = pn
        self.description2 = description2
        self.capacity2 = capacity2
        self.pn2 = pn2

class BatteryAddresses(db.Model):
    __tablename__ = "BatteryAddresses"
    id = db.Column(db.Integer, primary_key=True)
    battery = db.Column(db.String(255))
    rs485_address = db.Column(db.String(255))

    def __init__(self, battery, rs485_address):
        self.battery = battery
        self.rs485_address = rs485_address
