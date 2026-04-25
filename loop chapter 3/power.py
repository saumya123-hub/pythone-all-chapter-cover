# power of te number
x = int(input("enter the number"))
a = int(input("till the power of x"))
result = 1
for i in range(a):
    result = result*x
print(x,"to the power of",a,"is",result)

   # leap year between the number
print("leap year from the 1900-2101 are:")
for i in range(1900,2101):
    if(i%4==0):
        print(i,end="  ")

