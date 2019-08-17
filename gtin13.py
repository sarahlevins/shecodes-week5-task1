# GTIN-13 check digits are calculated as follows:

# 1. Multiply every second digit by 3, and every other digit by 1.
# 2. Add up all the multiplied numbers.
# 3. You can now get the check digit by working out what number would have to be added to the sum in 
# order to bring it up to a multiple of 10. If the number is already a multiple of 10, the check digit is 0.

GTIN = int(input('Enter your 13 digit GTIN product code: '))
GTIN_list = []

for a in GTIN:
    GTIN_list.append (a)

print(GTIN_list)

times_three = GTIN_list[::2]

print(times_three)

x = 0
for a in times_three:
    times_three[x] = a * 3
    x += 1


print(times_three)