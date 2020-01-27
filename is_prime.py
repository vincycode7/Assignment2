input_ = int(input('Enter a number: '))

upper_range = input_+1 if input_ < 10 else 10
lower_range = 2
is_prime = False

if input_ == 0 or input_ == 1:
        print('not prime')
else:
    for divisor in range(lower_range,upper_range):
        if divisor == 1:
            continue
        if divisor == upper_range-1:
            print(' is prime')
        elif input_ % divisor == 0 and divisor != input_:
            print('not prime')
            break