### String
Explicitly use whitespace characters in strings. 
Most often used whitespace characters are:
- newline character \n
- space character \s
- tab character \t

The keyword `None` is a a Python constant meaning the `absence of a value`. 
Other programming languages such as Java use the value `null` instead.

If you do not define a return value for a function it will return `None`
"" and 0 are not the same as `None`


### Lists
Lists are mutable

### Keyword: is
The keyword `is` simply checks whether both variables refer to the same object in memory. 
This can confuse Python newcomers. 
```
y = x = 3

print(x is y) # True
print([3] is [3]) # False

```

If you create two lists - even if they contain the same elements - they still refer to two different list objects in memory. Modifying one list object does not affect the other list object. We say that lists are mutable because they can be modified after creation. Therefore, if you check whether one list refers to the same object in memory, the result is `False`. However, integer values are immutable, so there is no risk of one variable changing the object that will then accidentally change all other variables. The reason is that you cannot change the integer object 3 -- trying it will only create a new integer object and leave the old one unmodified. 

### Sets
A set is an unordered collection of unique elements.

You can create a set of strings, because strings are hashable. But you cannot create a set of lists, because lists are unhashable. 
The reason is that the hash value depends on the content of the item, and lists are mutable. if you change the list data type, the has value must change too. Because mutable data types are not hashable, you cannot use them in sets

Sets are unordered
```
hero = "Harry" 
guide = "Dumbledore" 
enemy = "Lord V."
characters = {hero, guide, enemy}
```
All elements in a set must be unique
#### Dictionaries
The `dictionary` is a useful data structure for storing (key, value) pairs:
```
calories = {'apple' : 52, 'banana' : 89, 'choco' : 546}
print(calories['apple'] < calories['choco']) # True 
calories['cappu'] = 74 
print(calories['banana'] < calories['cappu']) # False

print('apple' in calories.keys()) # True 
print(52 in calories.values()) # True
```

### List and Set Comprehension

List comprehension is a popular Python feature that helps you quickly create and modify lists. The simple formula is `[expression + context]`
- Expression - Tells Python what to do with each elemet in the list.
- Context - Tells Python which list elements to select. The context conssists of an arbitrary number of for and if statements
For example, in the list comprehension statement [x for x in range(3)], -- the first part `x` is the (identity) expression, and the secon part `for x in range(3)` is the context. The statement creates the list [0, 1, 2]. The range() function returns a range of subsequent integer values , 1, and 2 -- when used with one argument as in the example. Another code example for list comprehension is the following. 


```
# (name, $-income)
customers = [("John", 240000),("Alice", 120000), ("Ann", 1100000), ("Zach", 44000)]

# your high-value customers earning >$1M 
whales = [x for x,y in customers if y>1000000] 
print(whales) # ['Ann']
```
Set comprehension is like list comprehension, but creates a set rather than a list

### Lambdas
`Lambdas Functions` are anonymous functions that are not defined in the namespace. Roughly speaking, they are functions without names, intended for single use. 
```
Syntax:
lambda <arguments> : <return expression>
```
A lambda function can have one or multiple arguments, separated by commas. After the colon(:), you define the return expression that may or may not use the defined argument. The return expression can be any expression or even another function. 

Lambda functions are important in Python. They are often used to make code shorter and more concise, or to create arguments of various Python functions (such as map() or reduce() ).
```
print((lambda x: x+3)(3)) # 6
print((lambda x: x+3)(4)) # 7

f = lambda x: x+3
print(f(8)) # 11
```

First you create a lambda function that takes a value x and returns the result of the expression x+3. The result is a function object that can be called like any other function. 
