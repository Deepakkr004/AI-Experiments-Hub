import heapq

def a_star(graph, start, goal, heuristic):
    frontier, cost_so_far, came_from = [(0, start)], {start: 0}, {start: None}
    
    while frontier:
        _, current = heapq.heappop(frontier)
        
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = came_from[current]
            return path[::-1], cost_so_far[goal]
        
        for neighbor, cost in graph[current].items():
            new_cost = cost_so_far[current] + cost
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                heapq.heappush(frontier, (new_cost + heuristic(neighbor, goal), neighbor))
                came_from[neighbor] = current
                
    return None, float('inf')

graph = {'A': {'B': 1, 'C': 4}, 'B': {'A': 1, 'C': 2, 'D': 5}, 'C': {'A': 4, 'B': 2, 'D': 1}, 'D': {'B': 5, 'C': 1, 'E': 3}, 'E': {'D': 3}}

def heuristic(node, goal): return {'A': 7, 'B': 6, 'C': 2, 'D': 1, 'E': 0}[node]

path, cost = a_star(graph, 'A', 'E', heuristic)
print(f"Path: {path}\nCost: {cost}")
