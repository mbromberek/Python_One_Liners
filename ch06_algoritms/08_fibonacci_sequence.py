## Dependencies
from functools import reduce

## The Data
n = 13

## The One-liner
fibs = reduce(lambda x, _: x + [x[-2] + x[-1]], [0] * (n-2), [0, 1])

## Results
print(fibs)

'''
Use the reduce() function with three arguments: reduce(function, iterable, initializer)

use a simple list as the aggregator object with the two initial Fibonacci numbers [0, 1]. Remember that the aggregator object is handed as the first argument to the function (in our example, x).

The second argument is the next element from the iterable. However, you initialized the iterable with (n-2) dummy values in order to force the reduce() function to execute function (n-2) times (the goal is to find the first n Fibonacci numbers—but you already have the first two, 0 and 1) You use the throwaway parameter _ to indicate that you are not interested in the dummy values of the iterable. Instead, you simply append the new Fibonacci number to the aggregator list x, calculated as the sum of the previous two Fibonacci numbers.


'''
