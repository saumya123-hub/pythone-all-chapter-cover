def exponent(x,y):
    if(y==0):
        return 1
    else:
        return (x*exponent(x,y-1))
x = int(input("enter the number of x"))
y = int(input("enter the number of y"))
print("the exeponent of the number",exponent(x,y))