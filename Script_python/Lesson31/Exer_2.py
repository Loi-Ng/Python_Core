def find_gcd( A:int, B:int ):
    """
    Buoc 1: Neu A > B. Dat A = A - B cho toi khi A < B 
    Buoc 2: Khi A < B. Doi cho A va B roi lap lai buoc 1 cho toi khi A = B
    Buoc 3: Khi A = B. return A hoac B
    """
    if (A == 0):
        return B
    
    elif (B == 0):
        return A
    
    else:
        while( A != B ):
            if ( A > B):
                A -= B
                
            else:
                B -= A
                
        return A
    
def gcd_euclid_dequi( A:int, B:int ):
    if (B == 0):
        return A
    else:
        return gcd_euclid_dequi( A = B, B = A % B)
    
def gcd_euclid_ko_dequi( A:int, B:int):
    tmp = None
    while( B != 0):
        tmp = A % B
        A = B
        B = tmp
    
    return A
        
def lcm(A:int, B:int, gcd):
    return A*B // gcd(A, B)

if __name__ == "__main__":
    print("Nhap 2 so nguyen : ", end= " ")
    a, b = [int (x) for x in input().split()]
    
    print(gcd_euclid_ko_dequi(A = a,B = b))
    
    print(lcm(A = a, B= b, gcd= gcd_euclid_ko_dequi))
    
    
    
        