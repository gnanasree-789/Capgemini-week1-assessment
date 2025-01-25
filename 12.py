num = int(input("Enter Number:"))
for i in range(0,num):
    for j in range(0,i+1):
        print("*", end="")
    print()
def print_reverse_pattern(num):
    for i in range(num,0,-1):
        print('*' * i)
inp=input("If you want to reverse the pattern(yes/no): ")
if inp == 'yes':
    print_reverse_pattern(num)
else:
    None