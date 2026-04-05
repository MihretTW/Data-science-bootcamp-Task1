x=int(input("Enter the first number: ")) # take the first number as input
y=int(input("Enter the second number: ")) # take the second number as input
operation=input("Enter the operation (+, -, *, /): ") # take the operation as input
def calculate(x, y, operation): # define a function to perform the calculation
    if operation=='+': # if the operation is addition, return the sum of x and y
        return "Sum: " + str(x+y)
    elif operation=='-': # if the operation is subtraction, return the difference of x and y
        return "Difference: " + str(x-y)
    elif operation=='*': # if the operation is multiplication, return the product of x and y
        return "Product: " + str(x*y)
    elif operation=='/': # if the operation is division, return the quotient of x and y
        if y!=0: # check for division by zero
            return "Quotient: " + str(x/y)
        else:
            return "Error: Division by zero is not allowed"
    else:
        return "Error: Invalid operation" # if the operation is not valid, return an error message

result=calculate(x, y, operation) # call the calculate function and store the result
print(result) # print the result
