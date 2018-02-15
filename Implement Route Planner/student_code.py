import heapq
def shortest_path(M,start,goal):
    print("shortest path called")
    
    if start == goal:
        return [start]
    
    ## Initialize h 
    n = len(M.intersections)
    h = [0] * n
    for i in range(n):
        h[i] = dis(M, i, goal)
    
    ## Implement A* Algorithm
    
    ## Initialization
    frontier = []
    parent = {}
    destinations = {}
    destinations[start] = 0
    explored = set()
    explored.add(start)
    for i in range(len(M.roads[start])):
        cost = dis(M, start, M.roads[start][i])
        parent[M.roads[start][i]] = start
        destinations[M.roads[start][i]] = cost
        heapq.heappush(frontier, (cost + h[M.roads[start][i]], M.roads[start][i]))
    
    ## Find the path
    while(frontier[0][1] != goal):
        next_road = heapq.heappop(frontier) 
        explored.add(next_road[1])
        for i in M.roads[next_road[1]]:
            if i in explored:
                continue
            new_cost = next_road[0] - h[next_road[1]] + dis(M, next_road[1], i)
            if i in destinations and destinations[i] < new_cost:
                continue
            heapq.heappush(frontier, (new_cost + h[i], i))
            destinations[i] = new_cost
            parent[i] = next_road[1]
    
    temp = goal
    path = [goal]
    while(temp != start):
        temp = parent[temp]
        path.append(temp)
        
    return path[::-1]

def dis(M, A, B):
    
    res = ((M.intersections[B][0] - M.intersections[A][0])**2 + (M.intersections[B][1] - M.intersections[A][1])**2) ** 0.5
    
    return res