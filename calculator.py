def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # Feature Branch: Precision division with rounding to 4 decimal places
    if b == 0:
        raise ZeroDivisionError("Error: Division by zero is not allowed.")
    return round(a / b, 4)

if __name__ == "__main__":
    print("=== Basic Calculator ===")
    print("10 + 5 =", add(10, 5))
    print("10 - 5 =", subtract(10, 5))
    print("10 * 5 =", multiply(10, 5))
    print("10 / 5 =", divide(10, 5))
