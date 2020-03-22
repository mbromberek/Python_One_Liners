#Chapter 02 - list Comprehension Section

employees = {'Alice' : 100000,
             'Bob': 99817,
             'Carol': 122908,
             'Frank': 99123,
             'Eve': 93121
}

# Original iteration code
top_earners = []
for key, val in employees.items():
    if val >= 100000:
        top_earners.append((key,val))

print(top_earners) # [('Alice',100000), ('Carol',122908)]

# One line iteration code
top_earners_oneline = [(k, v) for k, v in employees.items() if v>=100000]
print(top_earners_oneline)

