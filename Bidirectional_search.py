from queue import Queue

def bidirectional_search(graph, start, goal):
    forward_queue = Queue()
    forward_queue.put([start])
    forward_visited = set()

    backward_queue = Queue()
    backward_queue.put([goal])
    backward_visited = set()

    while not forward_queue.empty() and not backward_queue.empty():
        forward_path = forward_queue.get()
        forward_node = forward_path[-1]

        if forward_node == goal or forward_node in backward_visited:
            return forward_path + backward_path[::-1]

        if forward_node not in forward_visited:
            forward_visited.add(forward_node)

            for adjacent in graph.get(forward_node, []):
                new_path = list(forward_path)
                new_path.append(adjacent)
                forward_queue.put(new_path)

        backward_path = backward_queue.get()
        backward_node = backward_path[-1]

        if backward_node == start or backward_node in forward_visited:
            return forward_path + backward_path
