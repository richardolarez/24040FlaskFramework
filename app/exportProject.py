from app import db
from models import Projects, TIDTableRelationships, ChargeMode, Devices, GSENetwork, PathsLoads, PowerSupply, PowerSupplySummary, TelemetryNetwork, VehicleBattery, VehicleNetwork, UEIDaq, BatteryAddresses, TIDTables, Component


def export_Project(projectId):
    project = Projects.query.filter_by(id=projectId).first()
    project_json = project.json()
    project_json['TIDTables'] = []
    tid_tables = TIDTableRelationships.query.filter_by(projectId=projectId).all()
    for tid_table in tid_tables:
        tid_table_json = tid_table.json()
        tid_table_json['ChargeMode'] = ChargeMode.query.filter_by(id=tid_table.chargeModeId).first().json()
        tid_table_json['Devices'] = []
        devices = Devices.query.filter_by(tidTableId=tid_table.id).all()
        for device in devices:
            device_json = device.json()
            device_json['GSENetwork'] = GSENetwork.query.filter_by(id=device.gseNetworkId).first().json()
            device_json['PathsLoads'] = []
            paths_loads = PathsLoads.query.filter_by(deviceId=device.id).all()
            for path_load in paths_loads:
                path_load_json = path_load.json()
                path_load_json['PowerSupply'] = PowerSupply.query.filter_by(id=path_load.powerSupplyId).first().json()
                path_load_json['PowerSupplySummary'] = PowerSupplySummary.query.filter_by(id=path_load.powerSupplySummaryId).first().json()
                path_load_json['TelemetryNetwork'] = TelemetryNetwork.query.filter_by(id=path_load.telemetryNetworkId).first().json()
                path_load_json['VehicleBattery'] = VehicleBattery.query.filter_by(id=path_load.vehicleBatteryId).first().json()
                path_load_json['VehicleNetwork'] = VehicleNetwork.query.filter_by(id=path_load.vehicleNetworkId).first().json()
                path_load_json['UEIDaq'] = UEIDaq.query.filter_by(id=path_load.ueiDaqId).first().json()
                path_load_json['BatteryAddresses'] = []
                battery_addresses = BatteryAddresses.query.filter_by(pathsLoadsId=path_load.id).all()
                for battery_address in battery_addresses:
                    path_load_json['BatteryAddresses'].append(battery_address.json())
                device_json['PathsLoads'].append(path_load_json)
            tid_table_json['Devices'].append(device_json)
        project_json['TIDTables'].append(tid_table_json)
    return project_json