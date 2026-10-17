CONTRIBUTORS = [seemal]
CONTRIBUTORS = [Prathmesh]

def add(a, b):
    pass

def subtract(a, b):
    return a-b

def multiply(a, b):
    return a*b

def divide(a, b):
    if b==0:
        raise valueError("cant divide by zero")
    return a / b

if __name__ == "__main__":
    print(f"Welcome to the Group Calculator!, written by {seemal}")
    print(f"Welcome to the Group Calculator!, written by {Prathmesh}")
    print(add(2, 2))
    print(subtract(5,3))
