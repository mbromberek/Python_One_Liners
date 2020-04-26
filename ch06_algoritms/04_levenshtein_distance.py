# The Levenshtein distance is a metric to calculate the distance between two strings; in other words, it’s used to quantify the similarity of two strings. Its alternate name, the edit distance, describes precisely what it measures: the number of character edits (insertions, removals, or substitutions) needed to transform one string into another. The smaller the Levenshtein distance, the more similar the strings.

## The Data
a = "cat"
b = "chello"
c = "chess"

## The One-Liner
ls = lambda a, b: len(b) if not a else len(a) if not b else min(
    ls(a[1:], b[1:])+(a[0] != b[0]),
    ls(a[1:], b)+1,
    ls(a, b[1:])+1
)

## The Result
print(ls(a,b)) # 5
print(ls(a,c)) # 4
print(ls(b,c)) # 3

# Python objects are considered False if they are empty or zero

'''
lambda a, b: len(b) if not a else len(a) if not b else min(
Create a lambda function that takes two strings a and b and returns the number of edits required to transform string a into string b

Two trivial cases: if string a is empty, the minimal edit distance is len(b), if string b is empty the minimal edit distance is len(a). 
'''

'''
ls(a[1:], b[1:])+(a[0] != b[0]),
Calcultae the edit distance from a[1:] to b[1:] in a recursive manner. If the leading characters a[0] and b[0] are different you have to fix it by replacing a[0] by b[0], so you increment the edit distance by one.
'''

'''
ls(a[1:], b)+1,
Calculate the distance from a[1:] to b in a recursive manner. 
'''

'''
ls(a, b[1:])+1
Calculate the distance from a to b[1:] in a recursive manner.
'''

'''
Finally take the minimum edit distance of all three 
'''

