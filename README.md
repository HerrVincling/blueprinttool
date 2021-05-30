# blueprinttool

<p>
Here's going to be some scripts for Scrap Mechanic's Blueprint System. Everything WIP!
</p>

# survival.py

<p>
A script for easier importing of blueprints from creative into survival.<br>
Be sure to edit the paths in the script to match with your installation!<br>
The blueprints can be spawned with /import [name] if the dev mode is activated.
</p>

# ConnectionToolV2.py

<p>A small library to create Blueprints consisting of logic gates.<br>
Requires PIL (Pillow), install with:<br>
'pip install Pillow'

To use it, make a new object of class 'BPJSON()' to get started.

Example:<br>
a = BPJSON()<br>
a.loadJSON('blank.json')


Then you can use these methods on the object:

loadJSON(path) # This is only used to load a blank json<br>
saveJSON(path) # This saves the blueprint<br>
createChildDict() # This updates the {block id : block array index} dictionary, do this before making connections!
</p>
