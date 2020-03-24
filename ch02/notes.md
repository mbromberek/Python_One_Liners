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

### Lambda functions
Lambda functions allow you to define a new function in a single line by using the keyword `lambda`. This is useful when you want to quickly create a function that you will use only once and can be garbage collected immediately afterward. 
```
lambda arguments : return expression
```
You start the function definition with the keyword `lambda`, followed by a sequence of function arguments. When calling the function the caller must provide these arguments. You then include a colon and the `return expression`, which calculates the return value based on the arguments of the lambda function. The return expression calculates the function output and can be any Python expression. 
```
lambda x, y: x + y
```

### Slicing
```
x[start:stop:step]
```
Starts at index start (included) and ends at index stop (excluded). You can include an optional third step argument that determines which elements are carved out, so you could choose to include just every step-th element. For example, the slicing operation x[1:4:1] used on variable `x = 'hello world'` results in the string 'ell'. Slicing operation `x[1:4:2]` on the same variable results in string 'el' because only every other element in taken into the resulting slice. 
If you do not include the step argument Python assumes the default step size of one. 
If you do not include te beginning or ending arguments Python assumes you want to start at the start, or end at the end. The slice call `x[:4]` would result in 'hell'
- If step size is positive the default start is the leftmost element, and the default stop is the rightmost element (excluded)
- If the step size is negative (step <0) the slice traverses the sequence in reverse order. You slice from the rightmost element (included) to the leftmost element (excluded)
```
s = 'Eat-more_fruits!'
print(s[6:1:-1])
# rom-t
```

### Combining List Comprehension and Slicing
- List Comprehension allows you to iterate over each list element and modify it subsequently
- Slicing allows you to quickly select every other element from a given List

### Generator Expressions
`Generator Expressions` work exactly like list comprehensions - but without creating an actual list in memory. The numbers are created on the fly, without storing them explicitly in a list. 
Example instead of using list comprehension to calculate the squares of the first 20 numbers, `sum([x*x for x in range(20)])` you can use a generator expression: `sum(x*x for x in range(20))`

### Zip functon
`zip()` takes iterables and aggregates them into a single iterable by aligning the corresponding i-th values into a single tuple. The result is an iterable of tuples.


## Summary
In this chapter you have mastered list comprehensions, file input, the functions lambda, map, and zip, the all qualifier, slicing, and basic list arithmetic. 
Also learned how to use and manipulate data structures to solve various day to day problems. 

