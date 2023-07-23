def fibonacci_sequence(n):
    i = 0
    k = 1
    count = 0
    j = []
    if  n == 0:
        j = []
        
    elif n == 1:
        j.append(0)

    else:
        while count < n:
            j.append(i)
            c = i + k
            i = k
            k = c
            count += 1
    return j



