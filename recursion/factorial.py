def fact(n):
    if(n<=0): return 1
    return n*fact(n-1)
n = int(input("enter the number of n"))
factorial = fact(n)
print("factorial of the number :",factorial)

import datetime
now =datetime.datetime.now()
print(now.strftime("%a %d %H: %M: %S IST %Y " ) )