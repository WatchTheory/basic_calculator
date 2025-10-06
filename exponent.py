def exp():
    """
    Created by: Daniel
    Inputs:
        Function asks user for inputs:
            x: the base number
            y: the power the base number should go to
    outputs:
        result: the result of x to the power of y
    """
    try:
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))
        result = x ** y
    except:
        return "Cancelling function. Input must be a number"
    
    
    return result

print(exp())
print(exp())
print(exp())