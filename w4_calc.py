
try:
    n_1 = int(input("enter 1 number"))
except ValueError:
    print("only num!")
try:
    n_2 = int(input("enter 2 number"))
except:
    print("only num!")

o_ = input("enter operand: +,-,*,/")
if o_ not in ['+','-','*','/']:
    raise ArithmeticError("mist")


if o_ == "+":
    res = n_1 + n_2
    print(res)
if o_ == "-":
    res = n_1 - n_2
    print(res)
try:
    if o_ == "/":
        res = n_1 / n_2
        print(res)
except ZeroDivisionError:
    print("/ 0!!!")

if o_ == "*":
    res = n_1 * n_2
    print(res)




