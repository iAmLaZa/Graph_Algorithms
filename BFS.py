from queue import Queue

def bfs(graph, start, goal):
    queue = Queue()
    queue.put([start])
    visited = set()

    while not queue.empty():
        path = queue.get()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)

            for adjacent in graph.get(node, []):
                new_path = list(path)
                new_path.append(adjacent)
                queue.put(new_path)
# Example usage: Find a path from 'A' to 'F' in a graph
graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D', 'F'],
    'D': ['E'],
    'E': ['F']
}
start = 'A'
goal = 'F'
path = bfs(graph, start, goal)
print(path)
