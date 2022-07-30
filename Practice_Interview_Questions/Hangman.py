import random
print("Hangman")
print("Category: Geography | Type: Continents")
continents = ("North America", "South America", "Europe", "Antartica", "Asia", "Africa", "Oceania")
secret_word = random.choice(continents)
losing_number = 0
guess_count = 5
word = "Word:" + "_" *len(secret_word)
print(word)

while guess_count > losing_number:
    guess = input("Guess the Word: ").title()
    guess_count -= 1
    print(f"Guess Left: {guess_count}")
    if guess == secret_word:
        print("You Won the Game!")
        break
    elif guess != secret_word:
        print("Wrong Guess!")
        
else:
    print("Sorry, you lost the game!")
    print("The word was" + secret_word)