from graph_utils import *


class Graph:

    def __init__(self):
        self.nodes: dict[int:Node] = {}
        self.edges: List[Edge] = []

    def add_node(self, node: Node = Node()) -> None:
        self.nodes.update({node.id: node})

    def connect(self, node1: int, node2: int) -> None:
        if node1 not in self.nodes.keys() or node2 not in self.nodes.keys():
            raise Exception("nodes not in graph")

        e = Edge(self.nodes[node1], self.nodes[node2])
        self.edges.append(e)
        self.nodes[node1].connectedEdges.append(e)
        self.nodes[node2].connectedEdges.append(e)

    def get_dic_nodes(self):
        return self.nodes

    def get_list_edges(self):
        return self.edges

    def num_of_nodes(self) -> int:
        return len(self.nodes)

    def num_of_edges(self) -> int:
        return len(self.edges)
