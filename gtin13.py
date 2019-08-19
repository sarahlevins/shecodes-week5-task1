GTIN = input('Enter your 13 digit GTIN product code: ')

#turn string input into a list of integers
GTIN_list = []
for a in GTIN:
    GTIN_list.append (int(a))

# add multiples together and find out if it is divisible by 10
remainder = sum(GTIN_list[1::2]+[i * 3 for i in GTIN_list[::2]]) % 10

#calculate check digit based on result
if remainder == 0:
    check_digit = 0
    print(f'check digit is {check_digit}')
else:
    check_digit = 10 - remainder
    print(f'check digit is {check_digit}')