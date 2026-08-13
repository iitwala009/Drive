from collections import deque

def create_graph(nodes):
    graph = {}

    for i in range(nodes):
        node = input("Enter Node Value: ").upper()

        edge = input("Enter its edges (Enter spaces between edges): ").split(",")

        for j in range(len(edge)):
            edge[j] = edge[j].upper()

        graph[node] = edge

    return graph

def bfs(start,goal,graph):
    visited = []
    queue = deque([start])

    while queue:
        print("Queue:", queue)
        print("Visited:", visited)
        print()

        node = queue.popleft()

        if node in visited:
            continue
        elif node == goal:
            visited.append(node)
            print(f"BFS Path: {visited}")
            return

        visited.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append(neighbor)

    print()
    print(f"BFS Path: {visited}")

def dfs_recursive(node,goal,graph,visited=None):

    if visited is None:
        visited = []

    if node in visited:
        return
    elif node == goal:
        visited.append(node)
        return

    visited.append(node)
    print(node, end=" ")

    for neighbor in graph[node]:
        dfs_recursive(neighbor, graph, visited)

def dfs(start,goal,graph):
    visited = []
    stack = [start]

    while stack:
        print("Stack:", stack)
        print("Visited:", visited)
        print()

        node = stack.pop()

        if node in visited:
            continue
        elif node == goal:
            visited.append(node)
            print(f"DFS Path: {visited}")
            return

        visited.append(node)

        for neighbor in reversed(graph[node]):
            if neighbor not in visited:
                stack.append(neighbor)
    print()
    print(f"DFS Path: {visited}")

   
nodes = int(input("Enter the number of nodes in the graph: "))
g1 = create_graph(nodes)


while(True):
    c = input("What Do you want to do?\n 1.BFS\n 2.DFS\n 3.Re-enter Graph\n 4.Exit\n")
   
    match c:
        case "1":
            print("\nGraph:", g1)
            start = input("Enter the starting point: ").upper()
            goal = input("Enter the Goal Node: ").upper()
            print("\nBFS:")
            bfs(start,goal,g1)
        case "2":
            print("\nGraph:", g1)
            start = input("Enter the starting point: ").upper()
            goal = input("Enter the Goal Node: ").upper()
            print("DFS:")
            dfs(start,goal,g1)
        case "3":
            nodes = int(input("Enter the number of nodes in the graph: "))
            g1 = create_graph(nodes)
        case "4":
            print("\nExiting Program...")
            break