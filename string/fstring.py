sen = "Hey my name is {} and i am a programmer and i am from {}"
name = "saumya gupta"
country = "India"
print(sen.format(name,country))
print(sen.format(country,name))
print(f"Hey my name is {name} and i am a programmer and i am from {country}")
print(f"Hey my name is {{name}} and i am a programmer and i am from {{country}}")

# docstrings 
def square(n):
    return n**2
print(square(5))

def power(n, m):
    '''Take in anumber n, return the power of n'''
    print(n**m)
power(2,3)
print(power.__doc__)
#   pep 8 import this
