a = (input("enter the number "))
print(f"multiplication of the tbale of {a} is:")
try:
    for i in range(1,11):
        print(f"{int(a)} x {i} = {int(a)*i}")
except:
    print("invalid inpute")
print("some imp lines of codes")
print("end of the program")