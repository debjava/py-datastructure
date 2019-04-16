# Python dictionary is like map in Java

def createDictionary():
    myMap = {
        "Key-1": "Value-1",
        "Key-2": "Value-2",
        "Key-3": "Value-3",
        "Key-4": "Value-4",
        "Key-5": "Value-5",
    }

    print("My Map Values : ", myMap)
    # Get value by key
    print("Value for the key, Key-3 : ", myMap.get("Key-3"))
    # You can also get the value from a key, in the following manner
    value = myMap["Key-3"]
    print("Now Value : " + value)

    # Update value in the Map/Dictionary
    myMap["Key-3"] = "Value-333"
    print("Now Map values : ", myMap)

    # Show all the key and value from the map/dictionary
    for data in myMap:  # It obtains only keys from the dictionary
        print("Now key : ", data)  # Prints only keys, not the values

    # Print all the values from a map/dictionary
    for key in myMap:
        value = myMap[key]
        print("Values inside myMap : ", value)

    print("------------------------------------------------------")

    # You can also display all the values directly
    for value in myMap.values():
        print("Value inside myMap : ", value)

    # Loop through both keys and values, by using the items() function
    for key, value in myMap.items():
        print(key + "<----->" + value)

    # Check whether the map/dictionary contains a key
    if "Key-1" in myMap:
        print("Now value for Key-1", myMap["Key-1"])

    # What is the size/length of the map/dictionary
    print("Size or Length of myMap : ", len(myMap))

    # Again add few items in map/dictionary
    myMap["Key-7"] = "Value-7"
    myMap["Key-9"] = "Value-9"
    myMap["Key-11"] = "Value-11"
    print("After adding new extra values : ",myMap)

    # Remove a key and value from
    myMap.pop("Key-11")
    if "Key-19" in myMap:
        myMap.pop("Key-19") # If you dont write an if condition, it will throw error.
    print("After deleting element : ", myMap)
    #also you can use like this
    del myMap["Key-9"]
    print("After deleting element : ", myMap)

    # Make a copy of a dictionary with the dict() method:
    # mydict = dict(thisdict)

    # Make a copy of a dictionary with the copy() method:
    # mydict = thisdict.copy()

    # It is also possible to use the dict() constructor to make a new dictionary:
    # thisdict =	dict(brand="Ford", model="Mustang", year=1964)




if __name__ == "__main__":
    createDictionary()
