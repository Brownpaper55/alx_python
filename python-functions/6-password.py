def validate_password(password='password'):
    
    if len(password) <= 7:
            return False
    elif str.isalpha(password) == True:
          return False
    elif str.isnumeric(password) == True:
          return False
    elif str.isupper(password) == True:
          return False
    elif str.islower(password)== True:
          return False
    else:
          return True 
    
  
