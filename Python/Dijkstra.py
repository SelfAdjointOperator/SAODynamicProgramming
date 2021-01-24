"""
We are given a connected graph G and a vertex v of G.
The edges of G are labelled with weights (distances).
For each vertex w of G we want to find the shortest length path from v to w, where travelling by an edge adds its weight to the total distance of that path.
We do this by at each step 'confirming' the vertex with the current shortest known distance from the vertices we have explored so far;
Any new shortest path must pass through our confirmed-shortest-paths vertices, hence to obtain the next shortest path we must travel at least as far as the smallest unconfirmed-shortest-path, as any other path to this vertex is at least as long as this length and another edge >=0.

We input our graph G as an adjacency array, with entries corresponding to edge weights >=0. This is a symmetric array.
For a pair of vertices for which no edge between them exists our array entry should be -1.

TODO: Consider handling Dijkstra for graphs with more than one connected component.

"""

class Graph():
    def __init__(self, adjacencyArray):
        self.adjacencyArray = adjacencyArray
        self.graphOrder = len(self.adjacencyArray)

    def dijkstra(self, startVertex = 0):
        """Returns a 2-tuple: an array of the shortest path lengths from $startvertex, and an array whose i'th entry is the previous vertex in the shortest path to that vertex (the entry for $startVertex is None)"""
        pathLengths = [-1 for _ in range(self.graphOrder)]
        previousVertexInPath = [None for _ in range(self.graphOrder)]
        verticesToDo = list(range(self.graphOrder))

        pathLengths[startVertex] = 0

        while verticesToDo:
            vertexDoing = min([[pathLengths[v], v] for v in verticesToDo if pathLengths[v] != -1])[1]
            verticesToDo.remove(vertexDoing)
            for vertex in [v for v in verticesToDo if self.adjacencyArray[vertexDoing][v] != -1]:
                smallerPathLength = pathLengths[vertexDoing] + self.adjacencyArray[vertexDoing][vertex]
                if pathLengths[vertex] == -1 or smallerPathLength < pathLengths[vertex]:
                    pathLengths[vertex] = smallerPathLength
                    previousVertexInPath[vertex] = vertexDoing

        return pathLengths, previousVertexInPath

    def shortestPath(self, startVertex, endVertex):
        """Returns a 2-tuple: the list of vertices from $startVertex to $endVertex that form the shortest path, and the length of this path"""
        pathLengths, previousVertexInPath = self.dijkstra(startVertex = startVertex)

        shortestPathList = [endVertex]
        while True:
            previousVertex = previousVertexInPath[shortestPathList[-1]]
            if previousVertex is not None:
                shortestPathList.append(previousVertex)
            else:
                shortestPathList.reverse()
                return shortestPathList, pathLengths[endVertex]

if __name__ == "__main__":
    G = Graph([[-1, 7, 4, 2,-1],
               [ 7,-1, 9, 1, 8],
               [ 4, 9,-1, 8, 2],
               [ 2, 1, 8,-1, 5],
               [-1, 8, 2, 5,-1]])
    print(G.dijkstra(1))
    print(G.shortestPath(1,2))
