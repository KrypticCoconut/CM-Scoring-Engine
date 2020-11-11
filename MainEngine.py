# Code Written by KrypticCoconut
# Refer to wiki for usage
# drink milk and have fun torturing peeople 
import subprocess
import sys
import ast
from datetime import datetime
from playsound import playsound
import pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent.absolute()) + "/")
from IfElseFuncs import *

import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify
Notify.init("CM-Report-Engine")


pointsgainedmp3 = str(pathlib.Path(__file__).parent.absolute()) +"/sounds/PointsGained.mp3"
pointslostmp3 = str(pathlib.Path(__file__).parent.absolute()) +"/sounds/PointsLost.mp3"



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



file = str(pathlib.Path(__file__).parent.absolute()) +'/config.ini'
print(file)
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

gained = 0
lost = 0

DoneForNotifications = []
pointsnow1 = 0
sectionsansweredfile1 = open(str(pathlib.Path(__file__).parent.absolute()) + "/TmpData/answered.txt", "r")
sectionsanswered1 = sectionsansweredfile1.readlines()
sectionsanswered1 = list(map(str.strip, sectionsanswered1))

for sections1 in sectionsanswered1:
    pointsnow1 += float(config[sections1]["points"])
    print(config[sections1]["points"])


Sections = config.sections()
for section in Sections:
    print(str(config[section]["Function"]))
    CheckStuff()
    if(float(config[section]["points"]) > 0):
        vulnstotal += 1
        totalpoints += float(config[section]["points"])
    result = Main(section, str(config[section]["Function"]))
    #string = str(config[section]["result"].encode('utf-8').decode('unicode_escape'))
    #print(ast.literal_eval(string))
    if(result == True):
        if(section not in DoneForNotifications):
            DoneForNotifications += [section]

        if(float(config[section]["points"]) > 0):
            positive  += [section + ": " + str(config[section]["description"]) + " " + str(config[section]["points"] + "pts")]
            gained += float(config[section]["points"])
            vulnsfixed += 1
            currentpoints +=  float(config[section]["points"])
            #Notify.Notification.new("Gained " + str(config[section]["points"]) + " pts").show()
            #playsound(pointsgainedmp3)

        
        if(float(config[section]["points"]) < 0):   
            negetive += [section + ": " + str(config[section]["description"]) + " " + str(config[section]["points"] + "pts")]
            lost += float(config[section]["points"])
            currentpoints +=  float(config[section]["points"])
            #Notify.Notification.new("Lost " + str(config[section]["points"]) + " pts").show()
            #playsound(pointslostmp3)
    
        if(float(config[section]["points"]) == 0):
            extra += [section + ": " + str(config[section]["description"]) + " " + str(config[section]["points"] + "pts")]
            #Notify.Notification.new("Completed extra question").show()
            #playsound(pointsgainedmp3)
    else:
        if(section in DoneForNotifications):
            DoneForNotifications.remove(section)

file = open(str(pathlib.Path(__file__).parent.absolute()) + "/TmpData/answered.txt", "w")
for donefor in DoneForNotifications:
    file.write(donefor + "\n")

file.close()


pointsnow2 = 0
sectionsansweredfile2 = open(str(pathlib.Path(__file__).parent.absolute()) + "/TmpData/answered.txt", "r")
sectionsanswered2 = sectionsansweredfile2.readlines()
sectionsanswered2 = list(map(str.strip, sectionsanswered2))
print(sectionsanswered2)

for sections2 in sectionsanswered2:
    pointsnow2 += float(config[sections2]["points"])
    print(config[sections2]["points"])

pointsgainednotif = pointsnow2 - pointsnow1
print(pointsgainednotif)

if(pointsgainednotif > 0):
        Notify.Notification.new("Gained " + str(pointsgainednotif) + " pts").show()
        playsound(pointsgainedmp3)
elif(pointsgainednotif < 0):
        Notify.Notification.new("Lost " + str(pointsgainednotif) + " pts").show()
        playsound(pointsgainedmp3)


for positives in positive:
    positivestr += "<p> [+]   "+str(positives)+"</p>\n"

for negetives in negetive:
    negetivestr += "<p> [+]   "+str(negetives)+"</p>\n"

for extras in extra:
    extrastr += "<p> [+]   "+str(extras)+"</p>\n"

index = open(str(pathlib.Path(__file__).parent.absolute()) +'/index.html','w')
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