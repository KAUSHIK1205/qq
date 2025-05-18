def multiply_once(n, m):
    result = 1
    for i in range(n, m + 1):
        result *= i
    return result

def multiply_n_iterations(n, m):
    result = 1
    for _ in range(n):  # Run n iterations
        for i in range(n, m + 1):
            result *= i
    return result

# Example usage
n = 2
m = 5
print("Multiplication in one iteration:", multiply_once(n, m))
print("Multiplication in n iterations:", multiply_n_iterations(n, m))