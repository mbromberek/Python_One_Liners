## Dependencies 
import re

'''
[^\s] = not a whitespace
\s = whitespace
'''

## Data
text = '''
It was a bright cold day in April, and the clocks were 
striking thirteen. Winston Smith, his chin nuzzled into 
his breast in an effort to escape the vile wind, slipped 
quickly through the glass doors of Victory Mansions, 
though not quickly enough to prevent a swirl of gritty
 dust from entering along with him. 
-- George Orwell, 1984 
'''

'''
Get all words the contain duplicate characters next to each other
'''
## One-liner
duplicates = re.findall('([^\s]*(?P<x>[^\s])(?P=x)[^\s]*)', text)

## Results
print(duplicates)
# [('thirteen.', 'e'), ('nuzzled', 'z'), ('effort', 'f'), ('slipped', 'p'), ('glass', 's'), ('doors', 'o'), ('gritty', 't'), ('--', '-'), ('Orwell,', 'l')]

print('\n')


'''
Get all words that contain duplicate characters next to each other or with one character between them
'''
duplicates = re.findall('([^\s]*(?P<x>[^\s])[^\s]{0,1}(?P=x)[^\s]*)', text)

## Results
print(duplicates)
# [('were', 'e'), ('striking', 'i'), ('thirteen.', 'e'), ('nuzzled', 'z'), ('effort', 'f'), ('slipped', 'p'), ('glass', 's'), ('doors', 'o'), ('prevent', 'e'), ('gritty', 't'), ('--', '-'), ('Orwell,', 'l')]

