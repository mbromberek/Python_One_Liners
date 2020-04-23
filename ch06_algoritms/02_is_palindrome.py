## One-liner
is_palindrome = lambda phrase: phrase == phrase[::-1]


## Result 
print(is_palindrome('hannah')) #True
print(is_palindrome('Hannah')) #False
print(is_palindrome("anna"))  #True
print(is_palindrome("kdljfasjf")) #False
print(is_palindrome("rats live on no evil star"))  #True

## Me playing
is_palindrome = lambda phrase: phrase.lower() == phrase.lower()[::-1]
print(is_palindrome('hannah')) #True
print(is_palindrome('Hannah')) #True
'''
Might be best to have the is_palindrome only work for exact text sent and then let the caller us other functions like lower() or remove spaces if they want to
'''
