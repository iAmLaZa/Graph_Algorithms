from queue import PriorityQueue

def ucs(graph, start, goal):
    queue = PriorityQueue()
    queue.put((0, [start]))
    visited = set()

    while not queue.empty():
        cost, path = queue.get()
        node = path[-1]

        if node == goal:
            return path

        if node not in visited:
            visited.add(node)

            for adjacent, weight in graph.get(node, {}).items():
                new_cost = cost + weight
                new_path = list(path)
                new_path.append(adjacent)
                queue.put((new_cost, new_path))

# Example usage: Find a path from 'A' to 'F' in a graph
graph = {
    'A': {'B': 1, 'C': 2},
    'B': {'C': 3, 'D': 4},
    'C': {'D': 5, 'F': 6},
    'D': {'E': 7},
    'E': {'F': 8},
    'F': {}
}
start = 'A'
goal = 'F'
path = ucs(graph, start, goal)
print(path)
