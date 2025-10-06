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
    try:
        x = float(input("Enter the first number: "))
        y = float(input("Enter the second number: "))
        result = x % y
    except:
        return "Cancelling function. Input must be a number"
    return result

