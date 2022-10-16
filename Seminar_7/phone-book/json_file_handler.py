import json


def read(path, handler):
    with open(path, 'r') as f:
        j = json.load(f)
        for person in j:
            handler(person["name"], person["lastname"],
                    person["phone"], person["description"])


def write(path, data):
    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
