num=int(input("Enter the number: "))
if(num<0):
    print("Error!, Negative numbers are not considered")
else:
    factorial=1
    for i in range(1,num+1):
        factorial=factorial*i
    print(f"The factorial of a number {num} is {factorial}")