age = int(input("enter the age of the person"))
if age>=18:
    print("you are eligible for vote :")
else:
    years_left = 18 - age
    print("you are not eligible for vote: ")
    print("you can vote after ", years_left,"years")