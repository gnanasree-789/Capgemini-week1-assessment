def is_prime(num):
    if num<=1:
        return False
    for i in range(2,num):
        if num%i == 0:
            return False
    return True
num1=int(input("Enter the number where to start the prime number: "))
num2=int(input("Enter the number where to end the prime number"))
for num in range(num1,num2+1):
    if is_prime(num):
        print(num,end=" ")