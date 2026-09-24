def fib_fast_doubling(n):
    """
    Efficiently compute the nth Fibonacci number using fast doubling.
    Time Complexity: O(log n)
    """
    def helper(n):
        if n == 0:
            return (0, 1)
        else:
            a, b = helper(n // 2)
            c = a * (2 * b - a)
            d = a * a + b * b
            if n % 2 == 0:
                return (c, d)
            else:
                return (d, c + d)
    return helper(n)[0]


# Example usage
if __name__ == "__main__":
    n = 50
    print(f"Fibonacci({n}) = {fib_fast_doubling(n)}")
