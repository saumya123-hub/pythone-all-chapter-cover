a = int(input("Enter the number: "))
sum = 0

for n in range(20, a + 1):
    if n > 20:
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                break
        
        else:
            print(n , end="  ")
            sum += n

print("\nSum of prime numbers:", sum)