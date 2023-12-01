def entrance_points(*args):
    ex_it = []
    for i in args:
        ex_it.append('.' *i)
    return ex_it
a = entrance_points(1,2,3)
print(a)
