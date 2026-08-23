def savings_heur_tsp(cost_matrix):
  num_nodes = len(cost_matrix)
  
  start_node = min(range(num_nodes), key=lambda i: sum(cost_matrix[i]))
  
  # 2. Calculate savings for all pairs (i, j) where i != j and neither is the start_node
  savings = []
  other_nodes = [n for n in range(num_nodes) if n != start_node]
  
  for i in other_nodes:
    for j in other_nodes:
      if i == j:
        continue
      s_val = cost_matrix[start_node][i] + cost_matrix[start_node][j] - cost_matrix[i][j]
      savings.append((s_val, i, j))
      
  # 3. Sort savings in descending order based on the savings value (x[0])
  savings.sort(key=lambda x: x[0], reverse=True)
  
  # Track the routes. Initially, every non-start_node node i has its own round trip
  routes = [[i] for i in other_nodes]
  
  def find_route(node):
    """Helper to find which partial route contains a given node."""
    for r in routes:
      if node in r:
        return r
    return None

  # 4. Merge routes based on sorted savings
  for s_val, i, j in savings:
    route_i = find_route(i)
    route_j = find_route(j)
    
    # Nodes must be in different sub-routes to be merged
    if route_i != route_j:
      # Condition: i and j must be outer endpoints of their respective paths
      i_is_end = (route_i[0] == i or route_i[-1] == i)
      j_is_end = (route_j[0] == j or route_j[-1] == j)
      
      if i_is_end and j_is_end:
        # Orient the routes so the endpoints meet: ... -> i -> j -> ...
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
        
    # Optimization: Stop early if everything is merged into one single path
    if len(routes) == 1:
      break

  # 5. Construct final TSP tour by wrapping the merged path with the chosen start_node
  final_tour = [start_node] + routes[0]
  # + [start_node]
  
  # Calculate final tour cost
  # total_cost = sum(cost_matrix[final_tour[k]][final_tour[k+1]] for k in range(len(final_tour) - 1))
  
  return final_tour
  # , total_cost, start_node

if __name__ == "__main__":
  import sys
  input_data = sys.stdin.read().strip().split("\n")
  cost_lines = input_data[(int(input_data[1]) + 2):]
  cost_matrix = [list(map(float, line.split())) for line in cost_lines]
  # , cost, selected_start_node 
  tour = savings_heur_tsp(cost_matrix)
  print(" ".join(map(str, tour)))
  # range(len(cost_matrix)))))
  # cost_matrix[0])
  """ print(f"Selected Centroid start_node: Node")
  print(f"Optimised TSP Tour: ")
  print(f"Total Travel cost: ") """
