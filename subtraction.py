def subtraction():
    """
    Created by: Kevin 
    Inputs: 
        Function asks user for inputs:
            x: first number to be subtracted
            y: second number to be subtracted by
    Outputs:
        result: the remainder of the subtracted of x - y
    """
    try:
       x = float(input("Enter the first number: "))
       y = float(input("Enter the second number: "))
       result = x - y
    except:
       return "Please Enter a Number"
   
    return result

print(subtraction())


