numbers = input("Type a Number to Convert: ")
digit_to_words = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine",
    "10": "Ten",
    

}
output = ""
for number in numbers:
    output += digit_to_words.get(number, "...") + ""
print(output)