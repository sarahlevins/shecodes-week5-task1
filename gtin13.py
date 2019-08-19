def calculate_gtin13_barcode_check_digit(gtin):

    #turn string input into a list of integers
    GTIN_list = []
    for digit in range(len(gtin)):
        GTIN_list.append (int(gtin[digit]))

    # add multiples together and find out if it is divisible by 10
    remainder = sum(GTIN_list[0::2]+[i * 3 for i in GTIN_list[1::2]]) % 10

    #calculate check digit based on result
    if remainder == 0:
        check_digit = 0
    else:
        check_digit = 10 - remainder
    return str(check_digit)

def validate_gtin13_barcode_check_digit(gtin):

    #turn string input into a list of integers
    GTIN_list = []
    for digit in range(len(gtin)):
        GTIN_list.append (int(gtin[digit]))

    # add multiples together and find out if it is divisible by 10
    remainder = sum(GTIN_list[0:11:2]+[i * 3 for i in GTIN_list[1:12:2]]) % 10
    
    #calculate check digit based on result
    if remainder == 0:
        check_digit = 0
    else:
        check_digit = 10 - remainder
    
    print(check_digit)
    print(GTIN_list[12])

    #calculate check digit based on result
    if check_digit == GTIN_list[12]:
        return ('This is a valid gtin13 barcode.')
    else:
        return ('This is an invalid gtin13 barcode.')
