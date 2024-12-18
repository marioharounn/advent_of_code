# Build graph and in-degrees
    graph = defaultdict(list)
    in_degree = defaultdict(int)

    for x, y in rules:
        if x in update and y in update:
            graph[x].append(y)
            in_degree[y] += 1
            in_degree[x] += 0  # Ensure x exists in in_degree

    # Topological Sort using a list instead of deque
    queue = [node for node in update if in_degree[node] == 0]
    sorted_order = []

    while queue:
        current = queue.pop(0)  # Pop the first element (FIFO)
        sorted_order.append(current)

        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
