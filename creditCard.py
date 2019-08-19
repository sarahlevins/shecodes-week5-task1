    #turn string input into a list of integers
def calculate_credit_card_number_check_digit(ccnum):   
    credit_list = []
    for digit in range(len(ccnum)):
        credit_list.append (int(ccnum[digit]))
    print (credit_list)

    times_one_list = credit_list[-2::-2]
    print (sum(times_one_list))

    times_two_list = [i * 2 for i in credit_list[-1::-2]]
    print(times_two_list)

    for number in times_two_list:
        if number >= 10:
            print (number)
            number_one = number // 10
            number_two = number - number_one * 10
            number = number_one + number_two
            print(number)
    print (times_two_list)


calculate_credit_card_number_check_digit('542418027979176')




