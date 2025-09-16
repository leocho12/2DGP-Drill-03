from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')


def move_top():
    print("move top")
    for x in range(0, 800, 5):
        draw_character(x, 550)


def move_right():
    print("move right")
    for y in range(550, 90, -5):
        draw_character(800, y)


def move_bottom():
    print("move bottom")
    for x in range(800, 0, -5):
        draw_character(x, 90)

def move_left():
    print("move left")
    for y in range(90, 600, 5):
        draw_character(0, y)



def move_rect():
    print("move rectangle")
    move_top()
    move_right()
    move_bottom()
    move_left()


def move_circle():
    print("move circle")
    for deg in range(0, 360, 2):  # 2도씩 증가하여 더 부드러운 원운동
        r = 200
        x = r * math.cos(math.radians(deg)) + 400
        y = r * math.sin(math.radians(deg)) + 300
        draw_character(x, y)


def draw_character(x: float, y: float):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    delay(0.01)


while True:
    # 사각 이동 후 원형 이동
    move_rect()
    move_circle()

    break

close_canvas()
