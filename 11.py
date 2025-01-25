password=input("ENter the password")
passwordlis=list(password)
c1=c2=c3=c4=0
for ch in passwordlis:
    if 'a' <= ch <= 'z':
        c1=c1+1
    elif 'A' <= ch <= 'Z':
        c2=c2+1
    elif '0'<= ch <='9':
        c3=c3+1
    else:
        c4=c4+1
if c1>=1 and c2>=1 and c3>=1 and c4>=1 and len(password)>=8:
    print("Password is Strong")
else:
    print("Password is Weak")