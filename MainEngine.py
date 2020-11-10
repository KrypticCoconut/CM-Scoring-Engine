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





def parsecommands(command):
    return str(command).split(",")

def ClassifyType(section):
    try:
        Type = str(config[section]["Type"])
    except KeyError:
        print("Type does not exist in section " + section + " exiting...")
        sys.exit()

    if(Type == "Single"):
        if(len(parsecommands(str(config[section]["commands"]))) > 1 ):
            print("more than one command on certain section Exiting....")
            sys.exit()
        else:
            return "Single"

    elif(Type == "Multi"):
        if(len(parsecommands(str(config[section]["commands"]))) < 2 ):
            print("less thantwo command on certain section Exiting....")
            sys.exit()
        else:
            return "Multi"
    
    elif(Type == "OneOrOther"):
        if(len(parsecommands(str(config[section]["commands"]))) < 2 ):
            print("less thantwo command on certain section Exiting....")
            sys.exit()
        else:
            return "OneOrOther"
    else:
        print("Unknown type of type, exiting...")
        sys.exit()


def ClassifyTrueIf(section):
    try:
        TrueIf = str(config[section]["TrueIf"])
    except KeyError:
        print("TrueIf does not exist in section " + section + " exiting...")
        sys.exit()

    possibles = globals().copy()
    possibles.update(locals())
    method = possibles.get(TrueIf)

    if not method:
        print("Unkown True If Method, exiting...")
        sys.exit()
    else:
        return TrueIf


def Main(section, Type, TrueIf):
    if(Type == "Single"):
            possibles = globals().copy()
            possibles.update(locals())
            method = possibles.get(TrueIf)
            result = method(parsecommands(str(config[section]["commands"]))[0], str(config[section]["result"]).encode('utf-8').decode('unicode_escape'))
            return result
    elif(Type == "Multi"):
            result = True
            possibles = globals().copy()
            possibles.update(locals())
            method = possibles.get(TrueIf)
            for command in parsecommands(str(config[section]["commands"])):
                result = method(command, str(config[section]["result"]).encode('utf-8').decode('unicode_escape'))
                if result == False:
                    return False
            return True
    elif(Type == "OneOrOther"):
        result = False
        possibles = globals().copy()
        possibles.update(locals())
        method = possibles.get(TrueIf)
        for command in parsecommands(str(config[section]["commands"])):
            result = method(command, str(config[section]["result"]).encode('utf-8').decode('unicode_escape'))
            if result == True:
                return True
        return False

def CheckStuff():
    try:
        TrueIf = str(config[section]["commands"])
    except KeyError:
        print("commands does not exist in section " + section + " exiting...")
        sys.exit()
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
        TrueIf = str(config[section]["result"]).encode('utf-8').decode('unicode_escape')
    except KeyError:
        print("result does not exist in section " + section + " exiting...")
        sys.exit()

def EvalStr(s, raw=False):
    r'''Attempt to evaluate a value as a Python string literal or
       return s unchanged.

       Attempts are made to wrap the value in one, then the 
       form of triple quote.  If the target contains both forms
       of triple quote, we'll just punt and return the original
       argument unmodified.

       Examples: (But note that this docstring is raw!)
       >>> EvalStr(r'this\t is a test\n and only a \x5c test')
       'this\t is a test\n and only a \\ test'

       >>> EvalStr(r'this\t is a test\n and only a \x5c test', 'raw')
       'this\\t is a test\\n and only a \\x5c test'
    '''

    results = s  ## Default returns s unchanged
    if raw:
       tmplate1 = 'r"""%s"""'
       tmplate2 = "r'''%s'''"
    else:
       tmplate1 = '"""%s"""'
       tmplate2 = "'''%s'''"

    try:
       results = eval(tmplate1 % s)
    except SyntaxError:
        try:
            results = eval(tmplate2 %s)
        except SyntaxError:
            pass
        return results



file = '/home/krypt/Projects/ScoringEngine/config.ini'
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
    Type = ClassifyType(section)
    TrueIf =  ClassifyTrueIf(section)
    if(float(config[section]["points"]) > 0):
        vulnstotal += 1
        totalpoints += float(config[section]["points"])
    result = Main(section, Type, TrueIf)
    #string = str(config[section]["result"].encode('utf-8').decode('unicode_escape'))
    #print(ast.literal_eval(string))
    if(result == True):
        if(float(config[section]["points"]) > 0):
            positive  += [section + ": " + str(config[section]["description"]) + " " + str(config[section]["points"] + "pts")]
            gained += float(config[section]["points"])
            vulnsfixed += 1
            currentpoints +=  float(config[section]["points"])
        
        if(float(config[section]["points"]) < 0):
        
            negetive += [section + ": " + str(config[section]["description"]) + " " + str(config[section]["points"] + "pts")]
            lost += float(config[section]["points"])
            currentpoints +=  float(config[section]["points"])
        
        if(float(config[section]["points"]) == 0):
        
            extra += [section + ": " + str(config[section]["description"]) + " " + str(config[section]["points"] + "pts")]
        


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