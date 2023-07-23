def is_prime(number):
    if number == (2 or 3):
        return True
    
    elif number % 2 == 0:
        return False
    
    elif number % 3 == 0:
        return False
    
    elif number == 1:
        return False
    else:
        return True

      
