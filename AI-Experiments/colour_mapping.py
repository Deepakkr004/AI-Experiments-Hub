import matplotlib.pyplot as plt
import networkx as nx
import seaborn as sns

# Function to check if current color assignment is valid
def is_valid(assignment, country, color, neighbors):
    for neighbor in neighbors[country]:
        if assignment[neighbor] == color:
            return False
    return True

# Backtracking function to solve the CSP
def solve_map_coloring(assignment, countries, colors, neighbors):
    # If all countries are assigned a color, return the assignment
    if all(assignment[country] is not None for country in countries):
        return assignment

    # Select an unassigned country
    unassigned = [country for country in countries if assignment[country] is None]
    country = unassigned[0]

    # Try each color for the country
    for color in colors:
        if is_valid(assignment, country, color, neighbors):
            # Assign the color
            assignment[country] = color
            
            # Recursively try to solve the rest of the map
            result = solve_map_coloring(assignment, countries, colors, neighbors)
            if result:
                return result
            
            # If it doesn't lead to a solution, backtrack
            assignment[country] = None

    return None

# Function to visualize the solution
def visualize_map_coloring(solution, neighbors):
    # Create a graph
    G = nx.Graph()

    # Add nodes (countries) to the graph
    for country in solution:
        G.add_node(country)

    # Add edges (neighbors) to the graph
    for country, neighbors_list in neighbors.items():
        for neighbor in neighbors_list:
            G.add_edge(country, neighbor)

    # Define position layout for nodes (countries)
    pos = nx.spring_layout(G)

    # Use seaborn color palette for the countries
    unique_colors = list(set(solution.values()))
    palette = sns.color_palette("Set1", len(unique_colors))
    color_map = {color: palette[i] for i, color in enumerate(unique_colors)}
    
    # Node colors based on solution
    node_colors = [color_map[solution[country]] for country in G.nodes]

    # Draw the graph
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color=node_colors, node_size=2000, font_size=12, font_weight='bold', edge_color='black', linewidths=1, font_color='white')

    # Create legend for colors
    legend_labels = [plt.Line2D([0], [0], marker='o', color='w', label=color, markerfacecolor=color_map[color], markersize=10) for color in unique_colors]
    plt.legend(handles=legend_labels, title="Colors")

    plt.title("Map Coloring Solution", fontsize=16)
    plt.show()

def main():
    # Define the countries (nodes) of the map
    countries = ['France', 'Germany', 'Italy', 'Switzerland', 'Austria']
    
    # Define the neighbors (edges between countries)
    neighbors = {
        'France': ['Germany', 'Switzerland', 'Italy'],
        'Germany': ['France', 'Switzerland', 'Austria'],
        'Italy': ['France', 'Switzerland', 'Austria'],
        'Switzerland': ['France', 'Germany', 'Italy', 'Austria'],
        'Austria': ['Germany', 'Italy', 'Switzerland']
    }

    # Define the available colors
    colors = ['Red', 'Green', 'Blue']

    # Initialize an empty assignment (no country has a color yet)
    assignment = {country: None for country in countries}

    # Solve the map coloring problem
    solution = solve_map_coloring(assignment, countries, colors, neighbors)
    
    # Output the solution
    if solution:
        print("Solution found:")
        for country, color in solution.items():
            print(f"Country {country}: {color}")
        
        # Visualize the solution
        visualize_map_coloring(solution, neighbors)
    else:
        print("No solution exists")

if __name__ == "__main__":
    main()
