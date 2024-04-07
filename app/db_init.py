from app import db
from models import Projects, TIDTableRelationships, ChargeMode, Devices, GSENetwork, PathsLoads, PowerSupply, PowerSupplySummary, TelemetryNetwork, VehicleBattery, VehicleNetwork, UEIDaq, BatteryAddresses, TIDTables, Component


def db_init():
    # Create Projects
    testProject1 = Projects(project="Test Project 1")
    testProject2 = Projects(project="Test Project 2")
    testProject3 = Projects(project="Test Project 3")
    db.session.add(testProject1)
    db.session.add(testProject2)
    db.session.add(testProject3)

    # Create Component Table for project 1
    testComponent1 = Component(componentName='TestPS1', componentId='1', partNumber='XYZ123', componentType='Power Supply', projectId=1)
    testComponent2 = Component(componentName='TestBattery1', componentId='2', partNumber='ABC123', componentType='Battery', projectId=1)
    testComponent3 = Component(componentName='TestDevice1', componentId='3', partNumber='DEF123', componentType='Device', projectId=1)
    db.session.add(testComponent1)
    db.session.add(testComponent2)
    db.session.add(testComponent3)

    # Create Component Table for project 2
    testComponent4 = Component(componentName='TestPS2', componentId='4', partNumber='XYZ123', componentType='Power Supply', projectId=2)
    testComponent5 = Component(componentName='TestBattery2', componentId='5', partNumber='ABC123', componentType='Battery', projectId=2)
    testComponent6 = Component(componentName='TestDevice2', componentId='6', partNumber='DEF123', componentType='Device', projectId=2)
    db.session.add(testComponent4)
    db.session.add(testComponent5)
    db.session.add(testComponent6)

    # Create Component Table for project 3
    testComponent7 = Component(componentName='TestPS3', componentId='7', partNumber='XYZ123', componentType='Power Supply', projectId=3)
    testComponent8 = Component(componentName='TestBattery3', componentId='8', partNumber='ABC123', componentType='Battery', projectId=3)
    testComponent9 = Component(componentName='TestDevice3', componentId='9', partNumber='DEF123', componentType='Device', projectId=3)
    db.session.add(testComponent7)
    db.session.add(testComponent8)
    db.session.add(testComponent9)
  
    # Commit the session
    db.session.commit()

if __name__ == "__main__":
    db_init()
    print("Database Initialized")