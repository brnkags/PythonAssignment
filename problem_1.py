a = input(" Enter a number ")
b = input(" Enter a number ")
if str.isdigit(a) and str.isdigit(b):
    print("Sum: ", int(a) + int(b))
    print("Difference: ", int(a) - int(b))
    print("Product: ", int(a) * int(b))
    if int(a[0:]) or int(b[0:]) != 0:
        print("Quotient: ", int(int(a) / int(b)))
    elif int(a[0:2]) or int(b[0:2]) is 0:
        print("Division by zero")
    if a == b:
        print("Equal")
    else:
        print("Not Equal")
else:
    print("Invalid input")