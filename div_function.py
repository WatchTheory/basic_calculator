
def division():
    """
    Created by: Charles Dillaway
    Inputs: function that asks for user inputs:
             x: the number you are dividing
             y: the number to be divided by
    Output: The quotient of a division operation
    """
    x = int(input('Enter your first number: ')) 
    y = int(input('Enter your second number: '))
    if y == 0:
        return  'Not a valid input'
    else:
        quotient = x / y
        return quotient



print(division())