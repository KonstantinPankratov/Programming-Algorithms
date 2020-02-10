class Dijkstra:

    graph = None
    costs = None
    parents = None

    processedNodes = []
    path = None

    def __init__(self, graph, costs, parents):
        self.graph = graph
        self.costs = costs
        self.parents = parents

        graph = list(self.graph)

        self.start = graph[0]
        self.end = graph[-1]
        self.__call__()

    def __call__(self):
        node = self.lowest_cost_node()
        while node is not None:
            cost = self.costs[node]
            neighbors = self.graph[node]
            for neighbor in neighbors.keys():
                new_cost = cost + neighbors[neighbor]
                if new_cost < self.costs[neighbor]:
                    self.costs[neighbor] = new_cost
                    self.parents[neighbor] = node
            self.processedNodes.append(node)
            node = self.lowest_cost_node()

    def get_graph(self):
        return self.graph

    def get_costs(self):
        return self.costs

    def get_parents(self):
        return self.parents

    def get_path(self):
        path = list()
        path.append(self.start)

        switched_parents = {v: k for k, v in self.parents.items()}
        current = self.start
        while current != self.end:
            current = switched_parents[current]
            path.append(current)

        return path

    def get_path_str(self):
        return ' > '.join(self.get_path())

    def get_length(self):
        return self.costs[self.end]

    def lowest_cost_node(self):
        lowest_cost = float('inf')
        lowest_cost_node = None
        for node in self.costs:
            cost = self.costs[node]
            if cost < lowest_cost and node not in self.processedNodes:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node
