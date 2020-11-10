import os
import subprocess
import sys
try:
    import configparser
except:
    try:
        from six.moves import configparser
    except:
        print("Cant import modules config parser exitting")
        sys.exit()

file = 'config.ini'
config = configparser.RawConfigParser()
config.read(file)

def checkenoughinputs(inputs, needed):
        if(sorted(inputs) == sorted(needed)):
            return True
        else:
            print(sorted(inputs))
            print(sorted(needed))
            return False

#------------------------------------------------------------------------NEW FUNCTION-------------------------------------------------------------------------------


def ReturnTrue(section, inputs):  #return true true if command gives a return of 1 else 0
    requiredinputs = ["type",  "commands", "function", "description", "points"]
    if(checkenoughinputs(inputs, requiredinputs)):
        pass
    else:
        print("missing/extra input for section " + section)
        sys.exit()
    Type = config[section]["Type"]


    if(Type == "Single"):
        if(len(str(config[section]["commands"]).split(",")) > 1 ):
            print("more than one command on certain section Exiting....")
            sys.exit()

    elif(Type == "Multi"):
        if(len(str(config[section]["commands"]).split(",")) < 2 ):
            print("less thantwo command on certain section Exiting....")
            sys.exit()
    
    elif(Type == "OneOrOther"):
        if(len(str(config[section]["commands"]).split(",")) < 2 ):
            print("less thantwo command on certain section Exiting....")
            sys.exit()
    else:
        print("Unknown type of type, exiting...")
        sys.exit()


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
        print("missing/extra input for section " + section)
        sys.exit()
    Type = config[section]["Type"]


    if(Type == "Single"):
        if(len(str(config[section]["commands"]).split(",")) > 1 ):
            print("more than one command on certain section Exiting....")
            sys.exit()

    elif(Type == "Multi"):
        if(len(str(config[section]["commands"]).split(",")) < 2 ):
            print("less thantwo command on certain section Exiting....")
            sys.exit()
    
    elif(Type == "OneOrOther"):
        if(len(str(config[section]["commands"]).split(",")) < 2 ):
            print("less thantwo command on certain section Exiting....")
            sys.exit()
    else:
        print("Unknown type of type, exiting...")
        sys.exit()


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
        print("missing/extra input for section " + section)
        sys.exit()
    Type = config[section]["Type"]


    if(Type == "Single"):
        if(len(str(config[section]["commands"]).split(",")) > 1 ):
            print("more than one command on certain section Exiting....")
            sys.exit()

    elif(Type == "Multi"):
        if(len(str(config[section]["commands"]).split(",")) < 2 ):
            print("less thantwo command on certain section Exiting....")
            sys.exit()
    
    elif(Type == "OneOrOther"):
        if(len(str(config[section]["commands"]).split(",")) < 2 ):
            print("less thantwo command on certain section Exiting....")
            sys.exit()
    else:
        print("Unknown type of type, exiting...")
        sys.exit()


    if(Type == "Single"):
        if(str(subprocess.check_output(str(config[section]["commands"]).split(",")[0] + " || true", shell=True)) == str(config[section]["result"]).encode('utf-8').decode('unicode_escape')):
            return True
        else:
            return False
    elif(Type == "Multi"):
            for command in str(config[section]["commands"]).split(","):
                if(not str(subprocess.check_output(command + " || true",shell=True)) == str(config[section]["result"].encode('utf-8').decode('unicode_escape'))):
                    return False
            return True
    elif(Type == "OneOrOther"):
            for command in str(config[section]["commands"]).split(","):
                if(str(subprocess.check_output(command + " || true",shell=True)) == str(config[section]["result"].encode('utf-8').decode('unicode_escape'))):
                    return True
            return False

#------------------------------------------------------------------------NEW FUNCTION-------------------------------------------------------------------------------


def TrueIfOutputIsqualTo(command, outputresult):
    requiredinputs = ["type",  "commands", "function", "description", "points", "result"]
    if(checkenoughinputs(inputs, requiredinputs)):
        pass
    else:
        print("missing/extra input for section " + section)
        sys.exit()
    Type = config[section]["Type"]


    if(Type == "Single"):
        if(len(str(config[section]["commands"]).split(",")) > 1 ):
            print("more than one command on certain section Exiting....")
            sys.exit()

    elif(Type == "Multi"):
        if(len(str(config[section]["commands"]).split(",")) < 2 ):
            print("less thantwo command on certain section Exiting....")
            sys.exit()
    
    elif(Type == "OneOrOther"):
        if(len(str(config[section]["commands"]).split(",")) < 2 ):
            print("less thantwo command on certain section Exiting....")
            sys.exit()
    else:
        print("Unknown type of type, exiting...")
        sys.exit()


    if(Type == "Single"):
        if(str(subprocess.check_output(str(config[section]["commands"]).split(",")[0], shell=True)) == str(config[section]["result"]).encode('utf-8').decode('unicode_escape')):
            return True
        else:
            return False
    elif(Type == "Multi"):
            for command in str(config[section]["commands"]).split(","):
                if(not str(subprocess.check_output(command,shell=True)) == str(config[section]["result"].encode('utf-8').decode('unicode_escape'))):
                    return False
            return True
    elif(Type == "OneOrOther"):
            for command in str(config[section]["commands"]).split(","):
                if(str(subprocess.check_output(command,shell=True)) == str(config[section]["result"].encode('utf-8').decode('unicode_escape'))):
                    return True
            return False

#------------------------------------------------------------------------NEW FUNCTION-------------------------------------------------------------------------------
