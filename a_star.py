import heapq

def a_star(graph, heuristic, start, goal):
    # OPEN list as priority queue (f_cost, node)
    open_list = []
    heapq.heappush(open_list, (0, start))

    # g-cost table
    g_cost = {start: 0}

    # parent table
    parent = {start: None}

    while open_list:
        current_f, current = heapq.heappop(open_list)

        # Goal check
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            return path, g_cost[goal]

        # Explore neighbors
        for neighbor, cost in graph[current]:
            tentative_g = g_cost[current] + cost

            if neighbor not in g_cost or tentative_g < g_cost[neighbor]:
                g_cost[neighbor] = tentative_g
                f_cost = tentative_g + heuristic[neighbor]
                heapq.heappush(open_list, (f_cost, neighbor))
                parent[neighbor] = current

    return None, float('inf')


# -------- PREDEFINED GRAPH (5 NODES) --------

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': [('E', 3)],
    'E': []
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 2,
    'D': 1,
    'E': 0
}

start_node = 'A'
goal_node = 'E'

# Run A*
path, cost = a_star(graph, heuristic, start_node, goal_node)

# Output
print("Optimal Path:", path)
print("Total Cost:", cost)
