def dfs(visited, graph, node): 
    if node not in visited:
        visited.append(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)
    return visited


def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)
    while queue:
        m = queue.pop(0) 
    for neighbour in graph[m]:
        if neighbour not in visited:
            visited.append(neighbour)
            queue.append(neighbour)
    return visited

graph = {
    'A' : ['B','C','D','E'],
    'B' : ['D'],
    'C' : ['E'],
    'D' : ['E'],
    'E' : []
}

visited = []
print('DFS')
print(dfs(visited, graph, 'A'))

visited = []
queue = []
print('\nBFS')
print(bfs(visited, graph, 'A'))
