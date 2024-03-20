import models.powerSupplyObject as PSO 
import models.batteryObject as BTO
import models.networkSwitchObject as NSO
import models.pcServerObject as PCO
import models.pduObject as PDU 
import models.flightCompObject as FCO
import models.powerControlObject as PWRCO
import models.IMUObject as IMO
import models.controllerObject as CO
import models.tvcController as TVC
import models.GPSObject as GPS
import models.AVNetworkSwitchObject as AV
import models.OrdnanceObject as ORD
import models.DAQPPCObject as DAQPPC
import models.DAQDigitalObject as DAQD
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

