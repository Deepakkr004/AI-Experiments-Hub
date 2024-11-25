from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    result = []

    while queue:
        vertex = queue.popleft()

        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)

            for neighbor in graph[vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return result

# Example usage:
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}

print(bfs(graph, 'A'))  # Output: ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
