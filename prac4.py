# Forward Chaining Algorithm

# Knowledge Base
KB = [
    ({"battery_low", "dim_lights"}, "alternator_fault"),
    ({"alternator_fault"}, "battery_not_charging"),
    ({"battery_not_charging"}, "replace_alternator")
]

# Take initial facts from user
F = set()

n = int(input("Enter number of initial facts: "))

for i in range(n):
    fact = input("Enter fact: ")
    F.add(fact)


# Display goal options
print("\nChoose the goal to prove:")
print("1. alternator_fault")
print("2. battery_not_charging")
print("3. replace_alternator")

choice = int(input("Enter your choice: "))

if choice == 1:
    G = "alternator_fault"
elif choice == 2:
    G = "battery_not_charging"
elif choice == 3:
    G = "replace_alternator"
else:
    print("Invalid choice!")
    exit()


# Forward Chaining Function
def forward_chaining(KB, F, G):

    # Continue applying rules
    while True:

        new_fact_added = False

        # Check every rule
        for antecedents, consequent in KB:

            # If all conditions of the rule are present
            if antecedents.issubset(F):

                # Add conclusion if it is not already known
                if consequent not in F:
                    F.add(consequent)
                    new_fact_added = True

                    # Goal is derived
                    if consequent == G:
                        return True

        # No new fact can be derived
        if new_fact_added == False:
            break

    # Goal could not be derived
    return G in F


# Apply Forward Chaining
result = forward_chaining(KB, F, G)


print("Initial/Derived Facts:", F)
print("Goal:", G)

if result:
    print("Goal can be derived.")
else:
    print("Goal cannot be derived.")







# Backward Chaining Algorithm

# Knowledge Base
KB = [
    ({"battery_low", "dim_lights"}, "alternator_fault"),
    ({"alternator_fault"}, "battery_not_charging"),
    ({"battery_not_charging"}, "replace_alternator")
]

# Take initial facts from user
F = set()

n = int(input("Enter number of initial facts: "))

for i in range(n):
    fact = input("Enter fact: ")
    F.add(fact)


# Display goal options
print("\nChoose the goal to prove:")
print("1. alternator_fault")
print("2. battery_not_charging")
print("3. replace_alternator")

choice = int(input("Enter your choice: "))

if choice == 1:
    G = "alternator_fault"
elif choice == 2:
    G = "battery_not_charging"
elif choice == 3:
    G = "replace_alternator"
else:
    print("Invalid choice!")
    exit()


# Backward Chaining Function
def backward_chaining(KB, F, G):

    # Goal is already a known fact
    if G in F:
        return True

    # Find rules whose conclusion is the goal
    matching_rules = []

    for antecedents, consequent in KB:
        if consequent == G:
            matching_rules.append((antecedents, consequent))

    # No rule can prove the goal
    if len(matching_rules) == 0:
        return False

    # Check each matching rule
    for antecedents, consequent in matching_rules:

        all_antecedents_proven = True

        # Prove every antecedent
        for A in antecedents:

            if backward_chaining(KB, F, A) == False:
                all_antecedents_proven = False
                break

        # All antecedents are proven
        if all_antecedents_proven == True:
            F.add(G)
            return True

    return False


# Apply Backward Chaining
result = backward_chaining(KB, F, G)



print("Initial Facts:", F)
print("Goal:", G)

if result:
    print("Goal can be derived.")
else:
    print("Goal cannot be derived.")






# 18/08

F = set()

print("==============================================")
print("          PLANT DISEASE EXPERT SYSTEM")
print("==============================================")



print("\nAnswer the following questions with Yes or No.")

answer = input("\nDo you have spots on the leaves? (yes/no): ")
if answer.lower() == "yes":
    F.add("Spots_on_leaves")

answer = input("Are the leaves dried? (yes/no): ")
if answer.lower() == "yes":
    F.add("Dried_leaves")

answer = input("Do you have yellow leaves? (yes/no): ")
if answer.lower() == "yes":
    F.add("Yellow_leaves")

answer = input("Are there holes in the leaves? (yes/no): ")
if answer.lower() == "yes":
    F.add("Holes_in_leaves")



KB = [
    ({"Spots_on_leaves", "Dried_leaves"}, "Disease1"),
    ({"Disease1"}, "Pest_Attack"),
    ({"Pest_Attack"}, "Use_Pesticide"),

    ({"Yellow_leaves"}, "Nutrient_Deficiency"),
    ({"Nutrient_Deficiency"}, "Use_Fertilizer"),

    ({"Holes_in_leaves"}, "Insect_Attack"),
    ({"Insect_Attack"}, "Use_Insecticide")
]



