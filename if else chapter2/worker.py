ch = input("enter the sex of the employee (m or f):")
salary = float(input("enter the salary of the employee :"))
if ch == 'm':
    bonus = salary*0.05
    amt_to_be_paid = bonus+salary
    if salary < 10000:
        bonus = bonus + (salary*0.02)
else:
    bonus = salary*0.10
    amt_to_be_paid = bonus+salary
    if salary < 10000:
            bonus = bonus+(salary*0.02)
            print("salary =",salary)
            print("bonus",bonus)
            print("*****************************************************")
            print("final salary of the employ: ",amt_to_be_paid)
            
