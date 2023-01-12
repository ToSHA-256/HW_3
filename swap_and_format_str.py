print('Enter 2 words:')
input_str = input()
split_str = input_str.split(' ')
if len(split_str) == 2:
    split_str[0], split_str[1] = split_str[1], split_str[0]
    format_str = ' '.join(split_str).replace(' ', ' ! ')
    print('!{}!'.format(format_str))    # option 1
    print('!{0}!'.format(format_str))   # option 1,5
    print(f'!{format_str}!')            # option 2
    print('!'+format_str+'!')           # option 3
else:
    print('Check input data!')
