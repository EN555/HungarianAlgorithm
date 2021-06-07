from Algo_GUI import *
from Graph import *
from GraphUtils import *
from HungrianAlgo import *
from GUI import *

if __name__ == '__main__':
    g = Graph()

    frame_height = 10000  # how many pixels to divide the frame to
    frame_width = 10000
    left_line = frame_width // 4
    right_line = (3 * frame_width) // 4
    radius = frame_width // 50
    gap = radius // 2
    max_nodes_on_side = frame_height // (radius + gap)
    nodes_on_right = 0
    nodes_on_left = 0

    h = frame_height - gap - (radius + gap) * nodes_on_left
    node = Node((left_line + radius // 2, h - radius // 2), side='left')
    g.add_node(node)
    nodes_on_left += 1

    h = frame_height - gap - (radius + gap) * nodes_on_left
    node = Node((left_line + radius // 2, h - radius // 2), side='left')
    g.add_node(node)
    nodes_on_left += 1

    h = frame_height - gap - (radius + gap) * nodes_on_right
    node = Node((right_line + radius // 2, h - radius // 2), side='right')
    g.add_node(node)
    nodes_on_right += 1

    h = frame_height - gap - (radius + gap) * nodes_on_right
    node = Node((right_line + radius // 2, h - radius // 2), side='right')
    g.add_node(node)
    nodes_on_right += 1

    g.connect(0, 2)
    g.connect(0, 3)
    g.connect(1, 2)

    algo_gui(g)



