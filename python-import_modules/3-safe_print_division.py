def safe_print_division(a,b):
    try:
        result = a/b
    except ZeroDivisionError:
        print('unallowed')
    finally:
        print("{}/{} = {}".format(a,b,result) )



          

