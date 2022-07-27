def divide(x, y):
    try:
        
        result = x // y
        print("Your answer is :", result)
    except ZeroDivisionError:
        print(" dividing by zero error")
 

divide(3, 0)
