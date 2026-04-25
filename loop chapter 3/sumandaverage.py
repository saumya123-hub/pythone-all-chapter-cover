n = int(input("enter the number"))
i = 0
s = 0
while(i<=n):
 s = s+i
 i = i+1
average = float(s)/(n+1)
print("sum of number is", s)
print("average of the number",average)