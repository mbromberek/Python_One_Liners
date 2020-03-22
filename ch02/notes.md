### Using List comprehension
[expression + context]

```
print([x for x in range(5)])
# [0, 1, 2, 3, 4]
```
Expression: is `x`: Identity function (does not change the context variable x).
Context: is `for x in range(5)]`: Context variable x takes all values returned by the range function: 0, 1, 2, 3, 4

```
print([(x, y) for x in range(3) for y in range(3)]) 
# [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
```
Expression `(x, y)`: Create a new tuple from the context variables x and y
Context `for x in range(3) for y in range(3)]`: The context variable x iterates over all values returned by the range function - 0, 1, 2, while context variable y iterates over all values returned by the range function - 0, 1, 2. 
The two for loops are nested, so the context variable y repeats its iteration procedure for every single value of the context variable x. Thus, there are 3 x 3 = 9 combinations of context variables. 

```
print([x ** 2 for x in range(10) if x % 2 > 0])
# [1, 9, 25, 49, 81]
```
Expression `x ** 2`: Square function on the context variable x
Context `for x in range(10) if x % 2 > 0`: Context variable x iterates over all values returned by the range function - 0 through 10 - but only if they are odd values

```
print([x.lower() for x in ['I', 'AM', 'NOT','SHOUTING']])
# ['i','am','not','shouting']
```
Expression `x.lower()`: String lowercase function on context variable x
Context `for x in ['I', 'AM', 'NOT','SHOUTING']]`: Context variable x iterates over all string values in the List

```
employees = {'Alice' : 100000,
             'Bob': 99817,
             'Carol': 122908,
             'Frank': 99123,
             'Eve': 93121
}
top_earners_oneline = [(k, v) for k, v in employees.items() if v>=100000]
print(top_earners_oneline)
```
Expression `(k, v)`: Creates a simple key-value tuple for context variables
Context `for k, v in employees.items() if v>=100000`: The dictionary method dict.items() ensures that context variable k iterates over all dictionary keys and that context variable v iterates over the associated values for context variable k - but only if the value of context variable v is larger than or equal to 100,000 as ensured by the if condition.

This demonstrates concept of `list comprehension`. We use list comprehension in multiple instances in this book. 


Of course, you need to get used to thinking in terms of list comprehensions, so the meaning may not come naturally to you. But after reading this book, list comprehensions will be your bread and butter—and you’ll quickly read and write Pythonic code like this.

