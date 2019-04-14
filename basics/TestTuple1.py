def createTuple():
    tuple1 = ("Hello", "Hello-1", 1, 2, 3, 4, 5, "It is a sentence")
    for data in tuple1:
        print("Data in Tuple : ", data)
    print("Total elements in tuple1 : ", len(tuple1))

    #tuple to list
    list1 = list(tuple1)
    list1.append("Elephant")
    print("List 1 : ",list1)

    #convert list to tuple
    tuple2 = tuple(list1)
    print("Tuple 2 : ",tuple2)



if __name__ == "__main__":
    createTuple()
