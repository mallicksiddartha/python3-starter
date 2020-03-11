class calculator:
    def addition(x, y):
        add = x+y
        print(add)
    def subtraction(x, y):
        sub = x-y
        print(sub)
    def multiplication(x, y):
        mult = x*y
        print(mult)
    def division(x, y):
        if y != 0:
            div = x/y
        else:
            div = 'undefined'
        print(div)
