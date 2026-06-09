# Write a program to display grade based on marks.

marks = int(input("enter marks: "))

if marks >= 90 :
    print("grade = A")
elif marks >= 75:
    print("grade = B")
elif marks >= 50:
    print("grade = C")
elif marks >= 30:
    print("grade = D")
else:
    print("grade = F")
