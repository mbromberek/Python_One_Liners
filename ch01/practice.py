## Most Important String Methods
y = "  This is lazy\t\n  "
print(y)
print(y.strip()) # Remove Whitespace

y = "DrDre"
print(y.lower())


print("attention".upper()) # Uppercase: 'ATTENTION'

print("smartphone".startswith("smart")) # Matches the string's prefix against the argument: True

print("smartphone".endswith("phone")) # Matches the string's suffix against the argument: True

print("another".find("other")) # Match index: 2

print("cheat".replace("ch", "m")) # Replaces all occurrences of the first by the second argument: meat

print(','.join(["F", "B", "I"])) # Glues together all elements in the list using the separator string: F,B,I

print(len("Rumpelstiltskin")) # String length: 15

print("ear" in "earth") # Contains: True