from collections import deque
def create_graph(nodes):
    graph = {}
    h = {}
    i = 0
    while i<nodes:
        node = input("Enter the node value: ").upper()
        edges = input("Enter the edges of the node: ").split(",")
        for j in range(len(edges)):
            edges[j] = edges[j].upper()
        h_value = int(input("Enter the heuristic value of node: "))
       
        graph[node] = edges
        h[node] = h_value
        i=i+1
       
    return graph,h

def heuristic(node,dq,h):
    val = h[node[0]]

    if len(dq)== 0:
        dq.append(node)
    else:
        for i in range(0,len(dq)):
            if h[dq[i][0]] > val:
                dq.insert(i,node)
                break
        else:
            dq.append(node)

    return dq

def cost_calc(path,h):
    final_path = []
    cost = 0
    for item in path:
        final_path.append(item[0])

    for item in path:
        if item[0] == start or item[0] == goal:
            continue
        else:
            cost = cost+h[item[0]]

    return final_path,cost

def greedy(start,goal,graph,h):
    open = deque([start])
    closed = set()
    path = []

    while open:
        node = open.popleft()

        if node[0] == goal:
            closed.add(node[0])
            path.append(node)
            final,cost = cost_calc(path,h)
            return final,cost

        closed.add(node[0])
        path.append(node)

        for neigbour in graph[node[0]]:
            if neigbour in closed or neigbour == '':
                continue
            elif neigbour not in open:
                temp = []
                temp.append(neigbour)
                temp.append(node[0])
                open = heuristic(temp,open,h)

    print("Failure(No Path exisits to goal)")
    return None,None

nodes = int(input("Enter the no. of nodes: "))
g1,h = create_graph(nodes)
print(f"\nGraph: {g1}\n")
print(f"Heusistic Values: {h}\n")

while True:
    start = input("Enter start node: ").upper()
    goal = input("Enter goal node: ").upper()

    ls,cost = greedy(start,goal,g1,h)
    if ls == None and cost == None:
        continue
    else:
        print(f"{ls}\n\n{cost}")