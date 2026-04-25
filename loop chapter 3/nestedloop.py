a = int(input("enter the number"))
for i in range(a):   
    for j in range(1,a+1):
        print(j,end=" ")
    print()

# asterisk print
n = int(input("enter the number"))
for i in range(n):
    for j in range(n+1):
        print("*",end="")
    print()
# print cube asterisk
n = int(input("enter the number"))
for i in range(n):
    for j in range(i):
        print("*",end="")
    print()
# print pyramid 1 22 33 44 55
n = int(input("enter the number"))
for i in range(n):
    for j in range(i):
        print(i,end="")
    print()
    # print pyramid 1 12 123 1234 
n = int(input("enter the number"))
for i in range( 1,n):
    for j in range( 1,i+1):
        print(j,end="")
    print()