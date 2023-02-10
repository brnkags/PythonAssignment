a = input(" Enter a number ")
b = input(" Enter a number ")
if str.isdigit(a) and str.isdigit(b):
    if a == b:
        print("a and b are equal")
    elif a > b:
        print("a is greater than b")
    elif a < b:
        print("b is greater than a")
else:
    print("Invalid input")