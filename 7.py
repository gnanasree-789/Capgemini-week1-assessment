salary=int(input("Enter your salary: "))
age=int(input("Enter your age: "))
credit_score=int(input("ENter your credit_score: "))
if(salary<=20000 and age>18 and credit_score>=30):
    print("Loan Approval")
elif(salary >20000):
    print("Rejected beacause of salary")
elif(age<=18):
    print("Rejected beacause of minor age")
elif(credit_score<30):
    print("Rejected beacause of credit score")