### lambda, map, filter and reduce
# https://www.youtube.com/watch?v=cKlnR-CB3tk
'''
def double(x):
    return x * 2

rslt = double(2)
'''
### lambda parameter(s): return
double = lambda x: 2 * x
rslt = double(2)
rslt
type(double)

'''
def add_xy(x,y):
    return x + y
'''
add_xy = lambda x,y: x + y
rslt = add_xy(2,3)
rslt

'''
def max_xy(x,y):
    if x > y:
        return x
    else: return y
'''
max_xy = lambda x,y: x if x > y else y
rslt = max_xy(2,3)
rslt


### [m,n,p] and fnc() -> map -> [fnc(m), fnc(n), fnc(p)]
'''
def square_lst(lst):
    lst2 = []
    for elm in lst:
        lst2 += [elm ** 2]
    return lst2
'''
lst = [1,2,3,4]
rslt = list(map(lambda x: x**2, lst))
rslt
### List Comprehension
rslt3 = [x**2 for x in lst]
rslt3

### filter
'''
def over_two(lst):
    lst2 = [x for x in lst if x > 2]
    return lst2
'''
rslt = list(filter(lambda x: x>2, lst))
rslt
### List Comprehension
rslt2 = [x for x in lst if x > 2]
rslt2

### reduce
### [m,n,p] and fnc() -> reduce -> f(f(m,n),p)
'''
def mult(lst):
    prod = lst[0]
    for i0 in range(1,len(lst)):
        prod *= lst[i0]
    return prod
'''
from functools import reduce
rslt = reduce(lambda x,y: x*y, lst)
rslt


### generator
# https://www.youtube.com/watch?v=bD05uGo_sVI
## generator vs. list

### list #1
def square_numbers1(nums):
    result = []
    for i in nums:
        result += [i*i]
    return result

### generator #1
def square_numbers2(nums):
    for i in nums:
        yield(i*i)

lst = [1,2,3,4]
rslt1 = square_numbers1(lst)
rslt1
rslt2 = square_numbers2(lst)
rslt2
next(rslt2)
next(rslt2)
next(rslt2)
next(rslt2)
next(rslt2) #### !

rslt2 = square_numbers2(lst)
rslt2
for num in rslt2:
    print(num)

rslt2 = square_numbers2(lst)
rslt2
rslt2_lst = list(rslt2)
rslt2_lst

### List Comprehenshion generator
rslt1 = [x*x for x in lst] ### []
rslt1
rslt2 = (x*x for x in lst) ### ()
rslt2
rslt2_lst = list(rslt2)
rslt2_lst

#https://www.youtube.com/watch?v=DEwgZNC-KyE
import os
import glob
os.chdir("Pictures")
for file in glob.glob("*.jpg"):
    print(file)
