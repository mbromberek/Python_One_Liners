## Dependencies 
import re

## Data
page = '''
<!DOCTYPE html> 
<html> 
<body>

<h1>My Programming Links</h1> 
<a href="https://app.finxter.com/">test your Python skills</a> 
<a href="https://blog.finxter.com/recursion/">Learn recursion</a> 
<a href="https://nostarch.com/">Great books from NoStarchPress</a> 
<a href="http://finxter.com/">Solve more Python puzzles</a>

</body> </html> 
'''

## My tesing
#regex = '<href=*finxter>*<test>|<puzzle>'
regex = 'href=.*finxter.*?(test|puzzle).*'
result = re.findall(regex,page)

print(result)


## One-Liner
practice_tests = re.findall("(<a.*?finxter.*?(test|puzzle).*?>)",page)

## Result
print(practice_tests)
# [('<a href="https://app.finxter.com/">test your Python skills</a>', 'test'), ('<a href="http://finxter.com/">Solve more Python puzzles</a>', 'puzzle')]
