numbers=input("Enter the list numbers: ")
list=list(map(int,numbers.split()))
print(f"The List is {list}")
list.sort(reverse=True)
print(f"The Second largest Element in the given list: {list[1]}")