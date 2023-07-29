def safe_print_division(a,b):
    result = a / b
    try:
        result
    except ZeroDivisionError:
        print(None)
    finally:
        print(result)
        print("{}/{} = {}".format(a,b,result) )



          

