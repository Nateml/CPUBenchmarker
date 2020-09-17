def getPersistance(num):
    persistance = 0
    while(len(str(num)) > 1):
        product = 1
        for i in str(num):
            dig = int(i)
            product = product * dig
        persistance += 1
        num = product

    return (persistance)

def loop(par):
    highPers = 0
    highPersNum = 0
    for i in range(par):
        pers = getPersistance(i)
        if pers > highPers:
            highPers = pers
            highPersNum = i
    return([highPers, highPersNum])

    




