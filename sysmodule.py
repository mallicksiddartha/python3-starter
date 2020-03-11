import sys as cachika
cachika.stderr.write("Test std error\n")
cachika.stdout.write("Test std out\n")

print(cachika.argv)

def addFive(args):
    for arg in args:
        if isFloat(arg):
            print(float(arg)+10)
        else:
            print(arg)
    print("Done, Thanks")
    

def isFloat(value):
    try:
        float(value)
        return True
    except:
        return False

if len(cachika.argv) > 1:
    addFive(cachika.argv)
