def addition():
    """
    Created by: Kevin
    Inputs: 
        Function asks user for inputs:
            x: first number to be divided
            y: second number to be divided by
    Outputs:
        result: the remainder of the added of x + y
    """
    try:
       x = float(input("Enter the first number: "))
       y = float(input("Enter the second number: "))
       result = x + y
    except:
       return "Please Enter a Number"
   
    return result

print(addition())


