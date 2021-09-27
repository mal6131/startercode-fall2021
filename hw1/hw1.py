from hwfunctions import fun_factor, fun_inc

def delayed_increment(c, start, end):
    # use fun_inc
    # return  sum([ fun_inc(i) for i in  range(start , end)]
    objects = []

    for i in range(start, end):
        x = delayed(fun_inc)(i)
        objects.append(x)

    z = delayed(sum)(objects)
    return z

def delayed_factor(c, start, end):
    # use fun_factor
    # return  sum([ fun_factor(i) for i in range(start , end)])
    objects = []

    for i in range(start, end):
        x = delayed(fun_factor)(i)
        objects.append(x)

    z = delayed(sum)(objects)
    return z

def future_increment(c, start, end):
    # use fun_inc
    objects = []

    for i in range(start,end):
        x = c.submit(fun_inc, i)
        objects.append(x)

    z = c.submit(sum, objects)
    return z

def future_factor(c, start, end):
    # use fun_factor
    objects = []

    for i in range(start, end):
        x = c.submit(fun_factor, i)
        objects.append(x)

    z = c.submit(sum, objects)
    return z
