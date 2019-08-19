# GTIN-13 check digits are calculated as follows:

# 1. Multiply every second digit by 3, and every other digit by 1.
# 2. Add up all the multiplied numbers.
# 3. You can now get the check digit by working out what number would have to be added to the sum in 
# order to bring it up to a multiple of 10. If the number is already a multiple of 10, the check digit is 0.

GTIN = input('Enter your 13 digit GTIN product code: ')

GTIN_list = []

for a in GTIN:
    GTIN_list.append (int(a))

times_one = GTIN_list[1::2]
times_three = [i * 3 for i in GTIN_list[::2]]

total = sum(times_one+times_three)

print(total)
remainder = total % 10

if remainder == 0:
    check_digit = 0
    print(f'check digit is {check_digit}')
else:
    check_digit = 10 - remainder
    print(f'check digit is {check_digit}')

