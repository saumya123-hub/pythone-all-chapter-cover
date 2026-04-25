def relation(a,b):
    if(a==b):
        return 0
    if(a>b):
        return 1
    if(a<b):
        return -1
a = int(input("enter the number of a "))
b = int(input("enter the number of b"))
res = relation(a,b)
if(res==0):
    print("a equal to b")
if(res==1):
    print("a is greater then b")
if(res==-1):
    print("a is less than b")