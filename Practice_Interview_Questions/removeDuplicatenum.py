numbers = [1,1,3,3,7,6,3,4,6,7]
sole_numbers = []

for number in numbers:
    if number not in sole_numbers:
        sole_numbers.append(number)
        
print(sole_numbers)