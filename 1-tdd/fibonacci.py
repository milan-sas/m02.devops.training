# define your solution
def fibonacci(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n <= 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

