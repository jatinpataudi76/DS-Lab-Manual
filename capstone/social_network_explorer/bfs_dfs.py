from collections import deque

def bfs_shortest_path(graph, start, end):
    """Degrees of separation between two users"""
    if start == end:
        return [start]
    
    visited = {start}
    queue = deque([[start]])  # queue of paths

    while queue:
        path = queue.popleft()
        node = path[-1]

        for neighbor in graph.adj.get(node, []):
            if neighbor == end:
                return path + [neighbor]
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(path + [neighbor])
    
    return None  # No connection found


def dfs_explore(graph, start, depth, visited=None, current_depth=0):
    """Friends-of-friends up to depth d"""
    if visited is None:
        visited = set()
    
    visited.add(start)

    if current_depth >= depth:
        return visited

    for neighbor in graph.adj.get(start, []):
        if neighbor not in visited:
            dfs_explore(graph, neighbor, depth, visited, current_depth + 1)
    
    return visited