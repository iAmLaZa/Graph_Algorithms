def dls(graph, start, goal, depth_limit):
    visited = set()

    def dls_helper(node, path, depth):
        if node == goal:
            return path

        if depth == depth_limit:
            return None

        if node not in visited:
            visited.add(node)

            for adjacent in graph.get(node, []):
                new_path = list(path)
                new_path.append(adjacent)
                result = dls_helper(adjacent, new_path, depth+1)
                if result is not None:
                    return result

    return dls_helper(start, [start], 0)

#Iterative deepening depth-first search:
def iddfs(graph, start, goal):
    for depth_limit in range(len(graph)):
        result = dls(graph, start, goal, depth_limit)
        if result is not None:
            return result
