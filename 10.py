Total_bill_amount=int(input("ENter the total bill amount: "))
number_of_people=int(input("Enter no.of people: "))
tip_percentage=int(input("Enter tip percentage: "))
percent_to_amount=tip_percentage*Total_bill_amount/100
present_bill_amount=Total_bill_amount+percent_to_amount
amou_for_each_person=present_bill_amount/number_of_people
print(f"Amount each person to pay: {amou_for_each_person}")