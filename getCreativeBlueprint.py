#Straight up stolen from my survival.py tool haha

import json
import os
import shutil

# Path to your creative blueprints folder
cbppath = 'C:/Users/[Windows User]/AppData/Roaming/Axolot Games/Scrap Mechanic/User/User_[long number, check your folder]/Blueprints'


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

        #print(bpids[bpnames.index(searchterm)])


        src = cbppath + '/' + bpids[bpnames.index(searchterm)] + '/blueprint.json'
        dst = os.getcwd() + '/blueprint.json'

        print('Copying blueprint...', end='')
        shutil.copyfile(src, dst)
        print('done')