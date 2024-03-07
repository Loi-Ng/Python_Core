def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y

def exp(x, y):
    return x ** y

def div2(x, y):
    return x // y

if __name__ == "__main__":
    print("Nhap lan luot cac so a b : ", end="")
    a, b = [int(x) for x in input().split()]
    print(f"{a} + {b} = {add(a, b)}")
    print(f"{a} - {b} = {sub(a, b)}")
    print(f"{a} * {b} = {mul(a, b)}")
    print(f"{a} / {b} = {div(a, b)}")
    print(f'{a} // {b} = {div2(a, b)}')

