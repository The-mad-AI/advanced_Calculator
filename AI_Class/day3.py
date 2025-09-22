def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a+b
    return b


fib_sequence = [fibonacci(i) for i in range(10)]
even_numbers = [num for num in fib_sequence if num % 2 == 0]
odd_numbers = [num for num in fib_sequence if num % 2 != 0]
total_sum = sum(fib_sequence)
even_numbers = len(even_numbers)
odd_numbers = len(odd_numbers)


print(fib_sequence)
print(even_numbers)
print(odd_numbers)
print(total_sum)

