import PySimpleGUI as sg
import pyautogui as ag
from HungrianAlgo import *
import copy
import tkinter as tk


def algo_gui(graph: Graph) -> None:
    algo = HungarianAlgo(graph)
    width, height = ag.size()  # get screen dimensions

    frame_height = height // 2  # how many pixels to divide the frame to
    frame_width = width // 2

    layout = [  # the layout of the frame
        [sg.Graph(
            key='-FRAME-', canvas_size=(width // 2, height // 2),
            graph_bottom_left=(0, 0), graph_top_right=(frame_width, frame_height),
            background_color='white'
        )],
        [sg.Button("Exit", key='-EXIT-', button_color='red'), sg.Button("Next", key='-NEXT-'),
         sg.Text("Press next to continue", key='-MSG-', text_color='purple', background_color='white', size=(100, 1))]
    ]

    window = sg.Window("Algo_Gui", layout=copy.deepcopy(layout), background_color='white')
    window.finalize()

    stage = 1
    is_find = True
    path = []

    # define some variables for drawing
    left_line = frame_width // 4
    right_line = (3 * frame_width) // 4
    radius = frame_width // 100
    gap = radius // 2

    while True:  # main loop
        events, values = window.read(timeout=200)

        if events is None or events == '-EXIT-':  # if the window is closed, exist
            break

        # the first stage - dividing into sets
        if events == '-NEXT-' and stage == 1:

            algo.divide_to_set(algo.graph)

            draw_nodes(window, algo, frame_height, frame_width, left_line, right_line, radius, gap)

            # draw the edges - red if in match, black if not
            draw_edges(window, algo)

            window['-MSG-'].update("Divided the node into the four groups as described in the algorithm")

            stage = 2

        # second step - convert to directed graph
        elif events == '-NEXT-' and stage == 2:
            algo.convert_to_direct_graph()
            algo.clear_All_lists()
            algo.divide_to_set(algo.temp_graph)

            draw_nodes(window, algo, frame_height, frame_width, left_line, right_line, radius, gap)

            # draw the edges - red if in match, black if not
            canvas = window['-FRAME-'].TKCanvas
            for ed in algo.temp_graph.edges:
                if ed.get_is_in():
                    canvas.create_line((ed.get_src().cords[0] - radius//2, height//2 - ed.get_src().cords[1]),
                                       (ed.get_dest().cords[0] + radius//2, height//2 - ed.get_dest().cords[1]),
                                       arrow=tk.LAST, fill='red', width=radius // 6)
                else:
                    canvas.create_line((ed.get_src().cords[0] + radius // 2, height // 2 - ed.get_src().cords[1]),
                                       (ed.get_dest().cords[0] - radius // 2, height // 2 - ed.get_dest().cords[1]),
                                       arrow=tk.LAST, fill='black', width=radius // 6)
            window['-MSG-'].update("Turned the graph to a connected graph")
            stage = 3

        elif events == '-NEXT-' and stage == 3:
            is_find, path = algo.find_m_augmenting_path()
            if is_find:

                draw_nodes(window, algo, frame_height, frame_width, left_line, right_line, radius, gap)

                edges_on_path = []
                for i in range(len(path) - 1):
                    edges_on_path.append(algo.temp_graph.get_edge(path[i], path[i + 1]))

                canvas = window['-FRAME-'].TKCanvas
                for ed in algo.temp_graph.edges:
                    if ed in edges_on_path:
                        canvas.create_line((ed.get_src().cords[0] + radius // 2, height // 2 - ed.get_src().cords[1]),
                                           (ed.get_dest().cords[0] - radius // 2, height // 2 - ed.get_dest().cords[1]),
                                           arrow=tk.LAST, fill='blue', width=radius // 4)
                    elif ed.get_is_in():
                        canvas.create_line((ed.get_src().cords[0] - radius // 2, height // 2 - ed.get_src().cords[1]),
                                           (ed.get_dest().cords[0] + radius // 2, height // 2 - ed.get_dest().cords[1]),
                                           arrow=tk.LAST, fill='red', width=radius // 6)
                    else:
                        canvas.create_line((ed.get_src().cords[0] + radius // 2, height // 2 - ed.get_src().cords[1]),
                                           (ed.get_dest().cords[0] - radius // 2, height // 2 - ed.get_dest().cords[1]),
                                           arrow=tk.LAST, fill='black', width=radius // 6)
                window['-MSG-'].update("Found an M augmenting path")
                stage = 4
            else:
                stage = -1  # should be msg "not path found, algo done!" + stage = -1
                draw_nodes(window, algo, frame_height, frame_width, left_line, right_line, radius, gap)
                draw_edges(window, algo)
                window['-MSG-'].update("The algorithm is done!")

        elif events == '-NEXT-' and stage == 4:
            algo.augment_the_path(path)

            draw_nodes(window, algo, frame_height, frame_width, left_line, right_line, radius, gap)

            draw_edges(window, algo)

            algo.clear_All_lists()

            window['-MSG-'].update("Augmented the path")
            stage = 1

    window.close()


def draw_nodes(window: sg.Window, algo: HungarianAlgo, frame_height: int, frame_width: int, left_line: int,
               right_line: int, radius: int, gap: int):
    window['-FRAME-'].TKCanvas.delete("all")
    nodes_left = 0
    nodes_right = 0

    for node in algo.get_listA():
        hei = frame_height - gap - nodes_left * (radius + gap)
        nodes_left += 1
        node.cords = (left_line + radius // 2, hei - radius // 2)
        window['-FRAME-'].draw_oval(top_left=(left_line, hei), bottom_right=(left_line + radius, hei - radius),
                                    fill_color='#FFCD00')

    for node in algo.get_listAm():
        hei = frame_height - gap - nodes_left * (radius + gap)
        nodes_left += 1
        node.cords = (left_line + radius // 2, hei - radius // 2)
        window['-FRAME-'].draw_oval(top_left=(left_line, hei), bottom_right=(left_line + radius, hei - radius),
                                    fill_color='#005EFF')

    for node in algo.get_listB():
        hei = frame_height - gap - nodes_right * (radius + gap)
        nodes_right += 1
        node.cords = (right_line + radius // 2, hei - radius // 2)
        window['-FRAME-'].draw_oval(top_left=(right_line, hei),
                                    bottom_right=(right_line + radius, hei - radius),
                                    fill_color='green')

    for node in algo.get_listBm():
        hei = frame_height - gap - nodes_right * (radius + gap)
        nodes_right += 1
        node.cords = (right_line + radius // 2, hei - radius // 2)
        window['-FRAME-'].draw_oval(top_left=(right_line, hei),
                                    bottom_right=(right_line + radius, hei - radius),
                                    fill_color='#B41BFF')


def draw_edges(window: sg.Window, algo: HungarianAlgo):
    for ed in algo.graph.edges:
        if ed.get_is_in():
            window['-FRAME-'].draw_line(ed.get_src().cords, ed.get_dest().cords, color='red', width=2)
        else:
            window['-FRAME-'].draw_line(ed.get_src().cords, ed.get_dest().cords, color='black', width=2)
