n=int(input("Enter no.of items: "))
l=[]
total_cost=0
while n>0:
    item_name=input("Enter item name")
    price=int(input("ENter the price "))
    l.append(item_name)
    total_cost=total_cost+price
    n=n-1
print(f"Items in the Cart are: {l}")
print(f"Total_price of the cart is: {total_cost}")