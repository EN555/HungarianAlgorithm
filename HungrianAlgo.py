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
        self.temp_graph = None

    def find_max_match(self):  # main function
        is_find = True
        num = 0
        while is_find:
            self.divide_to_set(self.graph)  # first divide the graph to four groups
            self.convert_to_direct_graph()
            self.clear_All_lists()
            self.divide_to_set(self.temp_graph)  # first divide the graph to four groups
            is_find = self.find_m_augmenting_path()  # check if have any path from A to B
            self.clear_All_lists()

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
            if path is not None:     # if find path need to update the sets
                self.augment_the_path(path)
                find = True
                break
        return find

    def convert_to_direct_graph(self):  # create direct graph as hungarian algorithm ask
        self.temp_graph = Graph()
        # copy all the nodes from the graph
        for node in self.graph.get_dic_nodes().values():
            new_node = Node((0, 0), node.get_side())
            new_node.set_ID(node.get_ID())
            self.temp_graph.add_node(new_node)

        # move on all the A group
        for node in self.listA:  # connect all the graph
            for edge in node.get_list_edge():
                self.temp_graph.connect_direct(edge.get_src().get_ID(), edge.get_dest().get_ID())

        # move on all the  Bm group
        for node in self.listBm:  # connect all the graph
            for edge in node.get_list_edge():
              if edge.get_dest() in self.listAm and self.graph.check_is_in(edge.get_src().get_ID(), edge.get_dest().get_ID()):
                  self.temp_graph.connect_direct(edge.get_src().get_ID(), edge.get_dest().get_ID())
                  self.temp_graph.set_is_in(edge.get_src().get_ID(), edge.get_dest().get_ID(),True)

        # move on all the Am group
        for node in self.listAm:  # connect all the graph
            for edge in node.get_list_edge():
                if edge.get_dest() in self.listB:
                    self.temp_graph.connect_direct\
                        (edge.get_src().get_ID(), edge.get_dest().get_ID())

    def augment_the_path(self, path: List= None):   # do it for the original graph
        for i in range(0,len(path) -1):
            if i%2 ==0:
                edge1 = self.graph.get_edge_by_id(path[i].get_ID(), path[i+1].get_ID())
                edge1.set_is_in(True)
                edge2 = self.graph.get_edge_by_id(path[i+1].get_ID(), path[i].get_ID())
                edge2.set_is_in(True)
            else:
                edge1 = self.graph.get_edge(path[i].get_ID(), path[i + 1].get_ID())
                edge1.set_is_in(False)
                edge2 = self.graph.get_edge(path[i].get_ID(), path[i + 1].get_ID())
                edge2.set_is_in(False)

    def divide_to_set(self, graph: Graph = None):
        for node in graph.get_dic_nodes().values():
            if node.get_side() == 'left':
                self.listA.append(node)
            else:
                self.listB.append(node)
        # divide A to two sets A intersection M, A and same for B
        temp_list = []
        for node in self.listA:  # insert to Am
            for edge in node.get_list_edge():
                if edge.get_is_in():
                    self.listAm.append(node)
                    self.listBm.append(edge.get_dest())
                    temp_list.append(node)
                    self.listB.remove(edge.get_dest())
        for node in temp_list:
            self.listA.remove(node)
        temp_list.clear()

        for node in self.listB:  # insert to Bm
            for edge in node.get_list_edge():
                if edge.get_is_in():
                    self.listBm.append(node)
                    self.listAm.append(edge.get_dest())
                    temp_list.append(node)
                    self.listA.remove(edge.get_dest())
        for node in temp_list:
            self.listB.remove(node)
    # move on all the Am group of nodes and return the path by bfs algorithm
    def bfs(self, src: Node = None) -> None:
        # init all the nodes
        for node in self.temp_graph.get_dic_nodes().values():
            node.set_tag2(-1)  # represent the distance
            node.set_tag3(False)  # represent the boolean is visit

        q = queue.Queue()
        q.put(src)  # insert the src from Am
        src.set_tag2(0)
        src.set_tag3(True)  # set to visit

        while q.empty() != True:
            curr_node = q.get()
            for edge in curr_node.get_list_edge():
                nei = edge.get_dest()
                if nei.get_tag3() == False and nei.get_tag2() == -1:
                    nei.set_tag2(curr_node.get_tag2() + 1)
                    q.put(nei)
                    nei.set_tag4(curr_node)
                else:   # visit there
                    if curr_node.get_tag2() + 1 < nei.get_tag2():
                        nei.set_tag2(curr_node.get_tag2() +1)
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
        if curr != None:
            while curr.get_tag4() != None:
                path.append(curr.get_tag4())
                curr = curr.get_tag4()
                path.reverse()
                if path[-1] in self.listB:  # check of the last node in B group
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

if __name__ == '__main__':
###############
# a ----- d
# b ----- e
###############

    node1 = Node((0, 0), 0)
    node2 = Node((0, 0), 0)
    node3 = Node((0, 0), 1)
    node4 = Node((0, 0), 1)
    node5 = Node((0, 0), 1)
    node6 = Node((0, 0), 1)
    node7 = Node((0, 0), 1)
    node8 = Node((0, 0), 1)
    node9 = Node((0, 0), 1)
    node10 = Node((0, 0), 1)

    g = Graph()
    g.add_node(node1), g.add_node(node2), g.add_node(node3), g.add_node(node4), g.add_node(node5)
    g.add_node(node6), g.add_node(node7), g.add_node(node8), g.add_node(node9), g.add_node(node10)
    g.connect(0, 2)
    g.connect(0, 3)
    g.connect(0, 4)
    g.connect(0, 5)
    g.connect(0, 6)
    g.connect(0, 7)
    g.connect(0, 9)
    g.connect(1, 3)
    g.connect(1, 4)
    g.connect(1, 5)
    g.connect(1, 6)
    g.connect(1, 7)

    h = HungarianAlgo(g)
    h.find_max_match()


######################################
    print("The result is: ")
    for edge in h.get_graph().get_list_edges():
        print(str(edge) + " " + str(edge.get_is_in()))
#####################################




