def calculate_isbn10_barcode_check_digit(barcode):
    
    barcode_list = []
    for digit in range(len(barcode)):
        barcode_list.append (int(barcode[digit]))
    print (barcode_list)

    w = 10
    sum_line = [i * w for i in barcode_list]
    print(sum_line)

print(calculate_isbn10_barcode_check_digit('188879997'))


# def validate_isbn10_barcode_check_digit(barcode)

# print(validate_isbn10_barcode_check_digit('1888799978'))