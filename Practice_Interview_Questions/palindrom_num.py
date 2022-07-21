num = 1221
temp = num
reverse_num = 0
while num!=0:
    remainder = num % 10
    reverse_num = reverse_num * 10 + remainder 
    num = num // 10
     
if temp == reverse_num:
    print('True')
else:
    print('False')