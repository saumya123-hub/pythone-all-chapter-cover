# sum and average of the number

n = int(input("enter the number"))
sum = 0
average = 0
for i in range(1,n+1):
    sum = sum+i
    print(i,end=" ")
print("\nsum of the number",sum)
average = float(sum)/i
print("avarage of the number", average)
          # table of the number and sum
print("\n")
n = int(input("enter the number :"))
sum = 0
for i in range(1,11):
    product= n*i
    sum = sum+product
    print(product,end="  ")
print("\nsum of the table is:",sum)

