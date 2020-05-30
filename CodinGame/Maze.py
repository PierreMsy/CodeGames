# Write an action  print, To debug: print("Debug messages", file=sys.stderr)
import sys
import math


def available_neighboors(grid, r, c):

    res = []
    
    for cor in ((r+1, c),(r-1, c), (r, c+1), (r, c-1)):
        if grid[cor[0]][cor[1]] != '#':
            res.append((cor[0],cor[1]))
    
    return res

def calculate_next_direction(r, c, nr, nc):
    if nr - r > 0:
        return 'DOWN'
    elif nr - r < 0 :
        return 'UP' 
    elif nc - c > 0:
        return 'RIGHT'
    else:
        return 'LEFT'

def bfs(initial_coordinates, grid, goal):

    dic_parents = {}
    memory = set()
    queue = []
    queue.append(initial_coordinates)
    memory.add(initial_coordinates)

    while len(queue) > 0:

        r,c = queue.pop(0)
        for rn, cn in available_neighboors(grid, r, c):

            if (rn, cn) not in memory:
                dic_parents[(rn, cn)] = (r, c)

                if grid[rn][cn]==goal:  
                    while (rn, cn) in dic_parents:
                        (rnew, cnew) = dic_parents[(rn, cn)]
                        if (rnew, cnew) == initial_coordinates:
                            return rn,cn
                        else:
                            (rn,cn) = (rnew,cnew) 
  
                memory.add((rn, cn))
                queue.append((rn, cn))

    print("BFS did not found goal", file=sys.stderr)
    return (-1,-1)

# H: number of rows. # W: number of columns.
# a: number of rounds between the time the alarm countdown is activated and the time the alarm goes off.
H, W, a = [int(i) for i in input().split()]
goals = (s for s in ['C','T'])
goal = '?'

# game loop
while True:

    # kr: row where Kirk is located.
    # kc: column where Kirk is located.
    kr, kc = [int(i) for i in input().split()]
    grid = list([input() for _ in range(H)])

    nr, nc = bfs((kr,kc), grid, goal)
    if (nr, nc) ==(-1,-1):
        goal = next(goals)
        nr, nc = bfs((kr,kc), grid, goal)
    
    print(f'goal : {goal}', file=sys.stderr)
    print(f'Kirk : {kr},{kc}', file=sys.stderr)
    print(f'Go to :{nr}{nc}', file=sys.stderr)

    direction = calculate_next_direction(kr,kc, nr,nc)
    print(direction)
    

    
