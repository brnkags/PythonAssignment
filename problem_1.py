a = input(" Enter a number ")
b = input(" Enter a number ")
if str.isdigit(a) and str.isdigit(b):
    print("Sum: ", int(a) + int(b))
    print("Difference: ", int(a) - int(b))
    print("Product: ", int(a) * int(b))
    if a or b == 0:
        print("Division by zero")
    else:
        print("Quotient: ", int(int(a) / int(b)))
    if a == b:
        print("Equal")
    else:
        print("Not Equal")
else:
    print("Invalid input")