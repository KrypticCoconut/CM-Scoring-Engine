import os
import subprocess
import sys
import re
import configparser
import pathlib


file = str(pathlib.Path(__file__).parent.absolute()) + '/config.ini'
config = configparser.RawConfigParser()
config.read(file)

def checkenoughinputs(inputs, needed):
        if(sorted(inputs) == sorted(needed)):
            return True
        else:
            return False

#------------------------------------------------------------------------NEW FUNCTION-------------------------------------------------------------------------------


def ReturnTrue(section, inputs):  #return true true if command gives a return of 1 else 0
    requiredinputs = ["type",  "commands", "function", "description", "points"]
    if(checkenoughinputs(inputs, requiredinputs)):
        pass
    else:
        return "missing/extra input for section " + section
    Type = config[section]["Type"]


    if(Type == "Single"):
        if(len(str(config[section]["commands"]).split(",")) > 1 ):
            return "more than one command  for single on section " + section+" Exiting...."

    elif(Type == "Multi"):
        if(len(str(config[section]["commands"]).split(",")) < 2 ):
            return "less than two command for multi on section " + section +" Exiting...."
    
    elif(Type == "OneOrOther"):
        if(len(str(config[section]["commands"]).split(",")) < 2 ):
            return "less than two command for OneOrOther on section " + section +" Exiting...."
    else:
        return "Unknown type of Type in section " + section+ " , exiting..."


    if(Type == "Single"):
        try:
            subprocess.check_output(str(config[section]["commands"]).split(",")[0], shell=True)
            return True
        except subprocess.CalledProcessError:
            return False
    elif(Type == "Multi"):
            for command in str(config[section]["commands"]).split(","):
                try:
                    subprocess.check_output(command, shell=True)
                except subprocess.CalledProcessError:
                    return False
            return True
    elif(Type == "OneOrOther"):
            for command in str(config[section]["commands"]).split(","):
                try:
                    subprocess.check_output(command, shell=True)
                    return True
                except subprocess.CalledProcessError:
                    pass 
            return False
        

    
#------------------------------------------------------------------------NEW FUNCTION-------------------------------------------------------------------------------

def IfOutput(section, inputs): #return true true if command gives any output else 0, #note stderr isnt counted as output
    requiredinputs = ["type",  "commands", "function", "description", "points"]
    if(checkenoughinputs(inputs, requiredinputs)):
        pass
    else:
        return "missing/extra input for section " + section
    Type = config[section]["Type"]


    if(Type == "Single"):
        if(len(str(config[section]["commands"]).split(",")) > 1 ):
            return "more than one command  for single on section " + section+" Exiting...."

    elif(Type == "Multi"):
        if(len(str(config[section]["commands"]).split(",")) < 2 ):
            return "less than 2 command  for multi on section " + section+" Exiting...."
    
    elif(Type == "OneOrOther"):
        if(len(str(config[section]["commands"]).split(",")) < 2 ):
            return "Unknown type of type on section "+ section+", exiting..."
    else:
        return "Unknown type of type on section "+ section+", exiting..."


    if(Type == "Single"):
        if(subprocess.check_output(str(config[section]["commands"]).split(",")[0] + " || true", shell=True)):
            return True
        else:
            return False
    elif(Type == "Multi"):
            for command in str(config[section]["commands"]).split(","):
                if(not subprocess.check_output(command + " || true", shell=True)):
                    return False
            return True
    elif(Type == "OneOrOther"):
            for command in str(config[section]["commands"]).split(","):
                if(subprocess.check_output(command + " || true", shell=True)):
                    return True
            return False

#------------------------------------------------------------------------NEW FUNCTION-------------------------------------------------------------------------------


def IfOutputIsqualTo(section, inputs):  #return true if comman's output (converted to string) is equal to given phrase (also converted to string), #note stderr isnt counted as output
    requiredinputs = ["type",  "commands", "function", "description", "points", "result"]
    if(checkenoughinputs(inputs, requiredinputs)):
        pass
    else:
        return "missing/extra input for section " + section
    Type = config[section]["Type"]


    if(Type == "Single"):
        if(len(str(config[section]["commands"]).split(",")) > 1 ):
            return "more than one command  for single on section " + section+" Exiting...."

    elif(Type == "Multi"):
        if(len(str(config[section]["commands"]).split(",")) < 2 ):
            return "less than 2 command  for multi on section " + section+" Exiting...."
    
    elif(Type == "OneOrOther"):
        if(len(str(config[section]["commands"]).split(",")) < 2 ):
            return "less than 2 command  for OneOrOther on section " + section+" Exiting...."
    else:   
        return "Unknown type of type on section "+ section+", exiting..."

    if(Type == "Single"):
        if(str(subprocess.check_output(str(config[section]["commands"]).split(",")[0] + " || true", shell=True).decode("ascii")) == str(config[section]["result"]).encode('utf-8').decode('unicode_escape')):
            return True
        else:
            return False
    elif(Type == "Multi"):
            for command in str(config[section]["commands"]).split(","):
                if(not str(subprocess.check_output(command + " || true",shell=True).decode("ascii")) == str(config[section]["result"].encode('utf-8').decode('unicode_escape'))):
                    return False
            return True
    elif(Type == "OneOrOther"):
            for command in str(config[section]["commands"]).split(","):
                if(str(subprocess.check_output(command + " || true",shell=True).decode("ascii")) == str(config[section]["result"].encode('utf-8').decode('unicode_escape'))):
                    return True
            return False

