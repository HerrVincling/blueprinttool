import json

path = 'blueprint.json'  # The blueprint files needs to be in the same folder as this script!
axis = "y"

axisdict = {"x": 1, "y": 2, "z": 3}
axisno = axisdict[axis]

offsettable = {2: {-1: {'x': 1, 'y': 0, 'z': 1}, 1: {'x': 0, 'y': 0, 'z': 0}, -3: {'x': 0, 'y': 0, 'z': 1}, 3: {'x': 1, 'y': 0, 'z': 0}}, 1: {2: {'x': 0, 'y': 0, 'z': 1}, -3: {'x': 0, 'y': 1, 'z': 1}, -2: {'x': 0, 'y': 1, 'z': 0}, 3: {'x': 0, 'y': 0, 'z': 0}}, -2: {1: {'x': 0, 'y': 1, 'z': 1}, -3: {'x': 1, 'y': 1, 'z': 1}, -1: {'x': 1, 'y': 1, 'z': 0}, 3: {'x': 0, 'y': 1, 'z': 0}}, -1: {-2: {'x': 1, 'y': 1, 'z': 1}, 3: {'x': 1, 'y': 1, 'z': 0}, 2: {'x': 1, 'y': 0, 'z': 0}, -3: {'x': 1, 'y': 0, 'z': 1}}, -3: {-1: {'x': 1, 'y': 1, 'z': 1}, 1: {'x': 0, 'y': 0, 'z': 1}, -2: {'x': 0, 'y': 1, 'z': 1}, 2: {'x': 1, 'y': 0, 'z': 1}}, 3: {1: {'x': 0, 'y': 1, 'z': 0}, -1: {'x': 1, 'y': 0, 'z': 0}, 2: {'x': 0, 'y': 0, 'z': 0}, -2: {'x': 1, 'y': 1, 'z': 0}}}

with open(path, 'r', encoding='utf8') as file:
    data = file.read()
    json1 = json.loads(data)

#xaxis +/- 3|? inv on Z mirror only
#xaxis +/- 2|? inv on Y mirror only
#xaxis +/- 1|? inv on X mirror only
#zaxis always inv

#xaxis = +/- 3|1 and 2|1 mirroring xaxis
    #inv 1 on 3|1 mirrors Y    ##inv 3&1 on 3|1 mirrors Z
    ##inv 2&1 on 2|1 mirrors Y   inv 1 on 2|1 mirrors Z
#yaxis = +/- 3|2 and 1|2 mirroring yaxis
    #inv 1&2 on 1|2 mirrors X   inv 2 on 1|2 mirrors Z
    ## inv 2 on 3|2 mirrors X   inv 3&2 on 3|2 mirrors Z
#zaxis = +/- 2|3 and 1|3 mirroring zaxis
    #inv 2&3 on 2|3 mirrors Y   inv 3 on 2|3 mirrors X? inv
    #inv 3 on 1|3 mirrors Y   inv 1&3 on 1|3 mirrors X?

for j in range(len(json1["bodies"])):
    for i in json1["bodies"][j]["childs"]:
        offset = offsettable[i["xaxis"]][i["zaxis"]]
        i["pos"]["x"] -= offset["x"]
        i["pos"]["y"] -= offset["y"]
        i["pos"]["z"] -= offset["z"]

        i["pos"][axis] *= -1
        #if "bounds" in i:
        #    i["pos"][axis] -= i["bounds"][axis] - 1

        if axisno != abs(i["zaxis"]):
            if axisno == abs(i["xaxis"]):
                offset = offsettable[-i["xaxis"]][-i["zaxis"]]
                i["xaxis"] *= -1
            else:
                offset = offsettable[i["xaxis"]][-i["zaxis"]]
            i["zaxis"] *= -1
        
        i["pos"]["x"] += offset["x"]
        i["pos"]["y"] += offset["y"]
        i["pos"]["z"] += offset["z"]


with open(path, 'w') as file:
    file.write(json.dumps(json1, indent=2))

