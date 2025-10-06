

def multiplication():
    """
    Created by: Charles Dillaway
    Inputs: function that asks for user inputs:
             x: a number you are multiplying
             y: anopther number you are multiplying
    Output: The product of a multiplication operation
    """
    try: 
        x = float(input('Enter your first number: ')) 
        y = float(input('Enter your second number: ')) 
        product = x * y
        return product 
    except:
        return "Not a valid input"
    
    
print(multiplication())