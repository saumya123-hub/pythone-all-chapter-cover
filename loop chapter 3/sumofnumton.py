m = int(input("enter the number of m: "))
n = int(input("enter the number of n: "))

i = m
sum = 0

while(i <= n):
    print(i, end="  ")
    sum = sum + i
    i = i + 1
print("\nSUM =", sum)