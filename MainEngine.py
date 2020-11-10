# Code Written by KrypticCoconut
# Refer to wiki for usage
# drink milk and have fun torturing peeople 

import configparser
import os
import subprocess
import sys
from IfElseFuncs import *
import ast
from datetime import datetime
import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify
Notify.init("CM-Report-Engine")





def Main(section, Function):
    possibles = globals().copy()
    possibles.update(locals())
    method = possibles.get(Function)
    if(not method):
        print("Non defined function, exiting")
        sys.exit()
    else:
        return method(section,config.options(section))

def CheckStuff():
    try:
        TrueIf = str(config[section]["points"])
    except KeyError:
        print("points does not exist in section " + section + " exiting...")
        sys.exit()
    try:
        TrueIf = str(config[section]["description"])
    except KeyError:
        print("description does not exist in section " + section + " exiting...")
        sys.exit()
    try:
        TrueIf = str(config[section]["Function"])
    except KeyError:
        print("Function does not exist in section " + section + " exiting...")
        sys.exit()



file = 'config.ini'
config = configparser.RawConfigParser()
config.read(file)

vulnstotal = 0
vulnsfixed = 0
totalpoints = 0
currentpoints = 0
positive = []
negetive = []
positivestr = ""
negetivestr = ""
extrastr = ""
extra = []
done = ""
gained = 0
lost = 0

Sections = config.sections()
for section in Sections:
    CheckStuff()
    if(float(config[section]["points"]) > 0):
        vulnstotal += 1
        totalpoints += float(config[section]["points"])
    result = Main(section, str(config[section]["Function"]))
    print(result)
    #string = str(config[section]["result"].encode('utf-8').decode('unicode_escape'))
    #print(ast.literal_eval(string))
    if(result == True):
        if(float(config[section]["points"]) > 0):
            positive  += [section + ": " + str(config[section]["description"]) + " " + str(config[section]["points"] + "pts")]
            gained += float(config[section]["points"])
            vulnsfixed += 1
            currentpoints +=  float(config[section]["points"])
            Notify.Notification.new("Gained " + str(config[section]["points"]) + " pts").show()

        
        if(float(config[section]["points"]) < 0):
        
            negetive += [section + ": " + str(config[section]["description"]) + " " + str(config[section]["points"] + "pts")]
            lost += float(config[section]["points"])
            currentpoints +=  float(config[section]["points"])
            Notify.Notification.new("Lost " + str(config[section]["points"]) + " pts").show()
        
        if(float(config[section]["points"]) == 0):
        
            extra += [section + ": " + str(config[section]["description"]) + " " + str(config[section]["points"] + "pts")]
            Notify.Notification.new("Completed extra question").show()
        


for positives in positive:
    positivestr += "<p> [+]   "+str(positives)+"</p>\n"
    print(positivestr)

for negetives in negetive:
    negetivestr += "<p> [+]   "+str(negetives)+"</p>\n"
    print(negetivestr)

for extras in extra:
    extrastr += "<p> [+]   "+str(extras)+"</p>\n"

index = open('index.html','w')
indexfile = """
<html>
    <style>
        p {
        text-indent: 2.0em;
        }
    </style>
    <head>
        <title>Scoring Engine Result</title>
    </head>
    <body>
        <br>
        <h1 style="text-align:center";>Scoring Engine Report</h1>
        <h3 style="text-align:center";>Report Last Checked at: """ + datetime.now().strftime("%H:%M:%S") + """</h3>
        <br>
        <br>
        <p><strong>Total Vulns fixed: </strong>""" + str(vulnsfixed)+ "/" + str(vulnstotal) +"""</p>
        <p><strong>Points Right now: </strong>"""  + str(currentpoints)+ "/" + str(totalpoints) + """
        <br>
        <br>
        <hr>
        <br>
        <p><strong>Points Gained: </strong>""" + str(gained) + """</p>
        """ + positivestr + """
        <br>
                <p><strong>Points lost: </strong>""" + str(lost) + """</p>
        """ + negetivestr + """
        <br>
                <p><strong>Extras: </strong> </p>
        """ + extrastr + """
        <br>
</html>
"""
index.write(indexfile)

Notify.uninit()
