# Apply database column names to a list of rows by using the zip() function

# Data
column_names = ['name', 'salary', 'job']

db_rows = [('Alice', 180000, 'data scientist'),
           ('Bob', 99000, 'mid-level manager'), 
           ('Frank', 87000, 'CEO')
]


## One-Liner
db = [dict(zip(column_names, row)) for row in db_rows]

## Reults
print(db)

# My Testing
# Gets the first row in key, value format that the dict function can then use to create dictionary entry
zipped = [zip(column_names, row) for row in db_rows]
print(list(zipped[0]))

