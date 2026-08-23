def savings_heur_tsp(cost_matrix):
  num_nodes = len(cost_matrix)
  
  start_node = min(range(num_nodes), key=lambda i: sum(cost_matrix[i]))
  
  # Calculate savings for all pairs (i, j) where i != j
  savings = []
  other_nodes = [n for n in range(num_nodes) if n != start_node]
  
  for i in other_nodes:
    for j in other_nodes:
      if i == j:
        continue
      s_val = cost_matrix[start_node][i] + cost_matrix[start_node][j] - cost_matrix[i][j]
      savings.append((s_val, i, j))
      
  # Sort savings in descending-order
  savings.sort(key=lambda x: x[0], reverse=True)
  
  tour_nodes = [[i, 2] for i in other_nodes]
  tour_edges = []
  final_tour = []
  for s_val, i, j in savings:
    if len(tour_edges) >= (num_nodes - 2):
      break
    # Check if adding this edge would create a cycle (except for the final edge)
    if tour_nodes[i][1] <= 0 and tour_nodes[j][1] <= 0:
      continue
    if [i, j] in tour_edges or [j, i] in tour_edges:
      continue
    
    tour_edges.append([i, j])
    tour_nodes[i][1] -= 1
    tour_nodes[j][1] -= 1
  
  for edge in tour_edges:
    if not final_tour:
      final_tour.extend(edge)
    else:
      if edge[0] == final_tour[-1]:
        final_tour.append(edge[1])
      elif edge[1] == final_tour[-1]:
        final_tour.append(edge[0])
      elif edge[0] == final_tour[0]:
        final_tour.insert(0, edge[1])
      elif edge[1] == final_tour[0]:
        final_tour.insert(0, edge[0])
      
  final_tour.append(start_node)
  
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
  cost_lines = input_data[(int(input_data[1]) + 2):]
  cost_matrix = [list(map(float, line.split())) for line in cost_lines]
  tour = savings_heur_tsp(cost_matrix)
  print(" ".join(map(str, tour)))
  # range(len(cost_matrix)))))
