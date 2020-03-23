## Data 
letters_amazon = ''' 
We spent several years building our own database engine, 
Amazon Aurora, a fully-managed MySQL and PostgreSQL-compatible 
service with the same or better durability and availability as 
the commercial engines, but at one-tenth of the cost. We were 
not surprised when this worked.
'''

## One-liner
find = lambda x, q: x[x.find(q)-18:x.find(q)+18] if q in x else -1

## Result
print(find(letters_amazon, 'SQL'))

'''
 This has the inefficiency of doing x.find(q) twice. storing the result of x.find(q) in a separate variable and then using tha variable would be more efficient. This is a downside of trying to get everything on one line. 
'''

