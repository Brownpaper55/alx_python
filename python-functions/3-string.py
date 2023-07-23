def reverse_string(string = 'string'):
    rev = len(string)
    
    while rev != 0:
        # sas = character of string returned
        sas = string[rev - 1]
        rev -= 1
        print(sas, end='')
    return ''


 