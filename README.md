# About

Cm scoring engine stands for confugurable modular scoring engine, it is a python3 based scoring engine that uses modules to asses if a vuln is fixed or not, you can add your own module (refer to wiki if you dont understand what i mean by modules) of code for extra functionality.

 modules are basically functions which take parameters from the conf file and calculate if the vuln is fixed/points should be given (like one takes a command and if the output is the result variable defined in the conf file, it will give points), you can decide which module you wanna use for a question or make ur own :)


All of that is in a very neat config file which makes stuff easy to manager so you dont have to spend hour making a scoring engine like i did.

Refer to wiki for usage


## Installation
Installation is simple enough

```
sudo apt-get install git python3 python3-pip python-gobject libnotify-bin libnotify-dev # ubuntu 20
sudo apt-get install python3-pip python3 python-gobject libnotify-bin libnotify-dev libnotify-cil-dev git #ubuntu 18
pip3 install playsound
sudo pip3 install playsound
cd /opt
git clone https://github.com/PineMaster/CM-Scoring-Engine.git
```

# Todo

Add error logging so it isnt just print()
