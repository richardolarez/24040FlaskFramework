from app import db 

class PowerSupply(db.Model):
    __tablename__ = "PowerSupplyObject"
    powerSupplyId = db.Column(db.String(255), primary_key=True)
    projectId = db.Column(db.Integer)
    name = db.Column(db.String(255))
    partNumber = db.Column(db.String(255))

    def json(self):
        return {'id': self.powerSupplyId, 'name': self.name, 'PN': self.partNumber}

    def __init__(self, name, ID, partNumber):
        self.name = name
        self.powerSupplyId = ID 
        self.partNumber = partNumber
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