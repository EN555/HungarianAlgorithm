### Hungarian Algorithm 

This is an implementation of the Hungarian method for finding a perfect matching in a **bipartite** graphs, and a visual representation of the algorithm work, step-by-step.

The project has three parts:

**[graph.py](https://github.com/EN555/HungarianAlgorithm/blob/master/graph.py), [graph_utils.py](https://github.com/EN555/HungarianAlgorithm/blob/master/graph_utils.py)** - a simple implementation of an not-weighted graph. The graph can be use as both directed and un-directed, by using the matching methods: 'connect' or 'connect_direct'. 
it is up to the user to make sure he is using the right methods.

**[HungarianAlgo.py](https://github.com/EN555/HungarianAlgorithm/blob/master/HungrianAlgo.py)** - an implementation of the Hungarian method, using the graph from graph.py, graph_utils.py.
in order to use this, the user need to construct a  bipartite graph using graph.py, graph_utils.py, and then create an instance of HungarianAlgo class, giving the graph as parameter in the constructor. To run the algorithm, the method 'find_max_match' need to be called.

**[GUI.py](https://github.com/EN555/HungarianAlgorithm/blob/master/GUI.py), [Algo_GUI.py](https://github.com/EN555/HungarianAlgorithm/blob/master/Algo_GUI.py)** - this provides a friendly GUI for constructing a bipartite graph, and visualizing the algorithm work on it.

The GUI can be run by simply executing the GUI.py file ("python GUI.py" in cmd).

 Note: you need the libraries 'PySimpleGUI' and 'pyautogui' to be installed on your computer. You can run 'pip install PySimpleGUI' and 'pip install pyautogui' in cmd to install them.

For the the use Gui you need to operate him from the main of [GUI.py](https://github.com/EN555/HungarianAlgorithm/blob/master/GUI.py)

After that you built the graph 

you can choose how to build the bipartite graph you can add nodes to the left side, to right side and how to connect between them,
after that you can choose to start the algorithm, and see how the algorithm work,


<img src="https://user-images.githubusercontent.com/61500507/119025488-d7256e00-b9ac-11eb-97f6-b63cc60cbe29.png" width="500" height="350"> 


*The algorithm divide for these parts:*
1. Divide all the nodes for four sets represent by four colors- yellow represent A -nodes at the left side that not contain match's edge, blue- represent Am - nodes that contain match's edge, green- represent B-nodes at the right side that not contain match's edge, purple represent Bm - nodes that contain an edge that contain match's edge.

2. Convert the undirected graph to directed graph as describe in the algorithm.

3. Find an augmenting path using bfs algorithm for shortest path.

4. Update The new match in The graph 

All this process visualize in the GUI in our work.
