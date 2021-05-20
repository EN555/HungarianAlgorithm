### Hungarian Algorithm 

This is an implementation of the Hungarian method for finding a perfect matching in a **bipartite** graphs, and a visual representation of the algorithm work, step-by-step.

For the the use Gui you need to operate him from the main of [GUI.py](https://github.com/EN555/HungarianAlgorithm/blob/master/GUI.py)

After that you have some option,

<img src="https://user-images.githubusercontent.com/61500507/115743270-31291880-a39a-11eb-8e16-92c19accae9f.png" width="600" height="150">

you can choose how to build the bipartite graph' you can add nodes to the left side, to right side and how to connect between them,
after that you can choose to start the algorithm, and see how the algorithm work,
First,

<img src="https://user-images.githubusercontent.com/61500507/115744738-831e6e00-a39b-11eb-8d2a-e727067e51ce.png" width="500" height="350">
at this time the algorithm divide to four sets represent by four colors- yellow represent A, blue- represent Am, green- represent B, purple represent Bm, at this time Am and Bm are empty so they not appper.

the pr7ject has three parts:
graph.py, graph_utils.py - a simple implementation of an not-weighted graph. the graph can be use as both directed and un-directed, by using the matching methods: 'connect' or 'connect_direct'. 
it is up to the user to make sure he is using the right methods.

HungarianAlgo.py - an implementation of the Hungarian method, using the graph from graph.py, graph_utils.py.
in order to use this, the user need to construct a  bipartite graph using graph.py, graph_utils.py, and then create an instance of HungarianAlgo class, 
giving the graph as parameter in the constructor. to run the algorithm, the method 'find_max_match' need to be called.

GUI.py, Algo_GUI.py - this provides a friendly GUI for constructing a bipartite graph, and visualizing the algorithm work on it. 
the GUI can be run by simply executing the GUI.py file ("python GUI.py" in cmd).
 note: you need the libraries 'PySimpleGUI' and 'pyautogui' to be installed on your computer. you can run 'pip install PySimpleGUI' and 'pip install pyautogui' in cmd to install them.