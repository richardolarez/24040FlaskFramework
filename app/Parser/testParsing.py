# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 16:35:00 2024

@author: julia
"""

import Parse_Txt as pParse 


file_path = "visioObjects.txt"
class parseTXT():
    def __init__(self, file_path):
        pass 
    
        self.powerDict = pParse.parsePower(file_path, "[PS]")
        self.bt = pParse.parsePower(file_path, "[Li-Ion Batt]")
        self.network = pParse.parsePower(file_path, "[Network Switch]")
        self.pcServers = pParse.parsePower(file_path, "[PC - Server]")
        self.pdu = pParse.parsePower(file_path, "[PDU]")
        self.flightComps = pParse.parsePower(file_path, "[Flight Computer]")
        self.pwrCtrl = pParse.parsePower(file_path, "[Power Control Device]")
        self.imu = pParse.parsePower(file_path, "[IMU]")
        self.ctrl = pParse.parsePower(file_path, "[Controller]")
        self.tvc = pParse.parsePower(file_path, "[TVC Controller]")
        self.gps = pParse.parsePower(file_path, "[GPS]")
        self.av = pParse.parsePower(file_path, "[AV Network Switch]")
        self.ordnance = pParse.parsePower(file_path, "[Ordnance]")
        self.DAQPPC = pParse.parsePower(file_path, "[DAQ-PPC]")
        self.DAQD = pParse.parsePower(file_path, "[DAQ-Digital]")
    
def runParsingTest(): 
    parse = parseTXT(file_path)
    key = list(parse.powerDict.keys()) 
    if (key[0] == "POWER SUPPLY 1" and key[1] == "POWER SUPPLY 2" and key[2] == "POWER SUPPLY 3"):
        if parse.powerDict.get(key[0]).name == "POWER SUPPLY 1" and parse.powerDict.get(key[0]).PN == "(DLM60)":
            pass
        else: 
            print("Power Supply Parsing FAILED")
        if parse.powerDict.get(key[1]).name == "POWER SUPPLY 2" and parse.powerDict.get(key[1]).PN == "(DLM60)":
            pass 
        else: 
            print("Power Supply Parsing FAILED")
        if parse.powerDict.get(key[2]).name == "POWER SUPPLY 3" and parse.powerDict.get(key[2]).PN == "(DLM40)":
            pass 
        else: 
            print("Power Supply Parsing FAILED")
    else: 
        print("Power Supply Parsing FAILED")
        
    key = list(parse.bt.keys())
    if (key[0] == "AV Batt" and key[1] == "TLM Batt" and key[2] == "IMU Batt" and key[3] == "S2 Batt" and key[4] == "GPS Batt" and key[5] == "ORD Batt"):
        if parse.bt.get(key[0]).name == "AV Batt" and parse.bt.get(key[0]).PN == "(XXXX-YYYY)":
            pass
        else: 
            print("Battery Parsing FAILED")
        if parse.bt.get(key[1]).name == "TLM Batt" and parse.bt.get(key[1]).PN == "(XXXX-YYYY)":
            pass 
        else: 
            print("Battery Parsing FAILED")
        if parse.bt.get(key[2]).name == "IMU Batt" and parse.bt.get(key[2]).PN == "(XXXX-YYYY)":
            pass 
        else: 
            print("Battery Parsing FAILED")
        if parse.bt.get(key[3]).name == "S2 Batt" and parse.bt.get(key[3]).PN == "(XXXX-YYYY)":
             pass 
        else: 
             print("Battery Parsing FAILED")
        if parse.bt.get(key[4]).name == "GPS Batt" and parse.bt.get(key[4]).PN == "(XXXX-YYYY)":
             pass 
        else: 
             print("Battery Parsing FAILED")
        if parse.bt.get(key[5]).name == "ORD Batt" and parse.bt.get(key[5]).PN == "(XXXX-YYYY)":
             pass 
        else: 
             print("Battery Parsing FAILED")
    else: 
        print("Battery Parsing FAILED")
     
    key = list(parse.network.keys())
    if (key[0] == "GSE Net Switch"):
        if parse.network.get(key[0]).name == "GSE Net Switch" and parse.network.get(key[0]).PN == "(CiscoXXX)":
            pass
        else: 
            print("Network Parsing FAILED")
    else: 
        print("Network Parsing FAILED")
        
    key = list(parse.pcServers.keys())
    if (key[0] == "Server #"):
        if parse.pcServers.get(key[0]).name == "Server #" and parse.pcServers.get(key[0]).PN == "(Dell XXYY)":
            pass
        else: 
            print("PC Server Parsing FAILED")
    else: 
        print("PC Server Parsing FAILED")
        
    key = list(parse.pdu.keys())
    if (key[0] == "PDU 1"):
        if parse.pdu.get(key[0]).name == "PDU 1" and parse.pdu.get(key[0]).PN == "(EPDU)":
            pass
        else: 
            print("PDU Parsing FAILED")
    else: 
        print("PDU Parsing FAILED")
    
    key = list(parse.flightComps.keys())
    if (key[0] == "Avionics FC"):
        if parse.flightComps.get(key[0]).name == "Avionics FC" and parse.flightComps.get(key[0]).PN == "(XXXX-YYYY)":
            pass
        else: 
            print("Flight Computer Parsing FAILED")
    else: 
        print("Flight Computer Parsing FAILED")
        
    key = list(parse.pwrCtrl.keys())
    if (key[0] == "PCD0" and key[1] == "PCD1" and key[2] == "PCD2" and key[3] == "PCD3"):
        if parse.pwrCtrl.get(key[0]).name == "PCD0" and parse.pwrCtrl.get(key[0]).PN == "(XXXX-YYYY)":
            pass
        else: 
            print("Power Control Parsing FAILED")
        if parse.pwrCtrl.get(key[1]).name == "PCD1" and parse.pwrCtrl.get(key[1]).PN == "(XXXX-YYYY)":
            pass 
        else: 
            print("Power Control Parsing FAILED")
        if parse.pwrCtrl.get(key[2]).name == "PCD2" and parse.pwrCtrl.get(key[2]).PN == "(XXXX-YYYY)":
            pass 
        else: 
            print("Power Control Parsing FAILED")
        if parse.pwrCtrl.get(key[3]).name == "PCD3" and parse.pwrCtrl.get(key[3]).PN == "(XXXX-YYYY)":
            pass 
        else: 
            print("Power Control Parsing FAILED")
    else: 
        print("Power Control Parsing FAILED")
        
    key = list(parse.imu.keys())
    if (key[0] == "IMU"):
        if parse.imu.get(key[0]).name == "IMU" and parse.imu.get(key[0]).PN == "(XXXX-YYYY)":
            pass
        else: 
            print("IMU Parsing FAILED")
    else: 
        print("IMU Parsing FAILED")
    
    key = list(parse.ctrl.keys())
    if (key[0] == "Stage 2 Controller" and key[1] == "Telemetry Controller"):
        if parse.ctrl.get(key[0]).name == "Stage 2 Controller" and parse.ctrl.get(key[0]).PN == "(XXXX-YYYY)":
            pass
        else: 
            print("Controller Parsing FAILED")
        if parse.ctrl.get(key[1]).name == "Telemetry Controller" and parse.ctrl.get(key[1]).PN == "(XXXX-YYYY)":
            pass
        else: 
            print("Controller Parsing FAILED")
    else: 
        print("Controller Parsing FAILED")
        
    key = list(parse.tvc.keys())
    if (key[0] == "S2 TVC Controller" and key[1] == "S1 TVC Controller"):
        if parse.tvc.get(key[0]).name == "S2 TVC Controller" and parse.tvc.get(key[0]).PN == "(XXXX-YYYY)":
            pass
        else: 
            print("TVC Controller Parsing FAILED")
        if parse.tvc.get(key[1]).name == "S1 TVC Controller" and parse.tvc.get(key[1]).PN == "(XXXX-YYYY)":
            pass
        else: 
            print("TVC Controller Parsing FAILED")
    else: 
        print("TVC Controller Parsing FAILED")
    
    key = list(parse.gps.keys())
    if (key[0] == "GPS"):
        if parse.gps.get(key[0]).name == "GPS" and parse.gps.get(key[0]).PN == "(XXXX-YYYY)":
            pass
        else: 
            print("GPS Parsing FAILED")
    else: 
        print("GPS Parsing FAILED")
        
    key = list(parse.av.keys())
    if (key[0] == "AV Eth Switch"):
        if parse.av.get(key[0]).name == "AV Eth Switch" and parse.av.get(key[0]).PN == "(XXXX-YYYY)":
            pass
        else: 
            print("AV Parsing FAILED")
    else: 
        print("AV Parsing FAILED")
    
    key = list(parse.ordnance.keys())
    if (key[0] == "Ordnance"):
        if parse.ordnance.get(key[0]).name == "Ordnance" and parse.ordnance.get(key[0]).PN == "(XXXX-YYYY)":
            pass
        else: 
            print("Ordnance Parsing FAILED")
    else: 
        print("Ordnance Parsing FAILED")
        
    key = list(parse.DAQPPC.keys())
    if (key[0] == "DAQ 1" and key[1] == "DAQ 2"):
        if parse.DAQPPC.get(key[0]).name == "DAQ 1" and parse.DAQPPC.get(key[0]).PN == "(DNA-PPC8)":
            pass
        else: 
            print("DAQ Parsing FAILED")
        if parse.DAQPPC.get(key[1]).name == "DAQ 2" and parse.DAQPPC.get(key[1]).PN == "(DNA-PPC8)":
            pass
        else: 
            print("DAQ Parsing FAILED")
    else: 
        print("DAQ Parsing Failed")
    
    key = list(parse.DAQD.keys())
    if (key[0] == "DAQ 1 Layer 1" and key[1] == "DAQ 1 Layer 2" and key[2] == "DAQ 2 Layer 1" and key[3] == "DAQ 2 Layer 3"):
        if parse.DAQD.get(key[0]).name == "DAQ 1 Layer 1" and parse.DAQD.get(key[0]).PN == "(DNA-DIO-404)":
            pass
        else: 
            print("DAQ Digital parsing FAILED")
        if parse.DAQD.get(key[1]).name == "DAQ 1 Layer 2" and parse.DAQD.get(key[1]).PN == "(DNA-DIO-404)":
            pass 
        else: 
            print("DAQ Digital Parsing FAILED")
        if parse.DAQD.get(key[2]).name == "DAQ 2 Layer 1" and parse.DAQD.get(key[2]).PN == "(DNA-DIO-406)":
            pass 
        else: 
            print("DAQ Digital Parsing FAILED")
        if parse.DAQD.get(key[3]).name == "DAQ 2 Layer 3" and parse.DAQD.get(key[3]).PN == "(DNA-DIO-406)":
            pass 
        else: 
            print("DAQ Digital Parsing FAILED")
    else: 
        print("DAQ Digital Parsing FAILED")
        
    print("Parsing Test Complete")
runParsingTest()