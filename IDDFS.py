def dls_stack(graph, start, depth_limit):
    stack = [(start, 0)]   # (node, current_depth)
    visited = set()

    while stack:
        node, depth = stack.pop()

        if node not in visited:
            print(node, end=" ")
            visited.add(node)

        # Only expand if within depth limit
        if depth < depth_limit:
            for neighbor in reversed(graph.get(node, [])):
                stack.append((neighbor, depth + 1))


def iddfs(graph, start, max_depth):
    for depth in range(max_depth + 1):
        print(f"\nDepth Level {depth}: ", end="")
        dls_stack(graph, start, depth)


# --- User Input Section ---
graph = {}
n = int(input("Enter number of nodes: "))

for _ in range(n):
    node = input("Enter node: ")
    neighbors = input(f"Enter neighbors of {node} (space-separated): ").split()
    graph[node] = neighbors

start = input("Enter starting node: ")
max_depth = int(input("Enter maximum depth: "))

iddfs(graph, start, max_depth)