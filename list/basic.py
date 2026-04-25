a = [1,2,3,4,5,6,7,9,"saumya",True]
print(a)
print(type(a))
print(a[0])
print(a[1])
print(a[3])
print(a[4])
print(a[5])
print(a[6])
print(a[7])
print(a[8])
print(a[9])
print(len(a))
print(a[-1])
if 12 in a:
    print("no")
else:
    print("no")
print(a)
print(a[1:-1])
print(a[1:9])
print(a[1:9:2])
list = [i for i in range(8)]
print(list)
list = [i*i for i in range(8) if i%2==0]
print(list)