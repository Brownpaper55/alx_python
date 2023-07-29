def raise_exception():
    try:
        raise TypeError()
    except TypeError:
        print('exception has been raised')
        