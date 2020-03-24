## Data
visitors = ['Firefox', 'corrupted', 'Chrome', 'corrupted',
            'Safari', 'corrupted', 'Safari', 'corrupted', 
            'Chrome', 'corrupted', 'Firefox', 'corrupted']

# Need to replace the corrupted with the browser name before it

## One-Liner
# Right side of equal starts at zero and goes ahead two records each time
# Left side of equal starts at one and goes ahead two records each time
visitors[1::2] = visitors[::2]

## Result
print(visitors)

