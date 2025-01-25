sentence=input("Enter the Sentence: ")
list=list(sentence.split())
for str in list:
    c=list.count(str)
    print(f"The word {str} occurs {c} times")