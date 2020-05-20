#!/bin/env python
"""WARNING: VERY bad code that I've written for my IT class presentation"""

import pygame
import sys
import functools
import tkinter
import tkinter.ttk
import threading

godmode = False
size = width, height = 1280, 720
bg_color = 50, 50, 50
brown = 150, 75, 0
blue = 0, 0, 255
last_blue = 50, 50, 127
disk_height = height/15
first_disk_width = width/5
last_disk_width = width/17

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.set_caption('Wieza Hanoi')
clock = pygame.time.Clock()


class Rod:
    def __init__(self, *args, disks=None):
        self.rect = pygame.Rect(*args)
        if disks == None:
            self.disks = []
        else:
            self.disks = disks

    def print_disks(self):
        for i, disk in enumerate(self.disks):
            pygame.draw.rect(screen, disk.color,
                    (disk.rect.x, disk.rect.y,
                        disk.rect.width, disk.rect.height))
            font = pygame.font.Font(None, 40)
            ren = font.render(
                    str(disk.number), 0, (255, 255, 255), screen)
            screen.blit(ren,
                    (disk.rect.x+disk.rect.width//2-5,
                        disk.rect.y+disk.rect.height//4))


    def set_disks(self):
        for i, disk in enumerate(self.disks):
            disk.rect.x = self.rect.x - disk.rect.width//2 + self.rect.width//2
            disk.rect.y = int(self.rect.bottom - (i+1) * disk_height)


class Disk:
    def __init__(self, number, color, *args):
        self.rect = pygame.Rect(*args)
        self.number = number
        self.color = color


def create_disks(n):
    disks = []
    width = first_disk_width
    color = blue
    for i in range(n-1, -1, -1):
        disks.append(Disk(i, color, (0, 0, int(width), int(disk_height))))
        width -= (first_disk_width-last_disk_width) / (n-1)
        color = \
            color[0] - (blue[0]-last_blue[0]) // (n-1), \
            color[1] - (blue[1]-last_blue[1]) // (n-1), \
            color[2] - (blue[2]-last_blue[2]) // (n-1)
    return disks


def set_print_tomove_disks(pos, disks):
    disks.reverse()
    for i, disk in enumerate(disks):
        disk.rect.x = int(pos[0] - disk.rect.width/2)
        disk.rect.y = int(pos[1] - i * disk_height)
        pygame.draw.rect(screen, disk.color,
                (disk.rect.x, disk.rect.y, disk.rect.width, disk.rect.height))
        font = pygame.font.Font(None, 40)
        ren = font.render(
                str(disk.number), 0, (255, 255, 255), screen)
        screen.blit(ren,
                (disk.rect.x+disk.rect.width//2-5,
                    disk.rect.y+disk.rect.height//4))
    disks.reverse()


in_rect = lambda pos, rect: \
        pos[0] >= rect.x and pos[0] <= rect.x+rect.width and \
        pos[1] >= rect.y and pos[1] <= rect.y+rect.height


rods = [Rod(
            int(width * ((i+1)/4)),
            int(height * 3/5 - (height/10)),
            int(width / 100),
            int(height * 2/5)
        ) for i in range(3)]
ilosc_dyskow = 4
min_ruchy = 0
binary_clock = 0
print_clock = False
ruchy = 0
to_move = []
win = False


def init_game(n):
    global win
    global rods
    global ilosc_dyskow
    global min_ruchy
    global ruchy
    global last_rod
    global binary_clock

    ilosc_dyskow = n
    min_ruchy = 2**ilosc_dyskow - 1
    ruchy = 0
    last_rod = None
    win = False
    binary_clock = 0
    for rod in rods:
        rod.disks = []
    rods[0].disks = create_disks(ilosc_dyskow)


def menu():
    root = tkinter.Tk()
    root.title("menu wiezy Hanoi")
    root.geometry('350x200')
    chk_godmode = tkinter.BooleanVar()
    chk_godmode.set(False)
    chk_clock = tkinter.BooleanVar()
    chk_clock.set(False)

    def change_godmode():
        global godmode
        godmode = chk_godmode.get()

    def change_clock():
        global print_clock
        print_clock = chk_clock.get()

    def reset_clock():
        global binary_clock
        binary_clock = 0

    chk = tkinter.Checkbutton(root, text='GODMODE', var=chk_godmode,
            command=change_godmode)
    chk.grid(column=0, row=0)
    chk2 = tkinter.Checkbutton(root, text='binary clock', var=chk_clock,
            command=change_clock)
    chk2.grid(column=1, row=0)

    lbl = tkinter.Label(root, text="dyski: ")
    lbl.grid(column=0, row=1)
    txt = tkinter.Entry(root, width=10)
    txt.grid(column=1, row=1)

    def clicked():
        init_game(int(txt.get()))

    btn = tkinter.Button(root, text="RESET", command=clicked)
    btn.grid(column=2, row=1)
    btn2 = tkinter.Button(root, text="reset clock", command=reset_clock)
    btn2.grid(column=2, row=0)

    root.mainloop()
    
menu_thread = threading.Thread(target=menu, args=(), daemon=True)
menu_thread.start()

init_game(ilosc_dyskow)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif win:
            if event.type == pygame.MOUSEBUTTONDOWN:
                init_game(ilosc_dyskow)
            continue
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for rod in rods:
                if len(rod.disks) > 0:
                    last_rod = rod
                    pos_in_rect = functools.partial(in_rect, event.pos)
                    if pos_in_rect(rod.disks[-1].rect):
                        to_move.append(rod.disks.pop())
                        break
                    elif godmode and any(map(pos_in_rect,
                            [x.rect for x in rod.disks])):
                        while not pos_in_rect(rod.disks[-1].rect):
                            to_move.append(rod.disks.pop())
                        to_move.append(rod.disks.pop())
                        break
        elif event.type == pygame.MOUSEBUTTONUP:
            if to_move:
                if event.pos[0] <= width/3:
                    rod = rods[0]
                elif event.pos[0] <= width/3 * 2:
                    rod = rods[1]
                else:
                    rod = rods[2]
                if rod == last_rod:
                    pass
                elif godmode or len(rod.disks) == 0 or \
                        rod.disks[-1].number > to_move[-1].number:
                    ruchy += 1
                else:
                    rod = last_rod
                while to_move:
                    rod.disks.append(to_move.pop())
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c:
                binary_clock += 1

    screen.fill(bg_color)

    for rod in rods:
        pygame.draw.rect(screen, brown, (rod.rect.x, rod.rect.y,
            rod.rect.width, rod.rect.height))
        rod.set_disks()
        rod.print_disks()
    set_print_tomove_disks(pygame.mouse.get_pos(), to_move)
    for rod in rods[1:]:
        if len(rod.disks) >= ilosc_dyskow:
            win = True;

    font = pygame.font.Font(None, 40)
    text = 'najmniejsza mozliwa ilosc ruchow: ' + str(min_ruchy)
    size = font.size(text)

    ren = font.render(text, 0, (255, 255, 255), screen)
    screen.blit(ren, (10, 10))

    text = 'aktualna ilosc ruchow: ' + str(ruchy)
    ren = font.render(text, 0, (255, 255, 255), screen)
    screen.blit(ren, (10, 50))

    if print_clock:
        font = pygame.font.Font(None, 100)
        number_format = f"{{:#0{2+ilosc_dyskow}b}}"
        ren = font.render(number_format.format(binary_clock),
                0, (255, 255, 255), screen)
        screen.blit(ren, (10, 100))

    if win:
        font = pygame.font.Font(None, 200)
        text = 'WYGRALES'
        ren = font.render(text, 0, (0, 255, 0), screen)
        screen.blit(ren, (50, height//2))
    pygame.display.flip()
    clock.tick(60)
