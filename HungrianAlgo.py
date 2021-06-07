from graph_utils import *
from graph import *
from graph_utils import *
import queue
import itertools


class HungarianAlgo:

    def __init__(self, graph: Graph = None):
        self.listA = []  # A\V(M)
        self.listAm = []  # A intersection with M (represent the match nodes group)
        self.listB = []  # B\V(M)
        self.listBm = []  # B intersection with M (represent the match nodes group)
        self.graph = graph
        self.temp_graph = None  # the graph after the convert to direct graph

    """
    main function in Hungarian algo 
    """

    def find_max_match(self):  # main function
        is_find = True
        num = 0
        while is_find:
            self.divide_to_set(self.graph)  # first divide the graph to four groups Am Bm A\m B\m
            self.convert_to_direct_graph()
            self.clear_All_lists()
            self.divide_to_set(self.temp_graph)  # first divide the graph to four groups
            is_find, path = self.find_m_augmenting_path()  # check if have any path from A to B
            if is_find:
                self.augment_the_path(path)
            self.clear_All_lists()

    def find_m_augmenting_path(self) -> (bool, List):  # move on all the A group nodes if find so augment
        find = False
        path = []
        for node in self.listA:
            self.bfs(node)
            path = self.shortest_path(node)
            if path is not None:  # if find path need to update the sets
                find = True
                break
        return find, path

    def convert_to_direct_graph(self):  # create direct graph as hungarian algorithm required
        self.temp_graph = Graph()

        # copy the nodes
        for node in self.graph.get_dic_nodes().values():
            new_node = Node(side=node.get_side())
            new_node.set_ID(node.get_ID())
            self.temp_graph.add_node(new_node)

        # connect Bm to Am
        for x, y in itertools.product(self.listBm, self.listAm):
            if self.graph.has_edge(x.get_ID(), y.get_ID()) and self.graph.check_is_in(x.get_ID(), y.get_ID()):
                self.temp_graph.connect_direct(x.get_ID(), y.get_ID())
                self.temp_graph.set_is_in(x.get_ID(), y.get_ID(), True)
            elif self.graph.has_edge(x.get_ID(), y.get_ID()) and not self.graph.check_is_in(x.get_ID(), y.get_ID()):
                self.temp_graph.connect_direct(y.get_ID(), x.get_ID())

        # connect the rest
        for x, y in (itertools.chain(itertools.product(self.listA, self.listB),
                                     itertools.product(self.listA, self.listBm),
                                     itertools.product(self.listAm, self.listB))):
            if self.graph.has_edge(x.get_ID(), y.get_ID()):
                self.temp_graph.connect_direct(x.get_ID(), y.get_ID())

    def augment_the_path(self, path: List = None):  # do it for the original graph
        for i in range(0, len(path) - 1):
            edge1 = self.graph.get_edge_by_id(path[i].get_ID(), path[i + 1].get_ID())   # get edges
            edge2 = self.graph.get_edge_by_id(path[i + 1].get_ID(), path[i].get_ID())
            edge1.set_is_in(not edge1.get_is_in())  # augment
            edge2.set_is_in(not edge2.get_is_in())

    def clear_All_lists(self):
        self.listA.clear()  # delete all the the items from the lists
        self.listB.clear()
        self.listAm.clear()
        self.listBm.clear()

    def divide_to_set(self, graph: Graph = None):

        self.listA = [node for node in graph.get_dic_nodes().values() if
                      (((not any(list(map(lambda e: e.get_is_in(), node.get_list_edge())))) and
                        (not any(list(map(lambda e: e.get_is_in(), node.get_edges_in()))))) and
                       node.get_side() == "left")]
        self.listAm = [node for node in graph.get_dic_nodes().values() if
                       (((any(list(map(lambda e: e.get_is_in(), node.get_list_edge())))) or
                         (any(list(map(lambda e: e.get_is_in(), node.get_edges_in()))))) and
                        node.get_side() == "left")]
        self.listB = [node for node in graph.get_dic_nodes().values() if
                      (((not any(list(map(lambda e: e.get_is_in(), node.get_list_edge())))) and
                        (not any(list(map(lambda e: e.get_is_in(), node.get_edges_in()))))) and
                       node.get_side() == "right")]
        self.listBm = [node for node in graph.get_dic_nodes().values() if
                       (((any(list(map(lambda e: e.get_is_in(), node.get_list_edge())))) or
                         (any(list(map(lambda e: e.get_is_in(), node.get_edges_in()))))) and
                        node.get_side() == "right")]

    """
    move on all the Am group of nodes and return the path by bfs algorithm
    """

    def bfs(self, src: Node = None) -> None:
        # init all the nodes
        for node in self.temp_graph.get_dic_nodes().values():
            node.set_tag2(-1)  # represent the distance
            node.set_tag3(False)  # represent the boolean is visit

        q = queue.Queue()
        q.put(src)  # insert the src from Am
        src.set_tag2(0)
        src.set_tag3(True)  # set to visit

        while not q.empty():
            curr_node = q.get()
            for edge in curr_node.get_list_edge():
                nei = edge.get_dest()
                if not nei.get_tag3() and nei.get_tag2() == -1:
                    nei.set_tag2(curr_node.get_tag2() + 1)
                    q.put(nei)
                    nei.set_tag4(curr_node)
                else:  # visit there
                    if curr_node.get_tag2() + 1 < nei.get_tag2():
                        nei.set_tag2(curr_node.get_tag2() + 1)
                        nei.set_tag4(curr_node)
            curr_node.set_tag3(True)

    def shortest_path(self, src: Node = None) -> list:  # if have any path return the path
        path = []
        curr = None
        for node in self.listB:
            if node.get_tag2() != -1:
                curr = node
                path.append(curr)
                break
        if curr is not None:
            while curr.get_tag4() is not None:
                path.append(curr.get_tag4())
                curr = curr.get_tag4()
            path.reverse()
            return path
        return None

    def get_listA(self):
        return self.listA

    def get_listB(self):
        return self.listB

    def get_listAm(self):
        return self.listAm

    def get_listBm(self):
        return self.listBm

    ## temp functions

    def get_temp_graph(self):
        return self.temp_graph

    def get_graph(self):
        return self.graph
