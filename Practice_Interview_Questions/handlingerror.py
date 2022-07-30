try:
    age1 = int(input("What is your Age?"))
    age2 = int(input("What is your Frined's Age?"))
    average = age1 / age2
    print(average)

except ZeroDivisionError:
    print("Age cannot be Zero")
   
except ValueError:
    print("Invalid Value")