def sum_digits(n):
    s = 0
    
    if n < 0:
        n = n *(-1)
        
    while ( n > 0):
        s += n % 10
        n = n // 10
    
    return s
    

def mul_digits(n):
    s = 1
    
    if (n < 0):
        n = n * (-1)
        
    while (n > 0):
        s *= n % 10
        n = n // 10
        
    return s

def first_num(n):
    while (n > 10):
        n = n // 10
    return n
    
if __name__ == "__main__":
    print(first_num(12345))
                 