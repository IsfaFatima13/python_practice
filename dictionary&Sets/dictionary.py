s={}#empty dictionary
dictionary={
    "isfa": 101,
    "fatima": 102,
    "urooj": 103,
    "list":[1,2,3,4],
    "izza":"isaa"
}
print(dictionary["isfa"])#it is muetable it can be changed 
#
print(dictionary["list"])
print(dictionary.items())
print(dictionary.keys())
print(dictionary.values())
print(dictionary.update({"isfa":1001}))
print(dictionary)
print(dictionary.get("isfa"))
print(type(dictionary))