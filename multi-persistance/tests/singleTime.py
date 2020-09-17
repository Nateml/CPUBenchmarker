import time

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


golden_ratio = 270000
par = 1069
start_time = time.perf_counter()
print(loop(par))
end_time = time.perf_counter()

print(f"time taken: {end_time - start_time:0.4f}")
