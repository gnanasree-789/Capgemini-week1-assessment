number=int(input("Enter the number to generate the multiplication table"))
start_num=int(input("Enter the starting number: "))
last_num=int(input("Enter the end number: "));
for i in range(start_num,last_num+1):
    print(f"{number} x {i} = {number*i}")