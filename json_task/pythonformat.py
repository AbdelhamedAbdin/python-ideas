import json

arr = {
    'name': 'Abdin',
    'age': 24
}

x = json.dump(arr, open("text.json","w"), indent=4)

load = json.load(open("text.json", "r"))

print(load)