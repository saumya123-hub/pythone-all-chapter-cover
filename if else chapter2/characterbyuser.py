char = input("pree any key :")
if (char.isalpha()):
    print("the user enter the character")
elif (char.isdigit()):
    print("the user enter the digit")
elif (char.isspace()):
   print("the user enter the space bar") 
else:
    print("special character")