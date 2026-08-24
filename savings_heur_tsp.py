# Edge-Savings heuristic algorithm for travelling-salesman-problem.
def savings_heur_tsp(cost_matrix):
  num_nodes = len(cost_matrix)
  
  # Find the starting-node with the minimum total-cost to all other nodes
  start_node = min(range(num_nodes), key=lambda i: sum(cost_matrix[i]))
  
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
  
  del cost_matrix
  cost_matrix = []
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
  
  return final_tour
  
  ''' # Track the routes.
  routes = [[i] for i in other_nodes]
  
  def find_route(node):
    # Helper to find which partial route contains a given node.
    for r in routes:
      if node in r:
        return r
    return None

  # Merge routes based on sorted savings
  for s_val, i, j in savings:
    route_i = find_route(i)
    route_j = find_route(j)
    
    # Nodes must be in different sub-routes to be merged
    if route_i != route_j:
      # Condition: i and j must be outer endpoints of their respective paths
      i_is_end = (route_i[0] == i or route_i[-1] == i)
      j_is_end = (route_j[0] == j or route_j[-1] == j)
      
      if i_is_end and j_is_end:
        if route_i[-1] == i:
          part_1 = route_i
        else:
          part_1 = route_i[::-1] # Reverse if i was at the start
          
        if route_j[0] == j:
          part_2 = route_j
        else:
          part_2 = route_j[::-1] # Reverse if j was at the end
        
        # Merge the two list structures
        new_route = part_1 + part_2
        routes.remove(route_i)
        routes.remove(route_j)
        routes.append(new_route)
    
    if len(routes) == 1:
      break

  final_tour = [start_node] + routes[0] '''

if __name__ == "__main__":
  import sys
  input_data = sys.stdin.read().strip().split("\n")
  num_nodes = int(input_data[1])
  # print(len(input_data))
  # print(input_data[-1])
  
  # Initial-backup valid-tour
  print(" ".join(map(str, range(num_nodes))))
  # Cost-matrix in the input-data
  cost_lines = input_data[(num_nodes + 2):]
  
  del input_data
  input_data = []
  
  # Cost-matrix values
  cost_matrix = [list(map(float, line.split())) for line in cost_lines]
  
  del cost_lines
  cost_lines = []
  
  tour = savings_heur_tsp(cost_matrix)
  
  del cost_matrix
  cost_matrix = []
  
  print(" ".join(map(str, tour)))
  
  del tour
  tour = []
  # range(len(cost_matrix)))))
