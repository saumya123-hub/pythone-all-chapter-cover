a = float(input("enter the number of a"))
b = float(input("enter the number of b"))
c = float(input("enter the number of c"))
print(a,b,c)
s = (a+b+c)/2
area = (s*(s-a)*(s-b)*(s-c))**0.5
print("area of triange by using heron formula",area)  