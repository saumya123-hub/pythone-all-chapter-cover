a = int(input("enter the number "))
i = 1
sum = 0
while(i<=10):
    product = a*i
    sum = sum + product
    i = i+1
    print(product , end="\t")
print("sum of the table is",sum)