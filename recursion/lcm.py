def lcm(a,b,n):
    if n%a==0 and n%b==0:
        return n
    else:
        return lcm(a,b,n+1)
a = int(input("enter the number of a"))
b = int(input("enter the number of b"))
print("the lcm of the number :",lcm(a,b,max(a,b)))