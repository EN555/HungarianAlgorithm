from graph_utils import *
from graph import *
from graph_utils import *
import queue


class HungarianAlgo:

    def __init__(self, graph: Graph = None):
        self.listA = []  # two set of nodes
        self.listAm = []  # A intersection with M (represent the match nodes group)
        self.listB = []
        self.listBm = []
        self.graph = graph

    def find_max_match(self):  # first function
        is_find = True
        while is_find:
            self.divide_to_set()  # first divide the graph to four groups
            is_find = self.find_m_augmenting_path()  # check if have any path from A to B
            self.listA.clear()  # delete all the the items from the lists
            self.listB.clear()
            self.listAm.clear()
            self.listBm.clear()

    def find_m_augmenting_path(self) -> bool:  # move on all the A group nodes if find so augment
        find = False
        for node in self.listA:
            self.bfs(node)
            path = self.shortest_path(node)
            if path != None: # if find path need to update the sets
                self.augment_the_path(path)
                find = True
                break
        return find

    def augment_the_path(self, path: List= None):
        for i in len(path) -1:
            if i%2 ==0:
                edge = self.graph.get_edge(path[i], path[i+1])
                edge.set_is_in("True")
            else:
                edge = self.graph.get_edge(path[i], path[i + 1])
                edge.set_is_in("False")

    def divide_to_set(self):
        # init all the nodes in the graph
        for node in self.graph.get_dic_nodes().values():
            node.set_tag1(-1)
        q = queue.Queue()

        # sort to A and B - bipartite graph
        list(self.graph.get_dic_nodes().values())[0].set_tag1(1)
        self.listA.append(list(self.graph.get_dic_nodes().values())[0])  # listA = 1
        q.put(list(self.graph.get_dic_nodes().values())[0])

        while q.empty() != True:
            node = q.get()
            for edge in node.get_list_edge():
                nei = edge.get_dest()
                if nei.get_tag1() == -1:
                    nei.set_tag1(1 - node.get_tag1())
                    q.put(nei)
                    if nei.get_tag1() == 1:
                        self.listA.append(nei)
                    else:
                        self.listB.append(nei)

        # divide A to two sets A intersection M, A and same for B
        for node in self.listA:  # insert to Am
            for edge in node.get_list_edge():
                if edge.get_is_in() == "True":
                    self.listAm.append(node)
                    self.listA.remove(node)

        for node in self.listB:  # insert to Bm
            for edge in node.get_list_edge():
                if edge.get_is_in() == "True":
                    self.listBm.append(node)
                    self.listB.remove(node)

    # move on all the Am group of nodes and return the path by bfs algorithm
    def bfs(self, src: Node = None) -> None:
        # init all the nodes
        for node in self.graph.get_dic_nodes().values():
            node.set_tag2(-1)  # represent the distance
            node.set_tag3("False")  # represent the boolean is visit

        q = queue.Queue()
        q.put(src)  # insert the src from Am
        self.src.set_tag2(0)
        self.src.set_tag3("True")  # set to visit

        while q.empty() != True:
            curr_node = q.get()
            for edge in curr_node.get_list_edge():
                nei = edge.get_dest()
                if nei.get_tag3() == "False":
                    if curr_node.get_tag2() + 1 < nei.get_tag2():
                        nei.set_tag2(curr_node.get_tag2() + 1)
                        q.put(nei)
            curr_node.set_tag3("True")

    def shortest_path(self, src: Node = None) -> list:  # if have any path return the path
        path = [src]
        curr = src
        for nei in curr.get_list_edge():
            if nei.get_dest().get_tag2() == curr.get_tag2() + 1:
                path.append(nei)
                curr = nei
        if path[-1] in self.listB:  # check of the last node in B group
            return path
        else:
            return None

    def get_listA(self):
        return self.listA

    def get_listB(self):
        return self.listB

    def get_listAm(self):
        return self.listAm

    def get_listBm(self):
        return self.listBm


if __name__ == '__main__':
    a = Node()
    b = Node()
    c = Node()
    d = Node()

    g = Graph()

    g.add_node(a), g.add_node(b), g.add_node(c), g.add_node(d)
    g.connect(1, 2)
    g.connect(1, 3)
    g.connect(1, 4)

    h = HungarianAlgo(g)
    h.divide_to_set()

    print(h.get_listA())
    print(h.get_listB())
    print(h.get_listAm())
    print(h.get_listBm())
    print()
    h.find_max_match()
