graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': []
}

def bfs(graph, start):

    visited = []
    queue = [start]

    while queue:

        node = queue.pop(0)

        if node not in visited:
            visited.append(node)

            queue.extend(graph[node])

    print("BFS:", visited)

def dfs(graph, start, visited=None):

    if visited is None:
        visited = []

    visited.append(start)

    for node in graph[start]:

        if node not in visited:
            dfs(graph, node, visited)

    return visited

bfs(graph, 'A')

print("DFS:", dfs(graph, 'A'))