import sys
import math


l, rides, n = [int(i) for i in input().split()]
groups = list([int(input()) for _ in range(n)]) # use dic to acces ?
nbr_groups = len(groups)

mem = {}
res = 0
state = 0

for _ in range(rides):
    
    if state in mem:
        state, gain = mem[state]
    
    else:
        free = l
        gain = 0
        cnt = 0
        j = state
        
        while True:
            group_size = groups[j]
            if (free < group_size) | (cnt >= nbr_groups):
                break
            cnt += 1
            j += 1
            j %= nbr_groups
            free -= group_size
            gain += group_size
        
        mem[state] = (j, gain)
        state = j
    
    res += gain

print(res)
    
