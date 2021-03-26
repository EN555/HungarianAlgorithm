from typing import List


class Node:
    __idCounter = 0

    def __init__(self):
        self.id: int = Node.__idCounter
        Node.__idCounter += 1
        self.connectedEdges: List[Edge] = []
        self.tag1: any = None  # for algorithms
        self.tag2: any = None  # for algorithms
        self.tag3: any = None  # for algorithms
        self.tag4: any = None  # for algorithms

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

    def __str__(self):
        return "The ID is: "  + str(self.id)

    def __repr__(self):
        return "The ID is: "  + str(self.id)

class Edge:

    def __init__(self, src: Node, dest: Node):
        self.src = src
        self.dest = dest

    def get_src(self):
        return self.src

    def get_dest(self):
        return self.dest
