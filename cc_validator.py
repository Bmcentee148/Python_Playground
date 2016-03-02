# This will ask the user for a credit card number and check the validity
# of the card number using a checksum

# Method Declarations
def get_digits(string_of_digits) :
    digits = []
    for s in string_of_digits : 
        digits.append(int(s))
    print "Digits: ", digits #REMOVE LATER -- TESTING PURPOSES
    return digits

def luhn_checksum(digits) :
    for i in range(0,len(digits),2) :
        digits[i] *= 2
        if digits[i] > 9 :
            digit_sum = (digits[i] // 10) + (digits[i] % 10)
            digits[i] = digit_sum
    print "Fixed Digits: ", digits #REMOVE LATER -- TESTING PURPOSES
    checksum = 0
    for d in digits :
        checksum += d
    print "Checksum: ", checksum #REMOVE LATER -- TESTING PURPOSES
    return checksum

def is_valid_checksum(checksum) :
    if checksum % 10 == 0 :
        return True
    else :
        return False

# Script 
print "Please enter a valid credit card number."
cc_string = raw_input('> ')

cc_digits = get_digits(cc_string)
checksum = luhn_checksum(cc_digits)

if is_valid_checksum(checksum) :
    print "Thank you, the credit card you have entered is valid."
    exit(0)
else :
    print "Error: Invalid Credit Card Number"
    exit(1)



