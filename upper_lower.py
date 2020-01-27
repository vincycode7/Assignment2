#read in input from user
input_ = input('Enter String of Alphabets: ')

upper_count = 0
lower_count = 0
not_alpha_count = 0
g = 'F'
print(g.isupper())
for each in input_:
    print(each)
    if each.isupper():
        upper_count += 1
    elif each.islower():
        lower_count += 1
    else:
        not_alpha_count += 1
print(f'Len of string: {len(input_)}')
print(f'Upper Count: {upper_count}')
print(f'LLower Count: {lower_count}')
print(f'Not Alpa Cont: {not_alpha_count}')

