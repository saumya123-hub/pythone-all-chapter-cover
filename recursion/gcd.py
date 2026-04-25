def gcd(m,n):
    res = m%n
    if(res==0):
        return n
    else:
        return gcd(n , res)
m = int(input("enter the number of m"))
n = int(input("enter the number of n"))
print("the gcd of number is",gcd(m,n))