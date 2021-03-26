from graph_utils import *
from graph import *
from graph_utils import *
import queue

class HungarianAlgo:

    def __init__(self):
        self.listA = [] #two set of nodes
        self.listAm = [] # A intersection with M (represent the match nodes group)
        self.listB = []
        self.listBm = []


    def divide_to_set(self, graph: Graph =None):

        # init all the nodes in the graph
        for node in graph.get_dic_nodes().values():
            node.set_tag1(-1)
        q = queue.Queue()

        # sort to A and B - bipartite graph
        list(graph.get_dic_nodes().values())[0].set_tag1(1)
        self.listA.append(list(graph.get_dic_nodes().values())[0])    # listA = 1
        q.put(list(graph.get_dic_nodes().values())[0])

        while q.empty() != True:
            node = q.get()
            for edge in node.get_list_edge():
                nei = edge.get_dest()
                if nei.get_tag1() == -1:
                    nei.set_tag1(1- node.get_tag1())
                    q.put(nei)
                    if(nei.get_tag1()==1):
                        self.listA.append(nei)
                    else:
                        self.listB.append(nei)

        # divide A to two sets A intersction M, A and same for B

    def get_listA(self):
        return self.listA

    def get_listB(self):
        return self.listB

if __name__ == '__main__':

    a = Node()
    b = Node()
    c = Node()
    d = Node()

    g = Graph()

    g.add_node(a), g.add_node(b), g.add_node(c), g.add_node(d)
    g.connect(1,2)
    g.connect(1,3)
    g.connect(1,4)

    h = HungarianAlgo()
    h.divide_to_set(g)

    print(h.get_listA())
    print(h.get_listB())