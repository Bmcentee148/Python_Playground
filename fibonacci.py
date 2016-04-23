# Multiple assignment to compute the fibonacci sequence
# @ author Brian McEntee

def fib(max_num) :

    a, b = 0, 1
    while b < max_num :
        print b, 
        a, b = b, a + b

def main() :
    fib(100)

if __name__ == "__main__" :
    main()