#------------------------------------------------------------------------NEW FUNCTION-------------------------------------------------------------------------------


def TrueIfOutputIsqualTo(command, outputresult):
    requiredinputs = ["type",  "commands", "function", "description", "points", "result"]
    if(checkenoughinputs(inputs, requiredinputs)):
        pass
    else:
        return "missing/extra input for section " + section
    Type = config[section]["Type"]


    if(Type == "Single"):
        if(len(str(config[section]["commands"]).split(",")) > 1 ):
            return "more than one command  for single on section " + section+" Exiting...."

    elif(Type == "Multi"):
        if(len(str(config[section]["commands"]).split(",")) < 2 ):
            return "less than 2 command  for multi on section " + section+" Exiting...."
    
    elif(Type == "OneOrOther"):
        if(len(str(config[section]["commands"]).split(",")) < 2 ):
            return "Unknown type of type on section "+ section+", exiting..."
    else:
        return "Unknown type of type on section "+ section+", exiting..."


    if(Type == "Single"):
        if(str(subprocess.check_output(str(config[section]["commands"]).split(",")[0], shell=True).decode("ascii") )== str(config[section]["result"]).encode('utf-8').decode('unicode_escape')):
            return True
        else:
            return False
    elif(Type == "Multi"):
            for command in str(config[section]["commands"]).split(","):
                if(not str(subprocess.check_output(command,shell=True).decode("ascii")) == str(config[section]["result"].encode('utf-8').decode('unicode_escape'))):
                    return False
            return True
    elif(Type == "OneOrOther"):
            for command in str(config[section]["commands"]).split(","):
                if(str(subprocess.check_output(command,shell=True).decode("ascii")) == str(config[section]["result"].encode('utf-8').decode('unicode_escape'))):
                    return True
            return False

#------------------------------------------------------------------------NEW FUNCTION-------------------------------------------------------------------------------

def CommandRegex(section, inputs):  #return true true if command gives a return of 1 else 0
    requiredinputs = ["regex",  "command", "function", "description", "points"]
    if(checkenoughinputs(inputs, requiredinputs)):
        pass
    else:
        return "missing/extra input for section " + section
    
    string = subprocess.check_output(config[section]["command"] + " || true", shell=True).decode("ascii")
    try:
        x = re.findall(r'' + config[section]["regex"]+'', string)
    except SyntaxError:
        return "Invalid regex in section " + section +", exiting"

    if(len(x) > 0):
        return True
    else:
        return False

#------------------------------------------------------------------------NEW FUNCTION-------------------------------------------------------------------------------


def IfNotOutput(section, inputs): #return true true if command gives any output else 0, #note stderr isnt counted as output
    requiredinputs = ["type",  "commands", "function", "description", "points"]
    if(checkenoughinputs(inputs, requiredinputs)):
        pass
    else:
        return "missing/extra input for section " + section
    Type = config[section]["Type"]


    if(Type == "Single"):
        if(len(str(config[section]["commands"]).split(",")) > 1 ):
            return "more than one command  for single on section " + section+" Exiting...."

    elif(Type == "Multi"):
        if(len(str(config[section]["commands"]).split(",")) < 2 ):
            return "less than 2 command  for multi on section " + section+" Exiting...."
    
    elif(Type == "OneOrOther"):
        if(len(str(config[section]["commands"]).split(",")) < 2 ):
            return "Unknown type of type on section "+ section+", exiting..."
    else:
        return "Unknown type of type on section "+ section+", exiting..."


    if(Type == "Single"):
        if(subprocess.check_output(str(config[section]["commands"]).split(",")[0] + " || true", shell=True)):
            return False
        else:
            return True
    elif(Type == "Multi"):
            for command in str(config[section]["commands"]).split(","):
                if(subprocess.check_output(command + " || true", shell=True)):
                    return False    
            return True
    elif(Type == "OneOrOther"):
            for command in str(config[section]["commands"]).split(","):
                if(not subprocess.check_output(command + " || true", shell=True)):
                    return True
            return False