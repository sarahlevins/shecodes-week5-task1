def calculate_credit_card_number_check_digit(ccnum):   
    credit_list = []
    for digit in range(len(ccnum)):
        credit_list.append (int(ccnum[digit]))

    times_one_list = credit_list[-2::-2]

    times_two_list = [i * 2 for i in credit_list[-1::-2]]

    times_two_count = 0
    for number in times_two_list:
        if number >= 10:
            times_two_list [times_two_count] = number - 9
            times_two_count += 1
        else:
            times_two_count += 1

    return str((((sum(times_two_list) + sum(times_one_list)) * 9) % 10))

def validate_credit_card_number_check_digit(ccnum):
    credit_list = []
    for digit in range(len(ccnum)):
        credit_list.append (int(ccnum[digit]))

    times_one_list = credit_list[-1::-2]
    times_two_list = [i * 2 for i in credit_list[-2::-2]]

    times_two_count = 0
    for number in times_two_list:
        if number >= 10:
            times_two_list [times_two_count] = number - 9
            times_two_count += 1
        else:
            times_two_count += 1
    if (sum(times_one_list) + sum (times_two_list)) % 10 == 0:
        return ('This is a valid credit card number.')
    else:
        return ('This is an invalid credit card number.')

# calculate_credit_card_number_check_digit('542418027979176')
# validate_credit_card_number_check_digit('5424180279791762')




