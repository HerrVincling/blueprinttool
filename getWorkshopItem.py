#Straight up stolen from my getBlueprints.py tool haha

import json5 as json
import os
import shutil

# Path to your workshop folder
wspath = 'C:/Program Files (x86)/Steam/steamapps/workshop/content/387990'


print("Searching for ids (folders)...", end="")
bpids = next(os.walk(wspath))[1]
print(str(len(bpids)) + " found")

bpnames = []

print('Fetching workshop object names...', end="")
for blueprint in bpids:
    with open(wspath + '/' + blueprint + '/description.json', 'r', encoding='utf8') as myblueprint:
        data = myblueprint.read()
    try:
        obj = json.loads(data)
    except:
        print(blueprint)
        os.exit()
    bpnames.append(obj['name'])
print('done')


while(True):
    searchresults = []
    searchterm = input("Search for workshop object: ")
    print('Searching for objects...', end='')
    for name in bpnames:
        if searchterm.lower() in name.lower():
            searchresults.append(name)
    print(str(len(searchresults)) + ' found')

    print('Search results:')
    i = 1
    for entry in searchresults:
        print(str(i) + ': ' + entry)
        i += 1


    userinput = input("Object found? Y/N")
    if userinput.lower() == "y":
        while(True):
            searchterm = input("Enter entry number: ")

            try:
                int(searchterm)
            except:
                break

            searchterm = searchresults[int(searchterm)-1]
            userinput = input("Object: '" + searchterm + "' Y/N")
            if userinput.lower() == "y":
                src = wspath + '/' + bpids[bpnames.index(searchterm)]# + '/blueprint.json'
                dst = os.getcwd() + '/' + searchterm# + '/blueprint.json'

                print('Copying directory...', end='')
                shutil.copytree(src, dst)
                print('done')
                break