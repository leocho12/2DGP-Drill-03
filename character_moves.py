from pico2d import *
import math

open_canvas()

grass=load_image('grass.png')
character=load_image('character.png')


def move_rect():
    print("move rectangle")
    pass


def move_circle():
    print("move circle")
    clear_canvas_now()
    character.draw_now(400,300)
    delay(0.1)
    pass


while(True):


    # 원형 이동
    move_circle()
    #사각 이동
    move_rect()


    #break

close_canvas()