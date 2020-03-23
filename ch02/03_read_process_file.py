'''
Read in a file and store each row as an element in a list. 
Strip the spaces and new lines from the beginning and end of each row.
'''
filename = "../../Alarm app Requirements.txt" 

f = open(filename) 
lines = [] 
for line in f:
    lines.append(line.strip())

print(lines) 


print([line.strip() for line in open("../../Alarm app Requirements.txt")])

