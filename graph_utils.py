from typing import List


class Node:
    __idCounter = 1

    def __init__(self):
        self.id: int = Node.__idCounter
        Node.__idCounter += 1
        self.connectedEdges: List[Edge] = []
        self.tag1: any = None  # for algorithms
        self.tag2: any = None  # for algorithms


class Edge:

    def __init__(self, src: Node, dest: Node):
        self.src = src
        self.dest = dest
