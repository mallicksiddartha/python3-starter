import subprocess

#check_output gets the result as string
dirResult = subprocess.check_output('dir', shell=True) #why 'shell=True' don't know yet!
print(dirResult)
print('\n\n\n\n')
#call another python script from this script and get the result
anotherScriptResult = subprocess.check_output('python statistics1.py',shell=True)
print(anotherScriptResult)

