"""
Interview Practice
File Structure
Other Techniques

            Tatsuya Arai

"""

set_val = set([])
set_val.add(1)
set_val.add(1)
set_val.add(2)
set_val.add(3)
"""
>>> set_val
set([1, 2, 3])
>>>
""" 

from collections import Counter
"""
>>> Counter([1,2,3,4,5,2,3,4,1,5,3])
Counter({3: 3, 1: 2, 2: 2, 4: 2, 5: 2})
>>> Counter("It has been a hot summer.")
Counter({' ': 5, 'e': 3, 'a': 2, 'h': 2, 'm': 2, 's': 2, 't': 2, 'b': 1, 'I': 1, 'o': 1, 'n': 1, 'r': 1, 'u': 1, '.': 1})

>>> string = "aaabbbcccdd"
>>> from collections import Counter
>>> [elm + str(Counter(string)[elm]) for elm in Counter(string)]
['a3', 'c3', 'b3', 'd2']
>>> ''.join([elm + str(Counter(string)[elm]) for elm in Counter(string)])
'a3c3b3d2'
#### Problems:
# 1. b and c got swapped.
# 2. This does not work with string = "aaabbbcccdda"

"""

''.join(["a","b","c","d","e"])
"""
'abcde'
>>> '%'.join(["a","b","c","d","e"])
'a%b%c%d%e'
"""

"It has been a hot summer".split(" ")
"""
['It', 'has', 'been', 'a', 'hot', 'summer']
>>> "It has been a hot summer".split("e")
['It has b', '', 'n a hot summ', 'r']
"""

[i for i in [1,2,3] for j in [1,2,3,4]]
"""
list comprehenshion
[1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
"""

int_str = str(101)
"""
>>> int(int_str,2)
5
>>> int(int_str)
101
>>> int(int_str,10)
101
>>> int(int_str,3)
10
"""

bin(65)
"""
'0b1000001'
"""
bin(65)[2:]
"""
'1000001'
"""
bin(65)[2:].zfill(32)
"""
'00000000000000000000000001000001'
"""
int(bin(65),2)
"""
65
"""
int(bin(65)[2:],2)
"""
65
"""
int("1"*32,2)
"""
4294967295
"""

### Backwards
lst = [1,2,3,4,5,6,7]
for i1 in range(len(lst)-1, -1, -1):
	print(lst[i1])


lst[-1::-1]
"""
[7, 6, 5, 4, 3, 2, 1]
"""

### Lower Upper 
https://www.codechef.com/problems/NITIKA
# gandhi -> Gandhi
# mahatma gandhI -> M. Gandhi
# Mohndas KaramChand ganDhi -> M. K. Gandhi
# 3
# gandhi
# mahatma gandhI
# Mohndas KaramChand gandhi

def whatsInTheName(strings):
    out_strings = ""
    # Last Name #
    if -1 == strings.find(" "):
        out_strings = out_strings + strings[0].upper() + strings[1:].lower()
    else:
        out_strings = out_strings + strings[0].upper() + ". "
        out_strings = out_strings + whatsInTheName(strings[strings.find(" ") + 1:]) 
    return out_strings


strings = "Mohndas KaramChand gandhi"
ans = whatsInTheName(strings)
ans

strings = "mahatma gandhI"
ans = whatsInTheName(strings)
ans
# Recursive way
# .find(" "), .upper(), and .lower()
# .find(" ") points at the exact index of the letter. 
# If I need to point at the next letter, that should be +1
# strings[0].upper() + strings[1:].lower() 





### Permutation
import itertools
string = 'CBDA'
perm_ittl = itertools.permutations(string, len(string))
perm_lst = [''.join(elm) for elm in perm_ittl] ### elm is tuple
perm_lst_sorted = sorted(perm_lst)
perm_lst_sorted ### Lexicographical Order
perm_dict = dict([(p, i) for i, p in enumerate(perm_lst_sorted)]) ### list comprehenshion, tuple and dict


import itertools
string = 'fixmfbhyutghwbyezkveyameoamqoi'
#string = 'fixmf'
perm_ittl = itertools.permutations(string, len(string))
perm_lst = [''.join(elm) for elm in perm_ittl] ### elm is tuple
perm_lst_sorted = sorted(perm_lst)
#perm_lst_sorted ### Lexicographical Order
perm_dict = dict([(p, i) for i, p in enumerate(perm_lst_sorted)]) ### list comprehenshion, tuple and dict

###JSON




