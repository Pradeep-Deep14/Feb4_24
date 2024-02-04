def calc(*args):
    count=len(args)
    elem=args[count-1]
    return count * elem
print(calc(2,2,1,3))