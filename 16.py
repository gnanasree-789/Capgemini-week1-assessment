numbers=input("Enter the list of numbers: ")
list=list(map(int,numbers.split()))
print(f"The list is {list}")
even=[]
odd=[]
for num in list:
    if num%2 == 0:
        even.append(num)
    else:
        odd.append(num)
print(f"Even numbers List: {even}")
print(f"Odd numbers List: {odd}")