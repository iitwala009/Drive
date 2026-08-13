from collections import deque

def input_graph():
    graph = {}

    n = int(input("Enter number of nodes: "))

    for i in range(n):
        node = input("Enter node value: ").upper()

        neighbours = input("Enter connected nodes: ").upper().split()

        graph[node] = neighbours

    return graph

def breadth_first_search(graph, start,final):

    visited = []
    queue = deque()

    queue.append(start)

    while queue:

        print("\nQueue:", list(queue))
        print("Visited:", visited)

        current = queue.popleft()
        
        
        if current not in visited:
            visited.append(current)
            if current == final:
                print("\nBFS Path:", visited)
                break
                
            for neighbour in graph[current]:
                if neighbour not in visited:
                    queue.append(neighbour)
                    
def depth_first_search(graph, start,final):

    visited = []
    stack = [start]

    while stack:

        print("\nStack:", stack)
        print("Visited:", visited)

        current = stack.pop()

        if current in visited:
            continue
            
        elif current == final:
            visited.append(current)
            print("\nDFS Path:", visited)
            break
        
        visited.append(current)

        for neighbour in reversed(graph[current]):
            if neighbour not in visited:
                stack.append(neighbour)
                
while(True): 
    print("--------------------Menu---------------------") 
    print("Choose apropriate number") 
    print("1. BFS") 
    print("2. DFS") 
    print("3. Exit.")

    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        graph = input_graph()
        print("\nGraph :",graph)
        start = input("\nEnter starting node: ").upper()
        final = input("Enter final node: ").upper()
        breadth_first_search(graph, start , final)

    elif choice == 2:
        graph = input_graph()
        print("\nGraph :",graph)
        start1 = input("\nEnter starting node: ").upper()
        final1 = input("Enter final node: ").upper()
        depth_first_search(graph, start1,final1)

    elif choice == 3:
        print("Stop the Process....")
        break;

    else:
        print("Enter valid choice")


