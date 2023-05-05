def dfs(graph, start, goal):
    visited = set()
    stack = [(start, [start])]

    while stack:
        node, path = stack.pop()
        if node == goal:
            return path

        if node not in visited:
            visited.add(node)

            for adjacent in graph.get(node, []):
                if adjacent not in visited:
                    new_path = list(path)
                    new_path.append(adjacent)
                    stack.append((adjacent, new_path))
                    print(stack)

    return None

# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D', 'F'],
    'D': ['E'],
    'E': ['F']
}

# Example usage
start_node = 'A'
goal_node = 'B'
result = dfs(graph, start_node, goal_node)
print(result)
