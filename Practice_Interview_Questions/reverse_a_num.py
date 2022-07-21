num = 123457
reverse_num = 0
while num!=0:

    remainder = num % 10
    reverse_num = reverse_num * 10 + remainder 
    num = num // 10    # decrase one index
        
print(reverse_num)