## Dependencies
import re

'''
Get instances where text contains the work crypto and within 30 characters of crypto is the work coin
'''


## Data
text_1 = "crypto-bot that is trading Bitcoin and other currencies" 
text_2 = "cryptographic encryption methods that can be cracked easily with quantum computers"

## One-liner
pattern = re.compile("crypto(.{1,30})coin")

## Result
print(pattern.match(text_1))
# <re.Match object; span=(0, 34), match='crypto-bot that is trading Bitcoin'>

print(pattern.match(text_2))
# None


'''
() matches whatever regex is inside
. matches an arbitrary character
{1,30} matches between 1 and 30 occurrences of the previous regex
(.{1,30})coin Matches the regex consisting of three parts: the word 'crypto', an arbitrary sequence with 1 to 30 chars, followed by the word 'coin'.
'''


print(pattern.match(text_1).group())
# crypto-bot that is trading Bitcoin

'''
group() - Return the string matched by the RE
start() - Return the starting position of the match
end() - Return the ending position of the match
span() - Return a tuple containing the (start, end) positions of the match
'''

