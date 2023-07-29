def safe_print_division(a,b):
    result = a / b
    try:
        result
    except ZeroDivisionError:
             result = None
             return result
    finally:
        print("{}:{}".format('Inside result', result))
        print("{}/{} = {}".format(a,b,result) )



          

safe_print_division(0,2)