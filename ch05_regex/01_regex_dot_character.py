## Dependencies
import re


text = '''A blockchain, originally block chain, is a growing list of records, called blocks, which are linked using cryptography. I added book to test number of dots matters.
'''

'''
The dot regex matches any character (including whitespace chracters). Can indicate you do not care which character matches, as long as exactly one matches.
'''
print(re.findall('b...k', text))
# ['block', 'block', 'block']

print(re.findall('y.*y', text))
# ['y block chain, is a growing list of records, called blocks, which are linked using cryptography']

'''
Added new line characters that are in the book since the . does not match with new line characters. 
'''
text = '''A blockchain, originally block chain, 
is a growing list of records, called blocks, 
which are linked using cryptography. I added book to test number of dots matters.
'''
print(re.findall('y.*y', text))
# ['yptography']

'''
zero-or-one regex, ?, applies to the regex immediately in front of it. Says the patter it modifies is optional
'''
print(re.findall('blocks?', text))
# ['block', 'block', 'blocks']


'''
Another use for the ? can be combined with the asterisk operator *?
this allows for nongreedy pattern matching. 
.*? searches for a minimal number of arbitrary characters
.* without the ? will greedily match as many characters as possible
'''
txt = '<div>hello world</div>'

print(re.findall('<.*>', txt))
# ['<div>hello world</div>']

print(re.findall('<.*?>', txt))
# ['<div>', '</div>']

print(re.findall('>.*?<', txt))
# ['>hello world<']

