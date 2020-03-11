
#eval evaluates what's passed as argument in it, doesn't assign anything
list_str1 = "[1,5,7,8,2]"
list_str = eval(list_str1)

print(list_str)
print(list_str[1])

#this throws error, "eval" cannot execute a line and assign the
#variable "list_str2"
#eval("list_str2 = [1,5,7,8,3]")

x = input("write:")

print(x)
x_with_eval = eval(input("write with eval:"))
print(x_with_eval)