def forward_chaining(KB, F):

    Knownfacts = set(F)

    Addednewfacts = True

    while Addednewfacts:

        Addednewfacts = False

        for antecedents, consequent in KB:

            if consequent not in Knownfacts:

                if antecedents.issubset(Knownfacts):

                    Knownfacts.add(consequent)

                    Addednewfacts = True

    return Knownfacts




def backward_chaining(KB, Knownfacts, goal):

    # Goal is already known
    if goal in Knownfacts:
        return True

    # Find a rule that concludes the goal
    for antecedents, consequent in KB:

        if consequent == goal:

            all_antecedents = True

            # Check every condition
            for fact in antecedents:

                if not backward_chaining(KB, Knownfacts, fact):

                    all_antecedents = False
                    break

            if all_antecedents:

                Knownfacts.add(goal)

                return True

    return False

print("Initial Facts:")

if len(F) == 0:

    print("No symptoms selected.")

else:

    for fact in F:
        print("-", fact)



while True:
    print("\n1. Forward Chaining")
    print("2. Backward Chaining")
    print("3. Exit")
    choice = input("\nEnter your choice: ")



    if choice == "1":


        Knownfacts = forward_chaining(KB, F)

        print("\nFinal Known Facts:")

        for fact in Knownfacts:
            print("-", fact)

        print("\nFinal Conclusion:")

        if "Use_Pesticide" in Knownfacts:

            print("Diagnosis: Pest Attack")
            print("Recommendation: Use Pesticide")

        elif "Use_Fertilizer" in Knownfacts:

            print("Diagnosis: Nutrient Deficiency")
            print("Recommendation: Use Fertilizer")

        elif "Use_Insecticide" in Knownfacts:

            print("Diagnosis: Insect Attack")
            print("Recommendation: Use Insecticide")

        else:

            print("No specific problem detected.")



    elif choice == "2":

        print("\nSelect the goal you want to prove:")

        print("1. Disease1")
        print("2. Pest Attack")
        print("3. Use Pesticide")
        print("4. Nutrient Deficiency")
        print("5. Use Fertilizer")
        print("6. Insect Attack")
        print("7. Use Insecticide")

        goal_choice = input("\nEnter your choice: ")


        if goal_choice == "1":
            goal = "Disease1"

        elif goal_choice == "2":
            goal = "Pest_Attack"

        elif goal_choice == "3":
            goal = "Use_Pesticide"

        elif goal_choice == "4":
            goal = "Nutrient_Deficiency"

        elif goal_choice == "5":
            goal = "Use_Fertilizer"

        elif goal_choice == "6":
            goal = "Insect_Attack"

        elif goal_choice == "7":
            goal = "Use_Insecticide"

        else:

            print("Invalid choice!")
            continue


        Knownfacts = set(F)

        result = backward_chaining(
            KB,
            Knownfacts,
            goal
        )


        print("\nFINAL RESULT: ")

        print("Goal:", goal)

        if result:

            print("Goal can be proved.")

        else:

            print("Goal cannot be proved.")




    elif choice == "3":

        print("     Thank you for using the system!")

        break


    else:

        print("\nInvalid choice! Please enter 1, 2 or 3.")













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
    open = deque()
    closed = set()
    parent = {}

    open.append((h[start], start))
    parent[start] = None

    while open:

        print("\n-----------------------------")
        print("OPEN List :", [(x[0], x[1]) for x in open])
        print("CLOSED List :", list(closed))

        heuristic_value, current = open.popleft()

        print("Checking Node :", current)
        print("Heuristic :", heuristic_value)

        closed.add(current)
        print("Added to CLOSED :", current)

        if current == goal:

            print("\nNode Found..")

            
            path = []
            node = goal

            while node is not None:
                path.append(node)
                node = parent[node]

            path.reverse()

            print("Path:", " -> ".join(path))

            
            cost = 0
            for node in path:
                if node != start and node != goal:
                    cost += h[node]

            return path, cost

        print("Neighbors of", current, ":", graph[current])

        for neighbour in graph[current]:

            if neighbour == '' or neighbour in closed:
                continue

            
            already_open = False

            for item in open:
                if item[1] == neighbour:
                    already_open = True
                    break

            if not already_open:
                open.append((h[neighbour], neighbour))
                parent[neighbour] = current

                print("Added to OPEN:", neighbour,
                      "(h =", h[neighbour], ")")

        
        open = deque(sorted(open, key=lambda x: x[0]))

        print("Current OPEN :", [(x[0], x[1]) for x in open])
        print("Current CLOSED :", list(closed))

    print("Failure (No Path exists)")
    return None, None

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
