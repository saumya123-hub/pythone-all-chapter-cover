a = 20
i = 1
while i >= a:
    print("hello", end=" ")
    i = i + 1

#print("hello" "\t" *100)

i = 0
while(i<=100):
    print(i, end="  ")
    i=i+1

i= 100
while(i>=0):
    print(i,end="  ")
    i=i-1 
a = int(input("enter the number of table"))
i = 1
while(i<=20):
    print(a*i ,end="  ")
    i = i+1
i = 1
while i <= 10:
    print(i * i, end=" ")
    i = i + 1
i = 1
while i<=10 :
    print(i , end="  ")
    if(i==5):
        break
    i=i+1
print(" \nend of loop")
i = 0
while (i <= 10):
    if (i == 5):
        i = i + 1
        continue
    print(i, end="  ")
    i = i + 1

print("\nend of loop")
nums = [1,2,3,4,5,6,7,8,9]
for val in nums:
    print(val , end="  ")



