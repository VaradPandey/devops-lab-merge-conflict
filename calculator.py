def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    # Main Branch: Division with whole number integer check
    if b == 0:
        return "Division Error: Zero divisor encountered"
    res = a / b
    return int(res) if res.is_integer() else res

if __name__ == "__main__":
    print("=== Basic Calculator ===")
    print("10 + 5 =", add(10, 5))
    print("10 - 5 =", subtract(10, 5))
    print("10 * 5 =", multiply(10, 5))
    print("10 / 5 =", divide(10, 5))
