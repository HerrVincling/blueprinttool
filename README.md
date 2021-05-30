# blueprinttool

Here's going to be some scripts for Scrap Mechanic's Blueprint System. Everything WIP!


# survival.py

A script for easier importing of blueprints from creative into survival.

Be sure to edit the paths in the script to match with your installation!

The blueprints can be spawned with /import [name] if the dev mode is activated.


# ConnectionToolV2.py

A small library to create Blueprints consisting of logic gates.
Requires PIL (Pillow), install with:
'pip install Pillow'

To use it, make a new object of class 'BPJSON()' to get started.
Example:
a = BPJSON()
a.loadJSON('blank.json')

Then you can use these methods on the object:

loadJSON(path) // This is only used to load a blank json 
saveJSON(path) // This saves the blueprint
createChildDict() // 
