original_num = 12345  #orifinal number
reverse_num = 0    #reversed number

#Loop to reverse a number
while original_num != 0:                    #True unless original number is 0
    digit = original_num % 10               #contains the last digit of orginal number
    reverse_num = reverse_num*10 + digit    #Reversed of number with mulitple of digits places and adding another digit
    original_num //= 10                     #orignal number divided by 10

print(reverse_num)          #print the reversed number

