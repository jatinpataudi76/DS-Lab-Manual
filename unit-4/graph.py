graph = {
    'A': [('B', 2), ('C', 4)],
    'B': [('D', 1)],
    'C': [('D', 3)],
    'D': []
}

print("Directed Weighted Graph:")

for node in graph:
    print(node, "->", graph[node])