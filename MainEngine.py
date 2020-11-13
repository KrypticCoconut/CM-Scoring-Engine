# Code Written by KrypticCoconut
# Refer to wiki for usage
# drink milk and have fun torturing peeople 
import logging
import subprocess
import sys
import ast
from datetime import datetime
import pathlib
import time
sys.path.insert(0, str(pathlib.Path(__file__).parent.absolute()) + "/")
from IfElseFuncs import *
import gi
import argparse

#from playsound import playsound   #Musicib

#gi.require_version('Notify', '0.7') #notification lib
#from gi.repository import Notify
#Notify.init("CM-Report-Engine")


pointsgainedmp3 = str(pathlib.Path(__file__).parent.absolute()) +"/sounds/PointsGained.mp3"
pointslostmp3 = str(pathlib.Path(__file__).parent.absolute()) +"/sounds/PointsLost.mp3"



def Main(section):
    Function = config[section]["Function"]    
    possibles = globals().copy()
    possibles.update(locals())
    method = possibles.get(Function)
    if(not method):
        logging.warning("Non defined function in section "+ section+",  exiting...")
        sys.exit()
    else:
        return method(section,config.options(section))

def CheckStuff(section):
    try:
        TrueIf = str(config[section]["points"])
    except KeyError:
        print("hi")
        logging.warning("points does not exist in section " + section + " exiting...")
        sys.exit()
    try:
        TrueIf = str(config[section]["description"])
    except KeyError:
        prlogging.warningint("description does not exist in section " + section + " exiting...")
        sys.exit()
    try:
        TrueIf = str(config[section]["Function"])
    except KeyError:
        logging.warning("Function does not exist in section " + section + " exiting...")
        sys.exit()

os.system("sudo rm -f " + str(pathlib.Path(__file__).parent.absolute())+'/TmpData/ScoringEngine.log 2>/dev/null || true')
logging.basicConfig(filename=str(pathlib.Path(__file__).parent.absolute())+'/TmpData/ScoringEngine.log',level=logging.INFO)

file = str(pathlib.Path(__file__).parent.absolute()) +'/config.ini'
config = configparser.RawConfigParser()
config.read(file)


totalpoints = 0
currentpoints = 0
vulnsfixed = 0
vulnstotal = 0

questionsdone = [] #questions done

positivestr = [] # desc of positive point qiestions
negetivestr = [] #desc of negetive point questions
extrastr = [] #description of extra questions

pointsgained = 0 #points gained
pointslost = 0#points lost

for section in config.sections():
    CheckStuff(section)
    result = Main(section)
    if(float(config[section]["points"]) > 0):
        vulnstotal += 1
    if(result == True):
            if(float(config[section]["points"]) > 0):
                positivestr  += [section + ": " + str(config[section]["description"]) + " " + str(config[section]["points"] + "pts")]
                vulnsfixed +=1
                pointsgained += float(config[section]["points"])
                currentpoints += float(config[section]["points"])
            if(float(config[section]["points"]) < 0):
                negetivestr  += [section + ": " + str(config[section]["description"]) + " " + str(config[section]["points"] + "pts")]
                pointslost += float(config[section]["points"])
                currentpoints += float(config[section]["points"])
            if(float(config[section]["points"]) == 0):
                extrastr  += [section + ": " + str(config[section]["description"]) + " " + str(config[section]["points"] + "pts")]
            questionsdone += [section]
    elif result != False:
        logging.warning(result)
        print(result)
        sys.exit()


    totalpoints += float(config[section]["points"])

if(not os.path.exists(str(pathlib.Path(__file__).parent.absolute()) + "/TmpData/answered.txt")):
    subprocess.check_output("touch " + str(pathlib.Path(__file__).parent.absolute()) + "/TmpData/answered.txt 2>/dev/null || true", shell=True)

file = open(str(pathlib.Path(__file__).parent.absolute()) + "/TmpData/answered.txt", "r")
previousanswered = list(map(str.strip,file.readlines()))
previouspoints = 0
file.close()

for previousanswer in previousanswered:
    if previousanswer in config.sections():
        previouspoints += float(config[previousanswer]["points"])

pointsincreasedby = currentpoints - previouspoints
if(pointsincreasedby > 0):
    pass
        #Notify.Notification.new("Gained " + str(pointsgainednotif) + " pts").show()
        #playsound(pointsgainedmp3)
elif(pointsincreasedby < 0):
    pass
        #Notify.Notification.new("Lost " + str(pointsgainednotif) + " pts").show()
        #playsound(pointsgainedmp3)
file = open(str(pathlib.Path(__file__).parent.absolute()) + "/TmpData/answered.txt", "w")
for done in questionsdone:
    file.write(done + "\n")


positiveindex = ""
negetiveindex = ""
extraindex = ""
for positives in positivestr:
    positiveindex += "<p> [+]   "+str(positives)+"</p>\n"

for negetives in negetivestr:
    negetiveindex += "<p> [+]   "+str(negetives)+"</p>\n"

for extras in extrastr:
    extraindex += "<p> [+]   "+str(extras)+"</p>\n"

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
        <p><strong>Points Gained: </strong>""" + str(pointsgained) + """</p>
        """ + positiveindex + """
        <br>
                <p><strong>Points lost: </strong>""" + str(pointslost) + """</p>
        """ + negetiveindex + """
        <br>
                <p><strong>Extras: </strong> </p>
        """ + extraindex + """
        <br>
</html>
"""
index.write(indexfile)

#Notify.uninit()

my_parser = argparse.ArgumentParser(description='Code Written by krypt')

my_parser.add_argument('--test', action='store_true', help='Specify if test run or not, so the program doesnt store the answered questions in a file')

args = my_parser.parse_args()

test = args.test
if(test):
    print("hi")
    subprocess.check_output("rm -rf " + str(pathlib.Path(__file__).parent.absolute()) + "/TmpData/answered.txt 2>/dev/null || true", shell=True)

