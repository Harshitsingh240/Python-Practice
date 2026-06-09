# Write a commented program to print multiplication table.

# Ask the user for a number
num = int(input("Enter a number: "))

# print the multiplication table up to 10
for i in range(1,11):
    print(num,"x",i,"=",num*i)

    