num = int(input('Enter a number: '))

while num != 0:
    remainder = num % 10
    if(remainder!=0 and remainder !=1):
        print('Number is not in binary representation!')
        break
    number = number //10
    if(number==0):
        print('Number is in binary representation')