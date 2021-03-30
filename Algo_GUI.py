import PySimpleGUI as sg
import pyautogui as ag
from graph import *
import time
from HungrianAlgo import *
import copy
import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


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
        [sg.Button("next", key='-NEXT-')]
    ]

    window = sg.Window("algo_gui", layout=copy.deepcopy(layout), background_color='white')
    window.finalize()

    stage = 1
    is_find = True

    # define some variables for drawing
    left_line = frame_width // 4
    right_line = (3 * frame_width) // 4
    radius = frame_width // 100
    gap = radius // 2

    while True:     # main loop
        events, values = window.read(timeout=200)

        if events is None:  # if the window is closed, exist
            break

        # the first stage - dividing into sets
        if events == '-NEXT-' and stage == 1:

            algo.divide_to_set(algo.graph)

            draw_nodes(window, algo, frame_height, frame_width, left_line, right_line, radius, gap)

            # draw the edges - red if in match, black if not
            for ed in algo.graph.edges:
                if ed.get_is_in():
                    window['-FRAME-'].draw_line(ed.get_src().cords, ed.get_dest().cords, color='red', width=2)
                else:
                    window['-FRAME-'].draw_line(ed.get_src().cords, ed.get_dest().cords, color='black', width=2)

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
                    canvas.create_line((ed.get_src().cords[0] + radius // 2, height // 2 - ed.get_src().cords[1]),
                                       (ed.get_dest().cords[0] - radius // 2, height // 2 - ed.get_dest().cords[1]),
                                       arrow=tk.LAST, fill='red', width=radius // 6)
                else:
                    i = canvas.create_line((ed.get_src().cords[0] + radius // 2, height // 2 - ed.get_src().cords[1]),
                                           (ed.get_dest().cords[0] - radius // 2, height // 2 - ed.get_dest().cords[1]),
                                           arrow=tk.LAST, fill='black', width=radius // 6)
            stage = 3

        elif events == '-NEXT-' and stage == 3:
            pass



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

