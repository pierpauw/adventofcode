from math import floor

TIME = 40929790
DISTANCE = 215106415051100

# Let's go c'est du O(1) :D

x = TIME/2
gap = x**2 - DISTANCE
t_max = gap**0.5

if (x-t_max) == int(x-t_max):
    t_max_fixed = t_max - 1
else:
    t_max_fixed = t_max

if TIME%2 == 0:
    possibilities = 1 + 2*floor(t_max_fixed)
else:
    possibilities = 0 + 2*round(t_max_fixed)

print(possibilities)