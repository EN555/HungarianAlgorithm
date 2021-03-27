import PySimpleGUI as sg
import pyautogui as ag
from graph import *
import time

width, height = ag.size()

graph = Graph()

frame_height = 10000
frame_width = 10000

layout = [
    [sg.Graph(
        key='-FRAME-', canvas_size=(width // 2, height // 2),
        graph_bottom_left=(0, 0), graph_top_right=(frame_width, frame_height),
        background_color='white'
    )],

    [sg.Button("add node to left", key='-ADD_LEFT-'), sg.Button("add node to right", key='-ADD_RIGHT-'),
     sg.Button("connect", key='-CONNECT-'),
     sg.Input(default_text='nodeID', size=(10, 1), key='-NODE1-'),
     sg.Input(default_text='nodeID', size=(10, 1), key='-NODE2-')],

    [sg.Button('Exist', key='-EXIST-', button_color='red'),
     sg.Text("", key='-ERROR_MSG-', size=(30, 1), text_color='red', background_color='white')]
]

window = sg.Window("GUI", layout=layout, background_color='white')

left_line = frame_width // 4
right_line = (3 * frame_width) // 4

radius = frame_width // 50
gap = radius // 2
max_nodes_on_side = frame_height // (radius + gap)
nodes_on_right = 0
nodes_on_left = 0

while True:
    event, value = window.read()

    if event is None or event == '-EXIST-':
        break
    if event == '-ADD_LEFT-':
        if nodes_on_left < max_nodes_on_side:

            window['-ERROR_MSG-'].update("")

            h = frame_height - gap - (radius + gap) * nodes_on_left
            node = Node((left_line + radius // 2, h - radius // 2), side='left')
            graph.add_node(node)

            window['-FRAME-'].draw_oval(top_left=(left_line, h), bottom_right=(left_line + radius, h - radius),
                                        fill_color='lightgreen')
            nodes_on_left += 1
            window['-FRAME-'].draw_text(str(node.id), location=(left_line - radius, h - radius // 2))
        else:
            window['-ERROR_MSG-'].update("out of space")

    if event == '-ADD_RIGHT-':
        if nodes_on_right < max_nodes_on_side:

            window['-ERROR_MSG-'].update("")

            h = frame_height - gap - (radius + gap) * nodes_on_right
            node = Node((right_line + radius // 2, h - radius // 2), side='right')
            graph.add_node(node)

            window['-FRAME-'].draw_oval(top_left=(right_line, h), bottom_right=(right_line + radius, h - radius),
                                        fill_color='lightblue')
            nodes_on_right += 1
            window['-FRAME-'].draw_text(str(node.id), location=(right_line + 2 * radius, h - radius // 2))
        else:
            window['-ERROR_MSG-'].update("out of space")

    if event == '-CONNECT-':
        n1 = value['-NODE1-']
        n2 = value['-NODE2-']
        if n1.isdigit() and n2.isdigit() and int(n1) in graph.nodes.keys() and int(n2) in graph.nodes.keys():
            if graph.nodes[int(n1)].side == graph.nodes[int(n2)].side:
                window['-ERROR_MSG-'].update("nodes must be on different sides")
            else:
                window['-ERROR_MSG-'].update("")
                graph.connect(int(n1), int(n2))
                window['-FRAME-'].draw_line(graph.nodes[int(n1)].cords, graph.nodes[int(n2)].cords, color='black', width=2)

        else:
            window['-ERROR_MSG-'].update("please enter nodes id's")

    time.sleep(0.05)
window.close()
