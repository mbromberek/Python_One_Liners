## Data 
text = '''
Call me Ishmael. Some years ago - never mind how long precisely - having 
little or no money in my purse, and nothing particular to interest me 
on shore, I thought I would sail about a little and see the watery part 
of the world. It is a way I have of driving off the spleen, and regulating
 the circulation. - Moby Dick
'''

print(text)
print()

## Get a list of lists of all the words over 3 characters long for each line
w = [[x for x in line.split() if len(x)>3] for line in text.split('\n')]

## Result
print(w)
print()

## Get a single list of all the words over 3 characters long for each line, remove the new line characters
w2 = [x for x in text.replace('\n','').split() if len(x)>3]
print(w2)
print()

