from typing import List


class Node:
    __idCounter = 0

    def __init__(self, cords=(0, 0), side=None):
        self.id: int = Node.__idCounter
        Node.__idCounter += 1
        self.connectedEdges: List[Edge] = []
        self.cords = cords
        self.side = side       #bipartide graph
        self.tag1: any = None  # for algorithms
        self.tag2: any = None  # for algorithms
        self.tag3: any = None  # for algorithms
        self.tag4: any = None  # for algorithms

    def get_ID(self):
        return self.id

    def set_ID(self, ID: int):
        self.id = ID

    def get_list_edge(self):
        return self.connectedEdges

    def set_tag1(self, tag: any = None):
        self.tag1 = tag

    def set_tag2(self, tag: any = None):
        self.tag2 = tag

    def get_tag1(self):
        return self.tag1

    def get_tag2(self):
        return self.tag2

    def set_tag3(self, tag: any = None):
        self.tag3 = tag

    def get_tag3(self):
        return self.tag3

    def __str__(self):
        return "The ID is: "  + str(self.id)

    def __repr__(self):
        return "The ID is: "  + str(self.id)

class Edge:

    def __init__(self, src: Node, dest: Node):
        self.src = src
        self.dest = dest
        self.isInMatch = False

    def get_src(self):
        return self.src

    def get_dest(self):
        return self.dest

    def get_is_in(self):
        return self.isInMatch

    def set_is_in(self,isIn: bool= False):
        self.isInMatch = isIn

    def __str__(self):
        return "The src is: " + str(self.src) + " The dest is: " + str(self.dest)

    def __repr__(self):
        return "The src is: " + str(self.src) + " The dest is: " + str(self.dest)