weight=int(input("Enter the weight in KG: "))
height=int(input("Enter the height in meter: "))
BMI=weight/(height*height)
print(f"BMI value is: {BMI}")
if BMI < 18.5:
    print("Category: Under Weight")
elif BMI>=18.5 and BMI <=24.9:
    print("Category: Normal")
elif BMI>=25 and BMI <=29.9:
    print("Category: Over Weight")
elif BMI>=30 and BMI<=35.9:
    print("Category: Obese")