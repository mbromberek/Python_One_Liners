## dependencies
import re

## Data
report = '''
If you invested $1 in the year 1801, you would have $18087791.41 today. 
This is a 7.967% return on investment.
But if you invested only $0.25 in 1801, you would end up with $4521947.8525. 
'''

## My try
result = re.findall('(\$[0-9]+(\.[0-9]*)*)', report)
print(result)
# [('$1', ''), ('$18087791.41', '.41'), ('$0.25', '.25'), ('$4521947.85', '.85')]

## One-liner
dollars = [x[0] for x in re.findall('(\$[0-9]+(\.[0-9]*)?)', report)]
'''
? in this example means zero or one instance of group in front of it
'''

## Result
print(dollars)
# ['$1', '$18087791.41', '$0.25', '$4521947.8525']

