import os
import subprocess
import sys



def ReturnTrue(command, outputresult):  #return true true if command gives a return of 1 else 0
    try:
        subprocess.check_output(command, shell=True)
        return True;
    except subprocess.CalledProcessError:
        return False;


def IfOutput(command, outputresult): #return true true if command gives any output else 0, #note stderr isnt counted as output
    if(subprocess.check_output(command + " || true", shell=True)):
        return True
    else: 
        return False

def IfOutputIsqualTo(command, outputresult):  #return true if comman's output (converted to string) is equal to given phrase (also converted to string), #note stderr isnt counted as output
    if(str(subprocess.check_output(command + " || true", shell=True)) == str(outputresult)):  # migth wanna do some testing because this is quite finnicy because of newlines and shit
        return True
    else:
        return False 

def TrueIfOutputIsqualTo(command, outputresult):
    try:
        if(str(subprocess.check_output(command, shell=True)) == str(outputresult)):
            return True
        else:
            return False
    except subprocess.CalledProcessError:
        return False