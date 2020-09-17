import sys
import signal

def log(signal, frame):
    print("whoops")
    file = open("testlog.txt", "w")
    file.write("terminated")
    file.close()
    sys.exit(0)

signal.signal(signal.SIGINT, log)