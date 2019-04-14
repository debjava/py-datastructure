def createList():
    fruitsList = ["apple", "banana", "cherry"]
    print("Fruit List : ", fruitsList)
    # Iterate the list of fruits
    for i in fruitsList:
        print("Value : ", i)
    # Add to fruits list
    fruitsList.append("kiwi")
    fruitsList.append("Grape")
    fruitsList.append("Orange")
    print("After adding furits now list ...")
    for fruit in fruitsList:
        print("Now Fruit : ", fruit)

    # Delete a fruits from List
    if fruitsList.__contains__("Grape"):
        fruitsList.remove("Grape")
        print("Fuits : ", fruitsList)

    # Update a fruit, instead of apple, use Green Apple
    for fruit in fruitsList:
        value = fruit
        if value == "apple":
            # Find the index of apple
            index = fruitsList.index("apple")
            print("Index of Apple : ", index)
            # Now update apple with Green Apple
            fruitsList[index] = "Green Apple"
    # finally print the details of the fruit list
    print("Show all the updated fruits ...")
    for fruit in fruitsList:
        print(fruit, end="\t")
    print("\n")

    # Insert at the beginning of List
    fruitsList.insert(0, "Laxman Phal")  # Insert at the top
    print("Inserted fruits : ", fruitsList)

    # Insert at the last
    fruitsList.append("Figs")  # Insert at the last
    print("Inserted at the end : ", fruitsList)

    # Get the index in list of fruits
    print("All the fruits with their indexes")
    for fruit in fruitsList:
        fruitIndex = fruitsList.index(fruit)
        print(fruit, "<---->", fruitIndex)

    #Sort a list
    fruitsList.sort();
    print("Sorted in Ascending order : ",fruitsList)
    print("-------- In descending order ------")
    fruitsList.sort(reverse = True)
    print("Sorted in Descending order : ", fruitsList)


if __name__ == "__main__":
    createList()
