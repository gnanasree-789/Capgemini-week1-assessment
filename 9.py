string=input("Enter the string: ")
list=list(string)
vowels=consonants=digits=special_characters=0
for i in list:
    if i.lower() in ('a','e','i','o','u'):
        vowels=vowels+1
    elif i.lower() in ('b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z'):
        consonants=consonants+1
    elif i=='0' or i=='1' or  i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9':
        digits=digits+1
    else:
        special_characters=special_characters+1
print(f"No.of vowels in given string: {vowels}")
print(f"No.of Consonants in given string: {consonants}")
print(f"No.of digits in given string: {digits}")
print(f"No.of special characters in given string: {special_characters}")
reverse_str=string[::-1]
print(f"Reversed String is : {reverse_str}")