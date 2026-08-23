def clarke_wright_savings_tsp(distance_matrix):
    num_nodes = len(distance_matrix)
    
    # 1. Dynamically select the central hub (centroid node)
    # The node with the minimum sum of distances to all other nodes 
    # also has the lowest average distance.
    hub = min(range(num_nodes), key=lambda i: sum(distance_matrix[i]))
    
    # 2. Calculate savings for all pairs (i, j) where i != j and neither is the hub
    savings = []
    non_hub_nodes = [n for n in range(num_nodes) if n != hub]
    
    for idx, i in enumerate(non_hub_nodes):
        for j in non_hub_nodes[idx + 1:]:
            # Formula: S_ij = d(hub, i) + d(hub, j) - d(i, j)
            s_val = distance_matrix[hub][i] + distance_matrix[hub][j] - distance_matrix[i][j]
            savings.append((s_val, i, j))
            
    # 3. Sort savings in descending order based on the savings value (x[0])
    savings.sort(key=lambda x: x[0], reverse=True)
    
    # Track the routes. Initially, every non-hub node i has its own round trip
    routes = [[i] for i in non_hub_nodes]
    
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

    # 5. Construct final TSP tour by wrapping the merged path with the chosen hub
    final_tour = [hub] + routes[0] + [hub]
    
    # Calculate final tour cost
    total_cost = sum(distance_matrix[final_tour[k]][final_tour[k+1]] for k in range(len(final_tour) - 1))
    
    return final_tour, total_cost, hub


# --- Example Usage ---
if __name__ == "__main__":
    # Example symmetric distance matrix (5 cities: 0, 1, 2, 3, 4)
    matrix = [,  # Distances from Node 0,  # Distances from Node 1,  # Distances from Node 2,  # Distances from Node 3
        [18, 14, 22, 13, 0]   # Distances from Node 4
    ]
    
    tour, cost, selected_hub = clarke_wright_savings_tsp(matrix)
    
    print(f"Selected Centroid Hub: Node {selected_hub}")
    print(f"Optimised TSP Tour: {' -> '.join(map(str, tour))}")
    print(f"Total Travel Distance: {cost} km")
