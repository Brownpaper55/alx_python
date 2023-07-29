def argv(*args):
    print ("{} {}.".format(len(args),'arguments'))
    i = 0
    for agg in args:
        i += 1
        print("{}:{}".format(i,agg))
        



argv()

