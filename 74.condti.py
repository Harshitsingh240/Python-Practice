 # Write a program using nested if.

age = int(input("enter you age:"))

if age >= 18:
    print("you are a eligible to vote ")

    if age >= 65:
        print("you are senior citizen. ")
    else:
        print("you are not a senior citizen. ")
else:
    print("you are not elgible to vote. ")
