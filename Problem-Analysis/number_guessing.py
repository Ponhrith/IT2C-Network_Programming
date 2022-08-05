import random as rand
generate_num = rand.randint(1, 100)

i = 5
for number in range(5):
    user_num = int(input("Select the numnber between 1 and 100. You have "+ str(i)+" guesses left."))
    if generate_num == user_num:
        print("Well done!")
        exit()
    elif generate_num < user_num:
        print('Your number is too large!')
        i -= 1
    elif generate_num > user_num:
        print('Your number is too small!')
        i -= 1 
print('You\'re out of guesses! You lose!')