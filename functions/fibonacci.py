def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError('Fibonacci numbers cannot be negative')
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)