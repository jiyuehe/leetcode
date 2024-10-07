import os
from collections import deque
os.system('cls')

class Graph:
    # Breadth first search
    # ----------
    # BFS from given source s
    def bfs(self, adj, s):
    
        # Create a queue for BFS
        q = deque()
        
        # Initially mark all the vertices as not visited
        # When we push a vertex into the q, we mark it as 
        # visited
        visited = [False] * len(adj);

        # Mark the source node as visited and enqueue it
        visited[s] = True
        q.append(s)

        # Iterate over the queue
        while q:
        
            # Dequeue a vertex from queue and print it
            curr = q.popleft()
            print(curr, end=" ")

            # Get all adjacent vertices of the dequeued 
            # vertex. If an adjacent has not been visited, 
            # mark it visited and enqueue it
            for x in adj[curr]:
                if not visited[x]:
                    visited[x] = True
                    q.append(x)

    # Function to add an edge to the graph
    def add_edge(self, adj, u, v):
        adj[u].append(v)
        adj[v].append(u)

    # Depth first search
    # ----------
    def dfs_rec(self, adj, visited, s):
        # Mark the current vertex as visited
        visited[s] = True

        # Print the current vertex
        print(s, end=" ")

        # Recursively visit all adjacent vertices
        # that are not visited yet
        for i in adj[s]:
            if not visited[i]:
                self.dfs_rec(adj, visited, i)


    def dfs(self, adj, s):
        visited = [False] * len(adj)
        # Call the recursive DFS function
        self.dfs_rec(adj, visited, s)

    def add_edge(self, adj, s, t):
        # Add edge from vertex s to t
        adj[s].append(t)
        # Due to undirected Graph
        adj[t].append(s)

graph = Graph()

# Number of vertices in the graph
V = 5

# Adjacency list representation of the graph
adj = [[] for _ in range(V)]

# Add edges to the graph
graph.add_edge(adj, 0, 1)
graph.add_edge(adj, 0, 2)
graph.add_edge(adj, 1, 3)
graph.add_edge(adj, 1, 4)
graph.add_edge(adj, 2, 4)

# Perform BFS traversal starting from vertex 0
print("BFS starting from 0: ")
graph.bfs(adj, 0)
print("")

V = 5

# Create an adjacency list for the graph
adj = [[] for _ in range(V)]

# Define the edges of the graph
edges = [[1, 2], [1, 0], [2, 0], [2, 3], [2, 4]]

# Populate the adjacency list with edges
for e in edges:
    graph.add_edge(adj, e[0], e[1])

source = 1
print("DFS from source:", source)
graph.dfs(adj, source)