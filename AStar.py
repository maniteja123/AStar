grid = [    [ [0, 2] , [1, 2] , [-1, 1] , [0, 1] ],
            [ [-1, 1] , [1, 2] , [1, 1] , [1, 2] ],
            [ [0, 2] , [-1, 1] , [1, 1] , [0, 1] ],
            [ [-1, 3] , [0, 1] , [-1 ,2] , [0, 0] ]      ] 

heuristic = [   [6, 5, 4, 3],
                [5, 4, 3, 2],
                [4, 3, 2, 1],
                [3, 2, 1, 0]  ]

init = [0, 0]
goal = [len(grid)-1, len(grid[0])-1]
cost = 1

def search(grid, init, goal , heuristic):

    closed = [[False for row in range(len(grid[0]))] for col in range(len(grid))]
    closed[init[0]][init[1]] = 1
    expand = [[-1 for row in range(len(grid[0]))] for col in range(len(grid))]

    x = init[0]
    y = init[1]
    g = 0
    h = heuristic[x][y]
    f = g + h
    open = [[f, g, h, x, y]]

    found = False  
    resign = False 
    count = 0
    
    while not found and not resign:
        if len(open) == 0:
            resign = True
            return "Fail"
        else:
            open.sort()
            open.reverse()
            next = open.pop()
            if g!=next[1] or g==0:
                print next[3], next[4]
            x = next[3]
            y = next[4]
            g = next[1]
            expand[x][y] = count
            count += 1
            
            if x == goal[0] and y == goal[1]:
                found = True
            else:
                types = grid[x][y][0]
                jump = grid[x][y][1]
                # print x , y, types , jump
                if types==0:
                    for i in range(1,jump+1):
                        x2  = x + i
                        y2  = y + i
                        if x2 >= 0 and x2 < len(grid) and y >=0 and y < len(grid[0]):
                            if not closed[x2][y] :
                                g2 = g + cost
                                h2 = heuristic[x2][y]
                                f2 = g2 + h2
                                open.append([f2, g2,h2, x2, y])
                                closed[x2][y] = True
                        if x >= 0 and x < len(grid) and y2 >=0 and y2 < len(grid[0]):
                            if not closed[x][y2] :
                                g2 = g + cost
                                h2 = heuristic[x][y2]
                                f2 = g2 + h2
                                open.append([f2, g2,h2, x, y2])
                                closed[x][y2] = True
                else:
                    x2 = x + types * jump
                    y2 = y + types * jump
                    if x2 >= 0 and x2 < len(grid) and y >=0 and y < len(grid[0]):
                        if not closed[x2][y]:
                            g2 = g + cost
                            h2 = heuristic[x2][y]
                            f2 = g2 + h2
                            open.append([f2, g2,h2, x2, y])
                            closed[x2][y] = True
                    if x >= 0 and x < len(grid) and y2 >=0 and y2 < len(grid[0]):
                        if not closed[x][y2] :
                            g2 = g + cost
                            h2 = heuristic[x][y2]
                            f2 = g2 + h2
                            open.append([f2, g2,h2, x, y2])
                            closed[x][y2] = True
    
    if found:
        print "Expansion of nodes is"
    for i in range(len(expand)):
        print expand[i]
    return "Success"

print search(grid, init, goal, heuristic)
