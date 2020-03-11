import os
import sys
import time

currentDir = os.getcwd()
print("currentDir", currentDir)

try:
    os.mkdir("example directory")
    time.sleep(5)
    os.rename("example directory", "toss a coin to your witcher")
except:
    print("Unexpected error:", sys.exc_info()[0])
    time.sleep(5)
    os.rmdir("example directory")
finally:
    print("didn't know about the finally block. Good to have ya mate!!")
