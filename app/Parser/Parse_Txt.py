import powerSupplyObject as PSO 
import batteryObject as BTO
import networkSwitchObject as NSO
import pcServerObject as PCO
import pduObject as PDU 
import flightCompObject as FCO
import powerControlObject as PWRCO
import IMUObject as IMO
import controllerObject as CO
import tvcController as TVC
import GPSObject as GPS
import AVNetworkSwitchObject as AV
import OrdnanceObject as ORD
import DAQPPCObject as DAQPPC
import DAQDigitalObject as DAQD
def parsePower(file_path, checkName):
    if checkName == "[PS]":
        obj = PSO.PowerSupply
    elif checkName == "[Li-Ion Batt]":
        obj = BTO.Battery
    elif checkName == "[Network Switch]":
        obj = NSO.NetworkSwitch
    elif checkName == "[PC - Server]":
        obj = PCO.PCServer
    elif checkName == "[PDU]":
        obj = PDU.PDUObject 
    elif checkName == "[Flight Computer]": 
        obj = FCO.flightCompObject
    elif checkName == "[Power Control Device]":
        obj = PWRCO.powerControlObject
    elif checkName == "[IMU]":
        obj = IMO.IMUObject
    elif checkName == "[Controller]":
        obj = CO.Controller
    elif checkName == "[TVC Controller]":
        obj = TVC.TVCCtrl
    elif checkName == "[GPS]": 
        obj = GPS.GPSObject
    elif checkName == "[AV Network Switch]":
        obj = AV.AVNetworkSwitchObject
    elif checkName == "[Ordnance]":
        obj = ORD.OrdnanceObject
    elif checkName == "[DAQ-PPC]":
        obj = DAQPPC.DAQPPCObject
    elif checkName == "[DAQ-Digital]":
        obj = DAQD.DAQDIGITALObject
    else: 
        pass
    Dict = {}
    with open(file_path, 'r') as file:
        lines = file.readlines()

    parsed_data = []
    for i, line in enumerate(lines):
        if checkName in line:
            start_index = max(0, i - 2)
            end_index = min(len(lines), i + 3)
            parsed_data.append(lines[start_index:end_index])

    # Now, parsed_data contains the relevant lines for each [PS] occurrence
    for data in parsed_data:
        name_line = data[1].strip()  # assuming the first line is the Text line
        pn_line = data[3].strip()  # assuming the second line is the Unique ID line
        unique_id_line = data[4].strip()
        obj_type = obj(name_line, unique_id_line, pn_line)
        Dict[name_line] = obj_type
    
    return Dict

