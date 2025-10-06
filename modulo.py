def modulo():
    """
    Created by: Daniel 
    Inputs: 
        Function asks user for inputs:
            x: first number to be divided
            y: second number to be divided by
    Outputs:
        result: the remainder of the division of x / y
    """
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    result = x % y
    return result
