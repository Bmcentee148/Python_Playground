# This will calculate the "Shannon entropy" of the given input string, and 
# output there values in the order the input was given.
#            n
#            _   count(i)          count(i)
#H(X) = -1 * >   --------- * log  (--------)
#            -       N          2      N
#            i=1
# 
# USE FOR COMPUTING LOG -> math.log(x[, base])

from math import log

def num_occurences(char , char_seq) :
    count = 0
    for c in char_seq :
        if c == char :
            count += 1
    return count

def shannon_entropy(char_seq) :
    """ Calculate the Shannon entropy of a string of characters."""
    n = len(char_seq)
    sum = 0
    # Loop through each character for the summation
    while char_seq :
        curr_char = char_seq[0]
        char_count = num_occurences(curr_char,char_seq)
        new_seq = [c for c in char_seq if (c != curr_char)]
        char_seq = new_seq
        sum += ( ((float(char_count)) / n) * log((float(char_count) / n), 2) )
    return -sum


def main() :
    s1 = "1223334444"
    s2 = "Hello, world!"
    s3 = ""
    s4 = "122333444455555666666777777788888888"
    s5 = "563881467447538846567288767728553786"
    s6 = "https://www.reddit.com/r/dailyprogrammer"
    s7 = "int main(int argc, char *argv[])"

    inputs = [s1, s2, s3, s4, s5, s6, s7]
    dec_formatter = "%.5f"
    for s in inputs :
        print dec_formatter % shannon_entropy(s)
    

if __name__ == "__main__" :
    main()
