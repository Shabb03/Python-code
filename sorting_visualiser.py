#!/usr/bin/env python3

#REFERENCE: https://www.youtube.com/watch?v=twRidO-_vqQ

import pygame
import random
import math
pygame.init()

class Screen:
    BLACK = 0, 0, 0
    WHITE = 255, 255, 255
    GREEN = 0, 255, 0
    RED = 255, 0, 0
    GREY = 128, 128, 128
    BG = WHITE

    GRADIENTS = [
        (128, 128, 128),
        (160, 160, 160),
        (192, 192, 192)
    ]

    SIDE = 100
    TOP = 150

    FONT = pygame.font.SysFont('comicsans', 30)
    LARGE_FONT = pygame.font.SysFont('comicsans', 40)

    def __init__(self, width, height, lst):
        self.width = width
        self.height = height
        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualiser")
        self.set_list(lst)

    def set_list(self, lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)

        self.side_width = round((self.width - self.SIDE) / len(lst))
        self.side_height = math.floor((self.height - self.TOP) / (self.max_val - self.min_val))
        self.start_x = self.SIDE // 2

def draw(drawing, name):
    drawing.window.fill(drawing.BG)

    title = drawing.LARGE_FONT.render(name, 1, drawing.GREEN)
    drawing.window.blit(title, (drawing.width/2 - title.get_width()/2, 5))

    controls = drawing.FONT.render("R - Reset | SPACE - Start", 1, drawing.BLACK)
    drawing.window.blit(controls, (drawing.width/2 - controls.get_width()/2, 45))

    sort_controls = drawing.FONT.render("B - Bubble Sort | I - Insertion Sort | S - Selection Sort", 1, drawing.BLACK)
    drawing.window.blit(sort_controls, (drawing.width/2 - sort_controls.get_width()/2, 75))

    draw_list(drawing)
    pygame.display.update()

def draw_list(drawing, pos_colour={}, clear_bg=False):
    lst = drawing.lst

    if clear_bg:
        clear_rect = (drawing.SIDE//2, drawing.TOP, drawing.width - drawing.SIDE, drawing.height - drawing.TOP)

        pygame.draw.rect(drawing.window, drawing.BG, clear_rect)

    for i, val in enumerate(lst):
        x = drawing.start_x + i * drawing.side_width
        y = drawing.height - (val - drawing.min_val) * drawing.side_height

        colour = drawing.GRADIENTS[i % 3]

        if i in pos_colour:
            colour = pos_colour[i]

        pygame.draw.rect(drawing.window, colour, (x, y, drawing.side_width, drawing.height))

    if clear_bg:
        pygame.display.update()

def gen_list(n, min_val, max_val):
    lst = []
    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)
    return lst

def bubble_sort(drawing):
    lst = drawing.lst

    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            num1 = lst[j]
            num2 = lst[j + 1]

            if num1 > num2:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                draw_list(drawing, {j: drawing.GREEN, j+1: drawing.RED}, True)
                yield True

def insertion_sort(drawing):
    lst = drawing.lst

    for i in range(1, len(lst)):
        current = lst[i]

        while True:
            sorting = i > 0 and lst[i - 1] > current

            if not sorting:
                break

            lst[i] = lst[i-1]
            i = i - 1
            lst[i] = current
            draw_list(drawing, {i-1: drawing.GREEN, i: drawing.RED}, True)
            yield True

    return lst

def selection_sort(drawing):
    lst = drawing.lst

    for i in range(len(lst)):
      
        min_val = i
        for j in range(i+1, len(lst)):
            if lst[min_val] > lst[j]:
                min_val = j
                draw_list(drawing, {min_val: drawing.GREEN, i: drawing.RED}, True)
                yield True
                     
        lst[i], lst[min_val] = lst[min_val], lst[i]

    return lst

def main():
    run = True
    clock = pygame.time.Clock()

    n = 50
    min_val = 0
    max_val = 100

    lst = gen_list(n, min_val, max_val)
    drawing = Screen(800, 600, lst)
    sorting = False

    sorting_algorithm = bubble_sort
    sorting_name = "Bubble Sort"
    sorting_gen = None

    while run:
        clock.tick(60)

        if sorting:
            try:
                next(sorting_gen)
            except StopIteration:
                sorting = False
        else:
            draw(drawing, sorting_name)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_r:
                lst = gen_list(n, min_val, max_val)
                drawing.set_list(lst)
                sorting = False
            elif event.key == pygame.K_SPACE and sorting == False:
                sorting = True
                sorting_gen = sorting_algorithm(drawing)
            elif event.key == pygame.K_i and sorting == False:
                sorting_algorithm = insertion_sort
                sorting_name = "Insertion Sort"
            elif event.key == pygame.K_b and sorting == False:
                sorting_algorithm = bubble_sort
                sorting_name = "Bubble Sort"
            elif event.key == pygame.K_s and sorting == False:
                sorting_algorithm = selection_sort
                sorting_name = "Selection Sort"

    pygame.quit()

if __name__ == "__main__":
    main()
