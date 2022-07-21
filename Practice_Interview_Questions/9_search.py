array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
type = int(input("Type a number: "))

for i in range(len(array)):
    if i == type:
        print("True")
    else:
        print("False")        
        