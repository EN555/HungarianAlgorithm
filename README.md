This is an implementation of the Hungarian method for finding a perfect matching in a bipartite graphs, and a visual representation of the algorithm work, step-by-step.

the project has three parts:
graph.py, graph_utils.py - a simple implementation of an not-weighted graph. the graph can be use as both directed and un-directed, by using the matching methods: 'connect' or 'connect_direct'. 
it is up to the user to make sure he is using the right methods.

HungarianAlgo.py - an implementation of the Hungarian method, using the graph from graph.py, graph_utils.py.
in order to use this, the user need to construct a  bipartite graph using graph.py, graph_utils.py, and then create an instance of HungarianAlgo class, 
giving the graph as parameter in the constructor. to run the algorithm, the method 'find_max_match' need to be called.

GUI.py, Algo_GUI.py - this provides a friendly GUI for constructing a bipartite graph, and visualizing the algorithm work on it. 
the GUI can be run by simply executing the GUI.py file ("python GUI.py" in cmd).
 note: you need the libraries 'PySimpleGUI' and 'pyautogui' to be installed on your computer. you can run 'pip install PySimpleGUI' and 'pip install pyautogui' in cmd to install them.
