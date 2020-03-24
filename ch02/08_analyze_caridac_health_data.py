## Dependencies 
import matplotlib.pyplot as plt

## Data
cardiac_cycle = [62, 60, 62, 64, 68, 77, 80, 76, 71, 66, 61, 60, 62]

# Want to remove the first digit and last two digits of data since they are redundant, then repeat the data 10 times

## One-liner
expected_cycles = cardiac_cycle[1:-2] * 10

## Result
plt.plot(expected_cycles)
plt.show()
