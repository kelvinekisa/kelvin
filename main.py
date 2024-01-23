thisdict = {
    "kelvin Ekisa": "Ruth Mukiri",
    "Year": 2022,
    "Joy Kasusya": "Arnold Asitiba",
    "Year": 2021
}
print(thisdict)


#THE DICT CONSTRUCTOR

names = dict(reference = "John Chege", age = 20, country_of_origin = "Pakista", nationality = "Pakistanian")
print(names)

#accessing values in a dictionary
x = thisdict.get('kelvin Ekisa') #The get method
print(x)

y = thisdict["Joy Kasusya"]
print(y)

#Looping through the dictionary
for x in thisdict: #Print all key names in the dictionary, one by one:
    print(x)
for x in thisdict: #Print all values in the dictionary, one by one:
    print(thisdict)

#You can also use the values() method to return values of a dictionary
for x in thisdict.values():
    print(x)

#You can use the keys() method to return the keys of a dictionary:
for x in thisdict.keys():
    print(x)


#Loop through both keys and values, by using the items() method:
for x, y in thisdict.items():
    print(x, y)


