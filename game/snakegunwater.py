import random
computer=random.choice([1,-1,0])
you_choose = input("enter your choice :")
u_dict={"s":1,"w":-1,"g":0}
rev_dict={1:"snake",-1:"water",0:"gun"}
u = u_dict[you_choose]
print(f"you choose{rev_dict[u]}\n computer choose{rev_dict[computer]}")
if (computer == u):
    print("game draw")
else:
    if((computer-u == -1) or (computer-u==2)):
        print("you lose!")
    else:
        print("you win")

