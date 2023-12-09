from math import floor

TIME = [40,92,97,90]
DISTANCE = [215,1064,1505,1100]

# Time for some maths !

# Maximum of a*b given a+b=n is for a=b=n/2.
# When reasoning over integers, it can then be 
# a=b=n/2 (if n is even), or 
# a=floor(n/2), b=a+1 (if n is odd), or
# (the same with a and b switched).

# Another interesting fact is, (x-t)(x+t) = x²-t².

# In the context of the problem, we have a given duration (n) to split between "hold" (a) and "move" (b).
# They match the a and b variables in the first paragraph.
# For now, we will only keep x as the optimal solution (not always integer).

# We can then find instantly wether the optimal play is winning, with what distance, and its gap to the record.
# This gap represents the maximum distance t² allowed for us to stay better than the record.
# This means "t_max := sqrt(t²=gap)" gives us the maximum time away from the optimal solution that keeps us above the record.
# However, if x-t_max is an integer, it means 2 solutions actually tie the current record. We should not count them.
# We introduce t_max_fixed which is t_max-1 if so, and t_max otherwise.

# To find how many solutions are possible, we then need to add :
# if n is even -> 1 (optimal solution)      + 2*floor(t_max_fixed) (2 times because you can be either too early or too late)
# if n is odd  -> 0 (no optimal solution)   + 2*round(t_max_fixed) (round because n odd causes x to be #.5 and, if t is more than #.5, it creates 2 more solutions)

product = 1

for i in range(len(TIME)):
    racetime = TIME[i]
    record = DISTANCE[i]

    x = racetime/2
    gap = x**2 - record
    t_max = gap**0.5
    
    if (x-t_max) == int(x-t_max):
        t_max_fixed = t_max - 1
    else:
        t_max_fixed = t_max
    
    if racetime%2 == 0:
        possibilities = 1 + 2*floor(t_max_fixed)
    else:
        possibilities = 0 + 2*round(t_max_fixed)
    
    product *= possibilities

print(product)