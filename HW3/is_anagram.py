def is_anagram(s1,s2):
    '''
Downey Exercise 10.7. Two words are anagrams
if you can rearrange the letters from one to
spell the other. Write a function called is_anagram
that takes two strings and returns
True if they are anagrams.Sort each string
If the sorted strings are equal, they are anagrams
Otherwise, they are not anagrams.
turn each string into a list
if these lists equal each other, the 2 strings are anagrams
'''
    L1 = list(s1); L1.sort()
    L2 = list(s2); L2.sort()
    return L1 == L2

def is_anagram1(s1,s2):
    '''
Bottom up approach.
For each ltr in s1:
   # ltr in s1  must equal # ltr in s2.
For each ltr in s2:
   # ltr in s1  must equal # ltr in s2.   
'''
    for letter in s1:
        if (s1.count(letter) != s2.count(letter)):
            return False
    for letter in s2:
        if (s2.count(letter) != s1.count(letter)):
            return False            
    return True
#s1 = 'tops'; s2 = 'stop'
#print(is_anagram(s1,s2))
#print(is_anagram1(s1,s2))
#
#s1 = 'tips'; s2 = 'stop'
#print(is_anagram(s1,s2))
#print(is_anagram1(s1,s2))
#True
#True
#False
#False
#>>>     


