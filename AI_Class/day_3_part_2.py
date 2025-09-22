
def largest_fibonacci_less_than(x):
    a, b = 0, 1
    while b < x:
        a, b = b, a+b
        return a


x = 50
result = largest_fibonacci_less_than(x)
print("largest_fibonacci_less_than", x, ":", result)


def fibonacci_less_than(x):
    a, b = 0, 1
    fib_list = []
    while a < x:
        fib_list.append(a)
        a, b = b, a+b
    return fib_list


x = 50
result = fibonacci_less_than(x)
print(f"fibonacci_less_than {x} : {result}")


def even_fibonacci_less_than(x):
    a, b = 0, 1
    even_fib_list = []
    while a < x:
        if a % 2 == 0:
            even_fib_list.append(a)
        a, b = b, a+b
    return even_fib_list


x = 50
result = even_fibonacci_less_than(x)
print(f"even_fibonacci_less_than{x}:{result}")


def fibonacci_between(a, b):
    fib_list = []
    x, y = 0, 1
    while x <= b:
        if x >= a:
            fib_list.append(x)
        x, y = y, x+y
    return fib_list


a = 10
b = 50
result = fibonacci_between(a, b)
print(result)
