from app import db

class PowerSupply(db.Model):
    __tablename__ = "PowerSupply"
    powerSupplyId = db.Column(db.Integer, primary_key=True)
    projectId = db.Column(db.Integer)
    name = db.Column(db.String(255))
    PN = db.Column(db.String(255))

    # # Paths/Loads Table
    # pl_PCDChannels = db.Column(db.String(255))
    # pl_Battery = db.Column(db.String(255))
    # pl_Components = db.Column(db.String(255))
    # pl_current = db.Column(db.Float)
    # pl_Range = db.Column(db.String(255))
    # pl_currentTotals = db.Column(db.float)
    # pl_rangeTotals = db.Column(db.String(255))

    # # External Power Mode Voltage/Current Limits
    # ext_battery = db.Column(db.String(255))
    # ext_voltageSetting = db.Column(db.Float)
    # ext_OVP = db.Column(db.Float)
    # ext_currentLimit = db.Column(db.Float)
    # ext_rgVoltageLimit = db.Column(db.String(255))
    # ext_rgCurrentLimit = db.Column(db.String(255))

    # # Charging Mode Voltage/Current Limits
    # ch_battery = db.Column(db.String(255))
    # ch_voltageSetting = db.Column(db.Float)
    # ch_OVP = db.Column(db.Float)
    # ch_currentSetting = db.Column(db.Float)
    # ch_currentLimit = db.Column(db.Float)
    # ch_rgLimitsVoltage = db.Column(db.String(255))
    # ch_rgLimitsCurrent = db.Column(db.String(255))


    # # Power Supply 5 Voltage/Current/Limits
    # ps5_system = db.Column(db.String(255))
    # ps5_voltageSetting = db.Column(db.Float)
    # ps5_ovp = db.Column(db.Float)
    # ps5_currentSetting = db.Column(db.Float)
    # ps5_currentLimit = db.Column(db.Float)
    # ps5_rgLimitsVoltage = db.Column(db.String(255))
    # ps5_rgLimitsCurrent = db.Column(db.String(255))

    # # GSE NET IP Addresses
    # gse_ipAddress = db.Column(db.String(255))
    # gse_subnetMask = db.Column(db.String(255))
    # gse_hostName = db.Column(db.String(255))

    # # Power Supply Assignments
    # psAssign_Battery = db.Column(db.String(255))
    # psAssign_Devices = db.Column(db.String(255))
    # psAssign_extpwr = db.Column(db.String(255))
    # psAssign_battchg = db.Column(db.String(255))
    # psAssign_control = db.Column(db.String(255))
    # psAssign_monitor = db.Column(db.String(255))

    # # Power Bust Configuration Details 
    # psBus_Battery = db.Column(db.String(255))
    # psBus_Component = db.Column(db.String(255))
    # psBus_extpwr = db.Column(db.String(255))
    # psBus_intpwr = db.Column(db.String(255))
    # psBus_busVLow = db.Column(db.Float)


    
  
    def json(self):
        return {'id': self.id, 'name': self.name, 'PN': self.PN}


    def __init__(self, name, ID, PN):
        self.name = name
        self.powerSupplyId = ID 
        self.PN = PN