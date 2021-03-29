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
        self.temp_graph= None

    def find_max_match(self):  # main function
        is_find = True
        num =0
        while is_find and num<2:
            self.divide_to_set(self.graph)  # first divide the graph to four groups
            self.convert_to_direct_graph()
            self.clear_All_lists()
            self.divide_to_set(self.temp_graph)  # first divide the graph to four groups
            is_find = self.find_m_augmenting_path()  # check if have any path from A to B
            self.clear_All_lists()
            num+=1

    def clear_All_lists(self):
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

    def convert_to_direct_graph(self):  # create direct graph as hungarian algorithm ask
        self.temp_graph = Graph()

        # copy all the nodes from the graph
        for node in self.graph.get_dic_nodes().values():
            new_node= Node()
            new_node.set_ID(node.get_ID())
            self.temp_graph.add_node(new_node)

        # move on all the A group
        for node in self.listA: # connect all the graph
            for edge in node.get_list_edge():
                self.temp_graph.connect_direct(edge.get_src().get_ID(), edge.get_dest().get_ID())

        # move on all the  Bm group
        for node in self.listBm:  # connect all the graph
            for edge in node.get_list_edge():
              if edge.get_dest() in self.listAm:
                  self.temp_graph.connect(edge.get_src().get_ID(), edge.get_dest().get_ID())

        # move on all the Am group
        for node in self.listBm:  # connect all the graph
            for edge in node.get_list_edge():
                if edge.get_dest() in self.listB:
                    self.temp_graph.connect(edge.get_src().get_ID(), edge.get_dest().get_ID())

    def augment_the_path(self, path: List= None):   # do it for the original graph
        for i in range(0,len(path) -1):
            if i%2 ==0:
                edge1 = self.graph.get_edge_by_id(path[i].get_ID(), path[i+1].get_ID())
                edge1.set_is_in("True")
                edge2 = self.graph.get_edge_by_id(path[i+1].get_ID(), path[i].get_ID())
                edge2.set_is_in("True")
            else:
                edge1 = self.graph.get_edge(path[i].get_ID(), path[i + 1].get_ID())
                edge1.set_is_in("False")
                edge2 = self.graph.get_edge(path[i].get_ID(), path[i + 1].get_ID())
                edge2.set_is_in("False")

    def divide_to_set(self, graph: Graph = None):
        # init all the nodes in the graph
        for node in graph.get_dic_nodes().values():
            node.set_tag1(-1)
        q = queue.Queue()

        # sort to A and B - bipartite graph
        list(graph.get_dic_nodes().values())[0].set_tag1(1)
        self.listA.append(list(graph.get_dic_nodes().values())[0])  # listA = 1
        q.put(list(graph.get_dic_nodes().values())[0])

        for uncheck in graph.get_dic_nodes().values():
            if uncheck.get_tag1() == -1:
                uncheck.set_tag1(1)
                self.listA.append(uncheck)  # listA = 1
                q.put(uncheck)
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
        for node in self.temp_graph.get_dic_nodes().values():
            node.set_tag2(-1)  # represent the distance
            node.set_tag3("False")  # represent the boolean is visit

        q = queue.Queue()
        q.put(src)  # insert the src from Am
        src.set_tag2(0)
        src.set_tag3("True")  # set to visit

        while q.empty() != True:
            curr_node = q.get()
            for edge in curr_node.get_list_edge():
                nei = edge.get_dest()
                if nei.get_tag3() == "False" and nei.get_tag2() == -1:
                    nei.set_tag2(curr_node.get_tag2() + 1)
                    q.put(nei)
                else:   # visit there
                    if curr_node.get_tag2() + 1 < nei.get_tag2():
                        nei.set_tag2(curr_node.get_tag2() +1)
            curr_node.set_tag3("True")

    def shortest_path(self, src: Node = None) -> list:  # if have any path return the path
        path = [src]
        curr = src
        for nei in curr.get_list_edge():
            if nei.get_dest().get_tag2() == curr.get_tag2() + 1:
                path.append(nei.get_dest())
                curr = nei.get_dest()
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

    ## temp functions

    def get_temp_graph(self):
        return self.temp_graph

    def get_graph(self):
        return self.graph

if __name__ == '__main__':
###############
# a ----- d
# b ----- e
# c ----- f
###############

    a = Node()
    b = Node()
    c = Node()
    d = Node()
    # e = Node()
    # f = Node()

    g = Graph()

    g.add_node(a), g.add_node(b), g.add_node(c), g.add_node(d)\
    # , g.add_node(e), g.add_node(f)

    g.connect(1, 4)
    g.connect(2, 3)
    # g.connect(3, 6)

    h = HungarianAlgo(g)
    # print(h.get_listA())
    # print(h.get_listB())
    # print(h.get_listAm())
    # print(h.get_listBm())
    h.find_max_match()
    print(h.get_listA())
    print(h.get_listB())
    print(h.get_listAm())
    print(h.get_listBm())



