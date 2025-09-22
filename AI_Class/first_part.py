
def intrativ_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n+1):
        a, b = b, a+b
    return b


print(intrativ_fibonacci(50))


def fibonacci_sequence(n):
    sequence = [0, 1]
    for i in range(2, n):
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    return sequence


print(fibonacci_sequence(10))


def fibonacci_memoization(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    elif n == 1:
        return 1
    memo[n] = fibonacci_memoization(
        n-1, memo) + fibonacci_memoization(n-2, memo)
    return memo[n]


print(fibonacci_memoization(10))
print(fibonacci_memoization(50))


def fibonacci_even(n):
    sequence = [0, 1]
    for i in range(2, n):
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)
    even_numbers = [num for num in sequence if num % 2 == 0]
    return even_numbers


even_sum = sum(fibonacci_even(15))
print(even_sum)


print(fibonacci_even(10))
print(fibonacci_even(15))
