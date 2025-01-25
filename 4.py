student_name=input("Enter the student name: ")
sub1=int(input("Enter subject1 marks out of 100: "))
sub2=int(input("Enter subject1 marks out of 100: "))
sub3=int(input("Enter subject1 marks out of 100: "))
sub4=int(input("Enter subject1 marks out of 100: "))
sub5=int(input("Enter subject1 marks out of 100: "))
total_marks=sub1+sub2+sub3+sub4+sub5
percentage=((sub1+sub2+sub3+sub4+sub5)/500)*100
print(f"Total marks of the {student_name} is {total_marks}")
print(f"Percentage of the {student_name} is {percentage}")
if percentage <=100 and percentage>=90:
    print("Grade is A")
elif percentage <90 and percentage>=80:
    print("Grade is B")
elif percentage <80 and percentage>=60:
    print("Grade is C")
else:
    print("Fail")