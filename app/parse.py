import xml.etree.ElementTree as ET
from models import Component

def run_XMLParser(input_file, output_file):
    # Load the XML file
    tree = ET.parse(input_file)
    root = tree.getroot()

    # Iterate through the shapes
    with open(output_file, 'w') as f:
        for shape in root.findall(".//Shape"):
            shape_id = shape.get("ID")
            unique_id = shape.get("UniqueID")
            name = shape.get("Name")
            name_u = shape.get("NameU")

            # Extract text within the Text element if it exists
            text_element = shape.find(".//Text")
            if text_element is not None:
                text = text_element.text
            else:
                text = None

            # Extract X and Y coordinates from the XForm element
            x_form = shape.find(".//XForm")
            if x_form is not None:
                pin_x = x_form.find(".//PinX").text
                pin_y = x_form.find(".//PinY").text
                pin_x_unit = x_form.find(".//PinX").get("Unit")
                pin_y_unit = x_form.find(".//PinY").get("Unit")
            else:
                pin_x = None
                pin_y = None
                pin_x_unit = None
                pin_y_unit = None

            # Add child objects as attributes of parent objects
            children = []
            for child in shape.findall(".//Shape"):
                child_id = child.get("ID")
                children.append(child_id)
            shape.set("Children", str(children))

            # Print or process the extracted information as needed
            if text is not None:
                f.write(f"{text}\n")
            f.write(f"{unique_id}\n")
            f.write(f"Shape ID: {shape_id}\n")
            f.write(f"Name: {name}\n")
            f.write(f"NameU: {name_u}\n")
            if pin_x is not None and pin_y is not None:
                f.write(f"PinX: {pin_x} {pin_x_unit}\n")
                f.write(f"PinY: {pin_y} {pin_y_unit}\n")
            f.write(f"Children: {children}\n")
            f.write("\n")
            
def parseTXT(file_path, project_id):
    checkNameList = ["[AV Network Switch]", "[Li-Ion Batt]", "[Controller]", "[DAQ-Digital]", "[DAQ-PPC]", "[Flight Computer]", "[GPS]", "[IMU]", "[Network Switch]", "[Ordnance]", "[PC - Server]", "[PDU]", "[Power Control Device]", "[PS]", "[TVC Controller]"]
    list1 = []
    for i in range(len(checkNameList)): 
        component_type = checkNameList[i]
        with open(file_path, 'r') as file:
            lines = file.readlines()
        parsed_data = []
        for j, line in enumerate(lines):
            if checkNameList[i] in line:
                start_index = max(0, j - 2)
                end_index = min(len(lines), j + 3)
                parsed_data.append(lines[start_index:end_index])
        for data in parsed_data:
            name_line = data[1].strip()  
            pn_line = data[3].strip()  
            unique_id_line = data[4].strip()
            obj_type = Component(componentName = name_line, componentId = unique_id_line, projectId = project_id, partNumber = pn_line, componentType=component_type)
            list1.append(obj_type)
    return list1

#This function will call the xmlParser and generate the txt file
def parseXML(input_file, output_file, project_id):
     run_XMLParser(input_file, output_file) 
     outputList = parseTXT(output_file, project_id)
     return outputList