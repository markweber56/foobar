from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def BFS(self, s):

        visited = [False] * (max(self.graph) + 1)

        queue = []

        # mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        while queue:
            # Dequeue a vertex from queue and print it
            s = queue.pop(0)
            print(s, end=" ")

            # get all adjacent vertices of the
            # dequeued vertex s. If an adjacent
            # has not been visited, then mark it
            # visited and enqueue it
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True

if __name__ == '__main__':
    edges = [(0,1),(0,2),(1,2),(2,0),(2,3),(3,3)]
    g = Graph()
    for v1, v2 in edges:
        g.addEdge(v1, v2)
    print('graph: ',g)
    print()
    g.BFS(2)
