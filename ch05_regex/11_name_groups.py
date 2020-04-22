import re

'''
Search for substrings that are enclosed in either single or double quotes
'''
pattern = '(?P<quote>[\'"]).*(?P=quote)'
text = 'She said "hi"'

print(re.search(pattern, text))
# <re.Match object; span=(9, 13), match='"hi"'>

text = 'She said \'hi\''
print(re.search(pattern, text))
# <re.Match object; span=(9, 13), match="'hi'">

text = 'She said "hi\''
print(re.search(pattern, text))
# None