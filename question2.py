dict1 = {
    "1": "name1",
    "2": "name2",
    "3": "name3"

}

dict2 = {
    "1": 50,
    "2": 80,
    "3": 100,
    "4": 10
}

maxTuple = max(dict2.items(), key=lambda x: x[1])
maxDict = dict.fromkeys(maxTuple[0], maxTuple[1])
print(maxDict)
