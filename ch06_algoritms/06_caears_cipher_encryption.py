'''
shift each character by 13 positions in the alphabet. When shifting over the last character, z , you start over at the first position in the alphabet, a .
'''

## Data
## Data
abc = "abcdefghijklmnopqrstuvwxyz"
s = "xthexrussiansxarexcoming"

## One-liner
rt13 = lambda x: "".join([abc[(abc.find(c) + 13) % 26] for c in x])

## Result
print(rt13(s)) # kgurkehffvnafknerkpbzvat
print(rt13(rt13(s))) # xthexrussiansxarexcoming

