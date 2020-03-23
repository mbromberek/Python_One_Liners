## Data
txt = ['lambda functions are anonymous functions.',
       'anonymous functions dont have a name.',
       'functions are objects in Python.']

## One-liner with map
mark = map(lambda s: (True, s) if 'anonymous' in s else (False, s), txt)

## Result
print(list(mark))
print()

## One-line with list_comprehension only returning matches
mark_2 = [s for s in txt if 'anonymous' in s]
print(mark_2)
print()

## One-line with list comprehension
mark_3 = [ (True, s) if 'anonymous' in s else (False, s) for s in txt]
print(mark_3)
print()
