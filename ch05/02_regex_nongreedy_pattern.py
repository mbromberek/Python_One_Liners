## Dependencies
import re

'''
Find al patterns that start with the character 'p', end with the character 'r' and have at least one occurence of the character 'e'
'''
text = 'peter piper picked a peck of pickled peppers'

# My guess
print(re.findall('pe*.*?r', text))
# ['peter', 'piper', 'picked a peck of pickled pepper']

## One liner
result = re.findall('p.*?e.*?r', text)
# ['peter', 'piper', 'picked a peck of pickled pepper']

## Result
print(result)

