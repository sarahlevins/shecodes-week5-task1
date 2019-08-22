def calculate_gtin13_barcode_check_digit(gtin):

    #turn string input into a list of integers
    GTIN_list = []
    for digit in range(len(gtin)):
        GTIN_list.append (int(gtin[digit]))

    # add multiples together and find out remainder when divisible by 10
    remainder = sum(GTIN_list[0::2]+[i * 3 for i in GTIN_list[1::2]]) % 10

    #calculate check digit based on result
    if remainder == 0:
        check_digit = 0
    else:
        check_digit = 10 - remainder
    return str(check_digit)

def validate_gtin13_barcode_check_digit(gtin):
    #calculate check digit based on result
    if calculate_gtin13_barcode_check_digit(gtin) == gtin[12]:
        return ('This is a valid gtin13 barcode.')
    else:
        return ('This is an invalid gtin13 barcode.')
