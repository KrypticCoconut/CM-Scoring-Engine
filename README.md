# About

Cm scoring engine stans for confugurable modular scoring engine, you can add your own module (refer to wiki if you dont understand what i mean by modules) of code for extra functionality.

All of that is in a very neat config file which makes stuff easy to manager so you dont have to spend hour making a scoring engine like i did.

Refer to wiki for usage


## Installation
Installation is simple enough
```
sudo apt-get install python2 #this is for ubuntu 20.04 but install python2 for your distro
cd /opt
git clone https://github.com/PineMaster/CM-Scoring-Engine.git
```

## Setup

Inside the folder will be a `MainEngine.py` this is the main engine that controls the config and modules, -  best not to mess with this, `config.ini` this the config file where you add your vulns and stuff, `IfElseFuncs.pyc` this is the modules file where you can add more modules that you call from config file, if this sounds confusing, head to the wiki, everything is explained much more clearly.

> modules are basically functions which take parameters from the conf file and calculate if the vuln is fixed/points should be given (like one takes a command and if the output is the result var defined in the conf file, it will give points), you can decide which module you wanna use for a question or make ur own :)

head to the wiki to understand how to configure your config to use different modules and all that fun stuffz

after youre done making your config, You can make a cronjob or a systemd timer for the `MainEngine.py` so it actually runs the engine, ill be making a cronjob that runs this every 
you have to edit `/etc/crontab` and add this line

```
* * * * * root python2 /path/to/MainEngine.py # make sure you use python2 or you will get errors
```

this will run the engine every 1 minute :)

