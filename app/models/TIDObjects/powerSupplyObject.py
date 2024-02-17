# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 17:47:14 2023

@author: julia
"""

class PowerSupply:
    def __init__(self, name, ID, PN):
        self.name = name
        self.ID = ID 
        self.PN = PN
        #PS Summary 
        self.volt = None
        self.currentA = None
        self.powerW = None 
        
        #External Mode
        self.ext_battery = None
        self.ext_voltageSetting = None 
        self.ext_OVP = None
        self.ext_currentLimit = None 
        self.ext_limitsVoltage = None
        self.ext_limitsCurrent = None 
        
        #Charging Mode
        self.ch_battery = None 
        self.ch_voltageSetting = None
        self.ch_OVP = None
        self.ch_currentLimit = None 
        self.ch_limitsVoltage = None 
        self.ch_limitsCurrent = None 
        
        #Paths/Loads Table 
        self.pl_PTMChannels = None
        self.pl_Battery = None
        self.pl_Components = None
        self.currentTotals = None