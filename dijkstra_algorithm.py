max_number = 9999999


class Graph():
    def __init__(self, vertices):
        self.Vert = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def min_distance(self, distance, node_set):
        min = max_number

        for vertex in range(self.Vert):
            if distance[vertex] < min and node_set[vertex] is False:
                min = distance[vertex]
                min_index = vertex

        return min_index

    def printSolution(self, dist):
        print("Vertex \tDistance from Source")
        for node in range(self.Vert):
            print(node, "\t", dist[node])

    def dijkstra(self, source):
        distance = [max_number] * self.Vert
        distance[source] = 0
        node_set = [False] * self.Vert

        for count in range(self.Vert):
            x = self.min_distance(distance, node_set)

            node_set[x] = True

            for y in range(self.Vert):
                if self.graph[x][y] > 0 and node_set[y] is False and distance[y] > distance[x] + self.graph[x][y]:
                    distance[y] = distance[x] + self.graph[x][y]

        self.printSolution(distance)


if __name__ == "__main__":
    g = Graph(9)
    g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
               [4, 0, 8, 0, 0, 0, 0, 11, 0],
               [0, 8, 0, 7, 0, 4, 0, 0, 2],
               [0, 0, 7, 0, 9, 14, 0, 0, 0],
               [0, 0, 0, 9, 0, 10, 0, 0, 0],
               [0, 0, 4, 14, 10, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 2, 0, 1, 6],
               [8, 11, 0, 0, 0, 0, 1, 0, 7],
               [0, 0, 2, 0, 0, 0, 6, 7, 0]
               ]

    g.dijkstra(0)