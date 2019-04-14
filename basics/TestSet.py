def createSet():
    fruitSet = {"apple", "banana", "grape", "orange"}
    # print all the fruits
    for fruit in fruitSet:
        print("Fruit Name : ", fruit)

    # Add a new type of fruit
    fruitSet.add("Figs")
    print("All fruits after addition : ", fruitSet)

    # add a duplicate fruit,
    fruitSet.add("apple")
    print("After adding duplicate : ", fruitSet)

    # delete/remove an element from Set, it throws error if the element is not there
    if fruitSet.__contains__("orange"):
        fruitSet.remove("orange")
    print("After deleting an element : ", fruitSet)

    # update some new fruits
    fruitSet.update(["Mango", "Pineapple"])
    print("After updating : ", fruitSet)

    # total size of set
    size = len(fruitSet)
    print("Total no of elements : ", size)

    # use of discard
    fruitSet.discard("Laxman Phal")
    print("All fruits after discard : ", fruitSet)
    # fruitSet.remove("Laxman Phal")#Raises KeyError if  elem is not contained in the set.

    # You can also create a set like the below

    carSet = set(("Mercedes", "BMW", "Audi"))
    print("All cars : ", carSet)


if __name__ == "__main__":
    createSet()
