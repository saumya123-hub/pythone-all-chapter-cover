i=0
sum=0
while(i<=10):
    print(i , end="  ")
    sum = sum+i
    i+=1
    average = float(sum)/10
print("\nsum of two number",sum)
print("average of the two number",average)
# 20 horiz0ntal asterisks(*)
i= 0
while(i<=20):
    print("*",end="")
    i+=1
# sum of number m to n
print("\n")
m = int(input("enter the number of m"))
n = int(input("enter the number of n"))
i = m
sum = 0
while(i<=n):
    print(i , end=" ")
    sum = sum+i
    i+=1
print("sum of number from m to n", sum)
# program to encounted -1 and also count positive , negative, zeros
pos = 0
neg = 0
zero = 0
while True:
    a = int(input("Enter number : "))

    if a == -1:
        break
    elif a > 0:
        pos += 1
    elif a < 0:
        neg += 1
    elif a==0:
        zero+=1

print("Positive numbers:", pos)
print("Negative numbers:", neg)
print("zero number",zero)
# armstorng number hai ya nahi
a = int(input("enter the number :"))
sum = 0
num = a
while(a>0):
    r = a%10
    sum = sum+(r**3)
    a = a//10
if(sum ==num):
    print("the number is armstrong")
else:
    print("the number is not armstrong")
