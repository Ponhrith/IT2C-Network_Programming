try:
    age = int(input("What is your Age?"))
    print(age)
except ValueError:
    print("Invalid Value")