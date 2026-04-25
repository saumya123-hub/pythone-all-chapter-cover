# 1+1/2+1/3+1/4+1/5+1/n
'''n = int(input("enter the number of the series"))
sum = 0
for i in range(1,n+1):
    a = 1.0/i
    sum = sum + a
print("sum of the serie is 1 + 1/2....1/:"+str(n),sum)
# 1+1/2ka square.........1/nka power2
n = int(input("enter the number "))
sum = 0
for i in range(1,n+1):
    a = 1.0/(i**2)
    sum = sum + a
print("sum of the series ",sum )
# sum of series 1/2+2/3+3/4+4/5+n/n+1
n = int(input("enter the number "))
sum = 0
for r in range(1,n+1):
    a = r/(r+1)
    sum = sum + a
print("sum of the series", sum)'''
# sum of the series 1/1+2kasqquare/2+3kasquare/3.......+nsquare/n
n = int(input("enter the number"))
s = 0
for i in range(1,n+1):
    a = float(i**i)/i
    s = s+a
print("sum of the series is",s)