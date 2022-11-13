#Made By Amy Readman




#list of options
print ("Addition = 1")
print ("Subtraction = 2")
print ("Multiplication = 3")
print ("Division = 4")


#choose method
method = int(input ("What would you like to do? "))
num1 = int(input ("What is your first number? "))
num2 = int(input ("What is your second number? "))

#check addition
if method == int("1"):
    print (num1, "+", num2, "=", num1 + num2)

#check subtraction
elif method == int("2"):
    print (num1, "-", num2, "=", num1 - num2)

    #check multiplication
elif method == int("3"):
    print (num1, "x", num2, "=", num1 * num2)


    #check division
elif method == int("4"):
    print (num1, "/", num2, "=", num1 / num2)




