import sys
import os
import xml.etree.ElementTree as xmlParser
import json
import pprint

if len(sys.argv) < 2:
	print("Incorrect number of arguments")
	print("Usage: xmldumpimport.py <input file> [> outputfile]")
	sys.exit()

currentTable = None
currentType = 0

currentStatement = ""

createLineNum = 0
createRowNum = 0

for event, elem in xmlParser.iterparse(sys.argv[1], events=("start", "end")):
	if event == "start":
		if elem.tag == "table_structure":
			currentTable = elem.attrib["name"]
			currentType = 1
			currentStatement += "DROP TABLE IF EXISTS " + currentTable + "; \n"
			currentStatement += "CREATE TABLE " + currentTable + " ("
		elif elem.tag == "table_data":
			currentType = 2
			currentStatement += "INSERT INTO " + currentTable + " VALUES "
		elif elem.tag == "row":
			if createRowNum > 0:
				currentStatement += ",\n("
			else:
				currentStatement += "("
			createRowNum += 1
		elif elem.tag =="field":
			if currentType == 1:
				if createLineNum > 0:
					currentStatement += ",\n" + elem.attrib["Field"] + " " + elem.attrib["Type"]
				else:
					currentStatement += elem.attrib["Field"] + " " + elem.attrib["Type"]
				createLineNum+=1
	if event == "end":
		if elem.tag == "table_structure":
			currentStatement += ");\n"
			createLineNum = 0
			print(currentStatement)
			currentStatement = ""
		if elem.tag == "row":
			if currentType == 2:
				currentStatement += ")"
				createLineNum = 0
		if elem.tag == "table_data":
			currentStatement += ";\n"
			print(currentStatement)
			createRowNum = 0
			currentStatement = ""
		if elem.tag =="field":
			if currentType == 2:
                                #text = elem.text
                                #if text == None:
                                    #text = xmlParser.tostring(elem)
                                #print "TEXT IS: " + (elem.text or "no") + "\n"
                                #print "TEXT IS (TAIL): " + (elem.tail or "no") + "\n"
				if createLineNum > 0:
					currentStatement += ",\n" + json.dumps(elem.text or "")
				else:
					currentStatement += json.dumps(elem.text or "")
				createLineNum+=1
                elem.clear()
