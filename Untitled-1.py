user=input("Enter the desired word:").lower()
if user==user[::-1]:
    print("Yes")
else :
    print("No")