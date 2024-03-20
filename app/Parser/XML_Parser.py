# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 16:56:34 2024

@author: julia
"""

import xml.etree.ElementTree as ET

# Load the XML file
tree = ET.parse('data.xml')
root = tree.getroot()

# Iterate through the shapes
with open('visioObjects.txt', 'w') as f:
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
            f.write(f"Text: {text}\n")
        f.write(f"Unique ID: {unique_id}\n")
        f.write(f"Shape ID: {shape_id}\n")
        f.write(f"Name: {name}\n")
        f.write(f"NameU: {name_u}\n")
        if pin_x is not None and pin_y is not None:
            f.write(f"PinX: {pin_x} {pin_x_unit}\n")
            f.write(f"PinY: {pin_y} {pin_y_unit}\n")
        f.write(f"Children: {children}\n")
        f.write("\n")