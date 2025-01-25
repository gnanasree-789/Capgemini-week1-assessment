while True:
    user_input=input("Enter the String or a number: ")
    rev=user_input[::-1]
    if user_input == rev:
        print(f"{user_input} is Palindrome")
    else:
        print(f"{user_input} is not palindrome")