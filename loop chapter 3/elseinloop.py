for i in range(5):
    print(i)
else:
    print("Sorry no i")

for i in []:
    print(i)
else:
    print("Sorry no i")
#  break karne par else wala code excute nahi hota hai
for i in range(5):
    print(i)
    if i == 4:
        break
else:
    print("Sorry no i")
i = 0
while(i<=6):
    i=i+1
    # if i==4:
    #     break
else:
    print("sorry no i")