import re

text = ''' 
"One can never have enough socks", said Dumbledore. 
"Another Christmas has come and gone and I didn't 
get a single pair. People will insist on giving me books." 
Christmas Quote 
'''

regex = 'Christ.*'

'''
match() looks for the pattern only at the beginning of the string
'''
print(re.match(regex, text))
# None

'''
search() searches for the first occurence of the regex anywhere in the string
'''
print(re.search(regex, text))
# <re.Match object; span=(64, 105), match="Christmas has come and gone and I didn't ">

'''
finall() results in a sequence of string rather than a match object, so we do not have the precise location of the match
'''
print(re.findall(regex, text))
# ["Christmas has come and gone and I didn't ", 'Christmas Quote ']

