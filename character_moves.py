from pico2d import *
import math

open_canvas()

grass=load_image('grass.png')
character=load_image('character.png')


def move_top():
    pass


def move_right():
    pass


def move_bottom():
    pass


def move_left():
    pass


def move_rect():
    print("move rectangle")
    
    move_top()
    move_right()
    move_bottom()
    move_left()
    pass


def move_circle():
    print("move circle")

    for deg in range(0, 360):
        r=200
        x=r*math.cos(math.radians(deg))+400
        y=r*math.sin(math.radians(deg))+300
        clear_canvas_now()
        character.draw_now(x,y)
        delay(0.01)
    pass


while(True):


    # 원형 이동
    move_circle()
    #사각 이동
    move_rect()


    break

close_canvas()