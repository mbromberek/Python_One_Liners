## Dependencies 
import re

## Data
inputs = ['18:29', '23:55', '123', 'ab:de', '18:299', '99:99']

## One-liner
input_ok = lambda x : re.fullmatch('[0-9]{2}:[0-9]{2}', x) != None

for x in inputs:
    print(input_ok(x))

'''
Output:
True
True
False
False
False
True
'''

print('\n')

input_ok_2 = lambda x : re.fullmatch('([01][0-9]|[2][0-3]):[0-5][0-9]', x) != None
for x in inputs:
    print(input_ok_2(x))
'''
Output:
True
True
False
False
False
False
'''
