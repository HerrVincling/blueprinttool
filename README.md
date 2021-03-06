# blueprinttool

<p>
Here's going to be some scripts for Scrap Mechanic's Blueprint System. Everything WIP!
</p>

## getCreativeBlueprints.py

<p>
A script to find & get blueprint JSONs from the blueprint folder.<br>
Be sure to edit the paths in the script to match with your installation!<br>
The blueprint file will be copied to the same directory where <code>getCreativeBlueprints.py</code> is located.
</p>

## getWorkshopItem.py

<p>
A script to find & get the folder of workshop items.<br>
Be sure to edit the paths in the script to match with your installation!<br>
The workshop item folder will be copied to the same directory where <code>getWorkshopItem.py</code> is located.
</p>

## survival.py

<p>
A script for easier importing of blueprints from creative into survival.<br>
Be sure to edit the paths in the script to match with your installation!<br>
The blueprints can be spawned with /import [name] if the dev mode is activated.
</p>

## ConnectionToolV2.py

<p>A small module to create Blueprints consisting of logic gates.<br>
Requires PIL (Pillow), install with:<br>

`pip install Pillow`

To use it, make a new object of class 'BPJSON()' to get started.

Example:<br>
a = BPJSON()<br>
a.loadJSON('blank.json')


Then you can use these methods on the object:
```python
loadJSON(path) # This is only used to load a blank json

saveJSON(path) # This saves the blueprint

createChildDict() # This updates the {block id : block array index} dictionary, do this before making connections!

makeConnection(ID1, ID2) # This creates a connection between two blocks (logic gates)

makeConnections(IDs1, IDs2) # This creates connection between a list of blocks (logic gates)

createLogicGate(x, y, z, color, ID, mode) # Creates a block (logic gate)
  # Modes: 0=AND, 1=OR, 2=XOR, 3=NAND, 4=NOR, 5=XNOR
  # Color: '000000' - 'FFFFFF' (Hex String)

createLogicGates(x, y, z, direction, color, IDs, mode) # Creates multiple blocks (logic gates)
  # Direction: [x, y, z]
  # Modes: 0=AND, 1=OR, 2=XOR, 3=NAND, 4=NOR, 5=XNOR
  # Color: '000000' - 'FFFFFF' (Hex String)

wireFrames(IDs1, IDs2, data) # Experimental: Makes connections according to data
  # Data (length=IDs1*IDs2): [True, False...]
  # Wires all IDs1 to all IDs2

wireDecoder(inputIDs, negatedInputIDs, outputIDs) # Used to make the connections for a decoder
```

To import data from an image file, use this function:
```python
importFrames(path, frameWidth, frameHeight, horizontalCount, verticalCount) # Extracts binary data from an image file
  # frameWidth & frameHeight = Chunk size
  # horizontalCount & verticalCount = Chunk grid size
  # Returns an bool array [True, False...]
  # See 'img.png' as example
```
</p>
