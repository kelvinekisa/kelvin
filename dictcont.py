myfamily = {
    "My_Wife": {
        "name": "Mrs Ruth Mukiri",
        "DOB": 2003,
        "County": "Meru, Tigania East"
    },
    "My_First_Child": {
        "Name": "Salemy",
        "Year": 2029,
        "County": "Nairobi, Westlands"
    },
    "My_second_child": {
        "Name": "Hepphy",
        "Year": 2031,
        "County": "Nairobi"
    },
    "My_last_born": {
        "name": "Jair Hephy",
        "Year": 2035,
        "County": "Pennyslavania"
    }
}
print(myfamily)

#Or You can actually create dictionaries and then add them to one dictionary

mercedes = {
    "Model": "SUV, GlS",
    "YOM": 2023
}
toyota = {
    "Model": "Toyota XLZ",
    "YOM": 2024
    }
Nissan = {
    "Model": "nissan Note",
    "YOM": 2023
}
myvehicles = {
    "Vehicle1": mercedes,
    "vehicle2": toyota,
    "vehicle3": Nissan
}
print(myvehicles)

if "My_Wife" in myfamily and "name" in myfamily["My_Wife"]:
    print(myfamily["My_Wife"]["name"])
else:
    print("Key 'name' not found in My_Wife dictionary.")


print(myfamily["My_Wife"]["name"])

