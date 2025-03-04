import random
import string
import numpy as np

def generate_graph(num_vertices: int, num_edges: int, edge_file: str, vertex_file: str):
    edges = set()
    
    # Preferential attachment: probability of selecting an existing node is proportional to its degree
    degrees = np.zeros(num_vertices + 1, dtype=int)  # Track degrees
    
    while len(edges) < num_edges:
        if len(edges) < num_vertices:  # Ensure every node has at least one edge
            src = len(edges) + 1
        else:
            src = random.choices(range(1, num_vertices + 1), weights=degrees[1:], k=1)[0]
        
        dst = random.randint(1, num_vertices)
        
        if src != dst and (src, dst) not in edges:
            edges.add((src, dst))
            degrees[src] += 1
            degrees[dst] += 1
    
    # Write edges to file
    with open(edge_file, "w") as f:
        for src, dst in edges:
            f.write(f"{src} {dst}\n")
    
    # Generate skewed vertex names
    with open(vertex_file, "w") as f:
        for vertex in range(1, num_vertices + 1):
            name_length = random.choices([3, 5, 8, 12, 15], weights=[10, 30, 40, 15, 5])[0]
            name = ''.join(random.choices(string.ascii_letters, k=name_length))
            f.write(f"{vertex},{name}\n")

if __name__ == "__main__":
    num_vertices = 1000   # Adjust as needed
    num_edges = 5000      # Adjust as needed
    generate_graph(num_vertices, num_edges, "edges.txt", "vertices.txt")
    print("Uneven dataset generated: edges.txt and vertices.txt")
