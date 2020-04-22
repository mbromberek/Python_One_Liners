import re

s = 'helloworld'

regex_1 = 'hello(world)'
regex_2 = '(hello(world))'

print(re.findall(regex_1, s))
# ['world']

print(re.findall(regex_2, s))
# [('helloworld', 'world')]
