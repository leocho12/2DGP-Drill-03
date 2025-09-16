from pico2d import *
import math

open_canvas()

grass=load_image('grass.png')
character=load_image('character.png')



def move_top():
    print("move top")
    for x in range(800, 20, -5):
        draw_character(x, 550)


def move_right():
    print("move right")
    for y in range(90, 550, 5):
        draw_character(780, y)


def move_bottom1():
    print("move bottom")
    for x in range(400, 780, 5):
        draw_character(x, 90)

def move_bottom2():
    print("move bottom")
    for x in range(20, 400, 5):
        draw_character(x, 90)

def move_left():
    print("move left")
    for y in range(550, 90, -5):
        draw_character(20, y)


def move_rect():
    print("move rectangle")

    move_bottom1()
    move_right()
    move_top()
    move_left()
    move_bottom2()
    pass


def move_circle():
    print("move circle")

    for deg in range(0, 360):
        r=200
        x=r*math.cos(math.radians(deg))+400
        y=r*math.sin(math.radians(deg))+300
        draw_character(x, y)
    pass


def draw_character(x: float, y: float):
    clear_canvas_now()
    character.draw_now(x, y)
    grass.draw_now(400, 30)
    delay(0.01)


while(True):


    # 원형 이동
    move_circle()
    #사각 이동
    move_rect()


    break

close_canvas()