def getPersistance(num):
    persistance = 0
    while(len(str(num)) > 1):
        print(num)
        print(len(str(num)))
        product = 1
        for i in str(num):
            dig = int(i)
            product = product * dig
        persistance += 1
        num = product

    print(persistance)
    print("")

getPersistance(277777788888899)