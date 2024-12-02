"""
Greedy graph coloring algorithm
"""

def greedy_coloring(graph):
    # Dictionary to store the color assigned to each node
    coloring = {}
    # Dictionary to store nodes grouped by color (reversed coloring)
    reversed_coloring = {}
    
    # Iterate over all nodes in the graph
    for node in graph.nodes():
        # Get the colors of neighboring nodes
        neighbor_colors = {coloring[neighbor] for neighbor in graph.neighbors(node) if neighbor in coloring}
        # Assign the smallest available color
        color = 0
        while color in neighbor_colors:
            color += 1
        coloring[node] = color
        
        # Add node to the reversed coloring dictionary
        if color not in reversed_coloring:
            reversed_coloring[color] = []
        reversed_coloring[color].append(node)
    
    return coloring, reversed_coloring