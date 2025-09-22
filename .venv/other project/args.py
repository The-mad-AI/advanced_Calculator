def skyline(*args):
    if not(args):
        return 0
    return max(args)
    
print(skyline(3, 7, 15, 2, 9))
print(skyline(1, 1 ,1 ,1))