from bisect import bisect_left
import math

def successfulPairs(spells, potions, success):
    potions.sort()
    m = len(potions)
    res = []

    for spell in spells:
        min_required = math.ceil(success / spell)
        idx = bisect_left(potions, min_required)
        res.append(m - idx)
    
    return res
