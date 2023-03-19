from os import *

print("Good Morning")
name = input("Please What is your name?\n")
system("cls")
gender = input("Gender?\n")
system("cls")
if gender == "Male":
    print("Hello Mr. " + name)
    print("These are the Services we can offer")
    print("1. 12 Hour PC use\n2. Gaming Lounge\n3. Laser Tag\n4. Boutique")
    decision = int(input("What will you like?\n"))
    system("cls")
    if decision == 1:
        print("We will have A PC ready for you...")
    if decision == 2:
        print("Let me escort you to the Gaming lounge")
    if decision == 3:
        print("Come and get your laser tag uniform")
    if decision == 4:
        print("What will you like to buy from the boutique?")

if gender == "Female":
    print("Hello Mrs. " + name)
    print("These are the Services we can offer\n")
    print("1. 12 Hour PC use\n2. Gaming Lounge\n3. Laser Tag\n4. Boutique")
    decision = int(input("What will you like?\n"))
    system("cls")
    if decision == 1:
        print("We will have A PC ready for you...")
    if decision == 2:
        print("Let me escort you to the Gaming lounge")
    if decision == 3:
        print("Come and get your laser tag uniform")
    if decision == 4:
        print("What will you like to buy from the boutique?")
