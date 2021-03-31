This is an implementation of the hungrian method for finding a perfect matching in a bipartite graphs, and a visual representation of the algorithm work, step-by-step.

the project has three parts:
graph.py, graph_utils.py - a simple implementation of a graph. the graph can be use as both directed and un-directed, by using the matching methods. 
it is up to the user to make sure he is using the right methods.

HumgrianAlgo.py - an implementation of the hungrian method, using the graph from graph.py, graph_utils.py.
in order to use this, the user need to constract a  bipartite graph using graph.py, graph_utils.py, and then create an instance of HungarianAlgo class, 
givinig the graph as parameter in the constractor. to run the algorighm, the method 'find_max_match' need to be called.

GUI.py, Algo_GUI.py - this provide a friendly GUI for constracting a bipartite graph, and visualizing the algorighm work on it. 
the GUI can be run by simply executing the GUI.py file ("python GUI.py" in cmd).
