import json
import os
import shutil

# Path to your creative blueprints folder
cbppath = 'C:/Users/[insert username here]/AppData/Roaming/Axolot Games/Scrap Mechanic/User/[enter long number here]/Blueprints'

# Path to your survival blueprints folder
sbppath = 'C:/Program Files (x86)/Steam/steamapps/common/Scrap Mechanic/Survival/LocalBlueprints'


print("Searching for blueprint ids (folders)...", end="")
bpids = next(os.walk(cbppath))[1]

print(str(len(bpids)) + " found")

bpnames = []

print('Fetching blueprint names...', end="")

for blueprint in bpids:
    with open(cbppath + '/' + blueprint + '/description.json', 'r', encoding='utf8') as myblueprint:
        data = myblueprint.read()
    obj = json.loads(data)
    bpnames.append(obj['name'])

print('done')


while(True):
    searchresults = []
    searchterm = input("Search for blueprint: ")
    print('Searching for blueprints...', end='')
    for name in bpnames:
        if searchterm.lower() in name.lower():
            searchresults.append(name)
    print(str(len(searchresults)) + ' found')

    print('Search results:')
    i = 1
    for entry in searchresults:
        print(str(i) + ': ' + entry)
        i += 1


    userinput = input("Blueprint found? Y/N")
    if userinput.lower() == "y":
        while(True):
            searchterm = input("Enter entry number: ")
            searchterm = searchresults[int(searchterm)-1]
            userinput = input("Blueprint: '" + searchterm + "' Y/N")
            if userinput.lower() == "y":
                break

        src = cbppath + '/' + bpids[bpnames.index(searchterm)] + '/blueprint.json'
        searchterm = input("Rename blueprint to (no spaces): ")
        dst = sbppath + '/' + searchterm + '.blueprint'

        print('Copying blueprint...', end='')
        shutil.copyfile(src, dst)
        print('done')

        path = sbppath + '/'
        filename = searchterm + '.blueprint'

        print('Reading JSON...', end='')
        file = open(path + filename, 'r')
        jsonfile = json.load(file)
        file.close()
        print('done')

        print("Editing 'type'...", end='')
        for i in range(0, len(jsonfile['bodies'])):
            jsonfile['bodies'][i]['type'] = 0.0
        print('done')

        print("Saving changes...", end='')
        file = open(path + filename, 'w')
        json.dump(jsonfile, file)
        file.close()
        print('done')
