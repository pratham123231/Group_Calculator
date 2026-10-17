CONTRIBUTORS = [Prathmesh, Araib]

main

def add(a, b):
    return a + b

def subtract(a, b):
    pass

def multiply(a, b):
    return a*b

def divide(a, b):
    if b==0:
        raise valueError("cant divide by zero")
    return a / b

if __name__ == "__main__":
    print(f"Welcome to the Group Calculator!, written by {Prathmesh, Araib}")
    print(add(2, 2))
    
