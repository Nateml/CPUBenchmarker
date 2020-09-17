from classes import calc
from datetime import date
import time


def cleanup():
    totEndTime = time.perf_counter()
    


    file = open("data.txt", "a")
    file.write(f"\n\nGolden Ratio = {ratioSum / count:0.10f}" ) 
    file.close()

    file = open("golden_ratios_log.txt", "a")
    dat = date.today()
    file.write("\n\n%s" % dat)
    file.write(f"\tGolden Ratio = {ratioSum / count:0.10f}")
    file.close()

    log.write(f"\n[%d, %d, %d, {totEndTime - totStartTime:0.4f}]" % (start, par, step))
    log.close()

    print("Highest persistance found in numbers 1 through %d:\n" % par)
    print(output)
    print(f"\ncompleted in {totEndTime - totStartTime:0.4f} seconds")

log = open("log.txt", "a")
file = open("data.txt", "w")
file.close()

totStartTime = time.perf_counter()

#parameters:
step = 64158
stop = 6479969
start = 1

try:
    ratioSum = 0
    count = 0
    for par in range(start, stop, step):
        sum = 0
        for i in range(1):
            startTime = time.perf_counter()
            output = calc.loop(par)
            endTime = time.perf_counter()
            timeTaken = endTime - startTime
            sum += timeTaken
        avg = sum / 1
        file = open("data.txt", "a")
        file.write("\n%d completed in:" % par)
        file.write("{:0.10f} ".format(avg))
        file.write(f"r = {par / timeTaken:0.5f}")
        file.close()
        count += 1
        ratioSum += (par / timeTaken)

    cleanup()


except KeyboardInterrupt:

    cleanup()
