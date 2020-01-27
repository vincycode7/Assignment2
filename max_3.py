input1, input2, input3 = input('Enter Three Digits Seperated By space e.g (23 6 8): ').split(' ')
input_  = [int(input1), int(input2), int(input3)]

print(f'Max of {input1} {input2} {input3} is {max(input_)}')