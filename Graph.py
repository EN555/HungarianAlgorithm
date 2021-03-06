from GraphUtils import *


class Graph:

    def __init__(self):
        self.nodes: dict[int:Node] = {}
        self.edges: List[Edge] = []

    def add_node(self, node: Node) -> None:
        self.nodes.update({node.get_ID(): node})

    def connect(self, node1: int, node2: int) -> None:
        if node1 not in self.nodes.keys() or node2 not in self.nodes.keys():
            raise Exception("nodes not in graph")

        e1 = Edge(self.nodes[node1], self.nodes[node2])
        self.edges.append(e1)
        e2 = Edge(self.nodes[node2], self.nodes[node1])
        self.nodes[node1].connectedEdges.append(e1)
        self.nodes[node2].connectedEdges.append(e2)
        self.edges.append(e2)

    def set_is_in(self, src: int, dest: int, isin: bool = False):
        for edge in self.get_list_edges():
            if edge.get_src().get_ID() == src and edge.get_dest().get_ID() == dest:
                edge.set_is_in(isin)

    def check_is_in(self, src: int, dest: int):
        for edge in self.get_list_edges():
            if edge.get_src().get_ID() == src and edge.get_dest().get_ID() == dest and edge.get_is_in():
                return True
        return False

    def connect_direct(self, node1: int, node2: int) -> None:
        if node1 not in self.nodes.keys() or node2 not in self.nodes.keys():
            raise Exception("nodes not in graph")

        e = Edge(self.nodes[node1], self.nodes[node2])
        self.edges.append(e)
        self.nodes[node1].connectedEdges.append(e)
        self.nodes[node2].inEdges.append(e)

    def get_edge(self, src: Node = None, dest: Node = None) -> Edge:
        for edge in self.get_list_edges():
            if edge.get_src() == src and edge.get_dest() == dest:
                return edge
        return None

    def get_edge_by_id(self, src: int, dest: int) -> Edge:
        for edge in self.get_list_edges():
            if edge.get_src().get_ID() == src and edge.get_dest().get_ID() == dest:
                return edge
        return None

    def get_dic_nodes(self):
        return self.nodes

    def get_list_edges(self):
        return self.edges

    def num_of_nodes(self) -> int:
        return len(self.nodes)

    def num_of_edges(self) -> int:
        return len(self.edges)

    def has_edge(self, x: int, y: int):
        return self.nodes[x].is_neighbor(y)
