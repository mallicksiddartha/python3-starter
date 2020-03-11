exec("print('printing this with exac command')")

list_str = "[3,4,5,2]"
list_str1 = exec(list_str)

#executing the string "[3,4,5,2]" in python compiler won't do anything so
#result is none
print(list_str1)


list_str3 = exec("list_str2 = [31,43,54,21]")

#now we have a new variable "list_str2", and executing the command doesn't
#return anything, so the "list_str3" is none(null)
print(list_str2)
print(list_str3)

exec("""
def test():
    print("multiline comment using exec command")
""")

exec("def test2(): print('Wooh, did this created a new method?')")

test()
test2()
