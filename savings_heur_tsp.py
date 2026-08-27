import sys, random, time
  
# Edge-Savings heuristic algorithm for travelling-salesman-problem.
def savings_heur_tsp(cost_matrix):
  num_nodes = len(cost_matrix)
  MAX_ITERATIONS = 150
  MAX_EXECUTION_TIME = 50

  # Find the starting-node with the minimum total-cost to all other nodes
  # start_node = min(range(num_nodes), key=lambda i: sum(cost_matrix[i]))
  
  # Calculate total costs for each node
  node_costs = [(i, sum(row)) for i, row in enumerate(cost_matrix)]

  # Sort nodes by total cost in ascending order
  sorted_nodes = sorted(node_costs, key=lambda x: x[1], reverse=False)
  
  min_tour_cost = 0
  tour_cost = 0
  start_time = time.time()
  final_tour = []

  # Select node with the minimum total cost
  for i in range(min(MAX_ITERATIONS, num_nodes)):
    if (time.time() - start_time) > MAX_EXECUTION_TIME:
      break
    if i and i%4==2 and len(sorted_nodes) > 1:
      # Random-exploration element in search-strategy
      start_node = sorted_nodes.pop(random.randint(1, (len(sorted_nodes) - 1)))[0]
    elif i and i%4==3:
      start_node = sorted_nodes.pop()[0]
    elif i and i%4==0:
      start_node = sorted_nodes.pop(int(len(sorted_nodes)/2))[0]
    else:
      start_node = sorted_nodes.pop(0)[0]
    
    # Construct a tour starting from the selected node
    (final_tour, tour_cost) = construct_tour(start_node, cost_matrix)
    
    if (not min_tour_cost) or (tour_cost < min_tour_cost):
      min_tour_cost = tour_cost
      # print("Tour-cost: ", tour_cost, ", Start-node: ", start_node)
      print(" ".join(map(str, final_tour)))

    del final_tour, tour_cost
    final_tour = []
    tour_cost = 0

# Construct a tour using the savings-heuristic, starting from a given node
def construct_tour(start_node, cost_matrix):
  # Calculate savings for all pairs (i, j) where i != j
  savings = []
  other_nodes = [n for n in range(num_nodes) if n != start_node]
  
  for i in other_nodes:
    for j in other_nodes:
      if i == j:
        continue
      s_val = cost_matrix[i][start_node] + cost_matrix[start_node][j] - cost_matrix[i][j]
      savings.append((s_val, i, j))
      
  del other_nodes
  other_nodes = []
  
  # Sort savings in descending-order
  savings.sort(key=lambda x: x[0], reverse=True)
  
  # in and out edge-counts of each node
  for i in range(num_nodes):
    cost_matrix[i].extend([1, 1])
    # cost_matrix[i].append(1)
  cost_matrix[start_node][-2] = 0
  cost_matrix[start_node][-1] = 0
  
  # tour_node_counts = [[i, 2] for i in other_nodes]
  tour_edges = []
  final_tour = []
  sub_tour = []
  tour_edges_copy = []
  # print(cost_matrix)
  
  # Choose valid-edges based on savings, to build the valid-tour
  for s_val, i, j in savings:
    if len(tour_edges) >= (num_nodes - 2):
      break
    
    # Each node should have only two edges
    if (cost_matrix[i][-2] < 1) or (cost_matrix[j][-1] < 1):
      continue
    if (j, i) in tour_edges:
      continue
    # (i, j) in tour_edges or 
    
    if (cost_matrix[i][-1] < 1) and (cost_matrix[j][-2] < 1):
      # Check if adding this edge would create a cycle (except for the final edge)
      tour_edges_copy = tour_edges[:]
      # + [(i, j)]
      # tour_edges_copy.append((i, j))
      
      sub_tour = []
      nextnode = j
      while i != nextnode:
        nextindex = next((k for k, edge in enumerate(tour_edges_copy) if edge[0] == nextnode), None)
        if nextindex is None:
          sub_tour.clear()
          break
        nextnode = tour_edges_copy[nextindex][1]
        sub_tour.append(nextnode)
        # sub_tour[-1]
      if sub_tour:
        continue
        
      # for edge in tour_edges_copy:
        # edge[0], edge[1]]
        # tour_edges_copy.pop(0)
        # sub_tour[-1]
        # sub_tour[0] 
    
    # Add the tour-edge and decrease the in and out edge-counts of the nodes
    tour_edges.append((i, j))
    cost_matrix[i][-2] -= 1
    cost_matrix[j][-1] -= 1
    # print(tour_edges)
  
  # print(cost_matrix)
  del savings, sub_tour, tour_edges_copy
  sub_tour = []
  savings = []
  tour_edges_copy = []
  
  # Add the final edges to complete the valid-tour
  indexi = next((i for i, row in enumerate(cost_matrix) if row[-2] > 0))
  indexj = next((j for j, row in enumerate(cost_matrix) if row[-1] > 0))
  tour_edges.extend([(indexi, start_node), (start_node, indexj)])
  
  # print(tour_edges)
  # tour_edges.append
  # print(savings)
  
  # Build the final-tour nodes-list from the tour-edges
  final_tour.extend(tour_edges[0])
  while len(final_tour) < num_nodes:
    nextnode = final_tour[-1]
    nextindex = next((i for i, edge in enumerate(tour_edges) if edge[0] == nextnode))
    final_tour.append(tour_edges[nextindex][1])
    # print(tour_edges)
    
  # final_tour.pop()
  # append(start_node)
  del tour_edges
  tour_edges = []
  # print(len(final_tour), num_nodes, sep=", ")

  # Calculate the total cost of the generated-tour
  tour_cost = sum(cost_matrix[(final_tour[k])][(final_tour[k+1])] for k in range(len(final_tour) - 1))
  # Add cost to return to start node
  tour_cost += cost_matrix[(final_tour[-1])][(final_tour[0])]
  
  del cost_matrix
  cost_matrix = []

  return final_tour, tour_cost

if __name__ == "__main__":
  input_data = sys.stdin.read().strip().split("\n")
  num_nodes = int(input_data[1])
  # print(len(input_data))
  # print(input_data[-1])
  
  # Initial-backup valid-tour
  # print(" ".join(map(str, range(num_nodes))))
  # Cost-matrix in the input-data
  cost_lines = input_data[(num_nodes + 2):]
  
  del input_data
  input_data = []
  
  # Cost-matrix values
  cost_matrix = [list(map(float, line.split())) for line in cost_lines]
  
  del cost_lines
  cost_lines = []
  
  savings_heur_tsp(cost_matrix)
  
  del cost_matrix
  cost_matrix = []
  
  # print(" ".join(map(str, tour)))
  
  # del tour
  # tour = []
