from pico2d import *
import math

open_canvas()

grass = load_image('grass.png')
character = load_image('character.png')


def move_top():
    print("move top")
    for x in range(20, 780, 5):  # 좌우 여백 20픽셀 확보
        draw_character(x, 530)    # 상단 여백 확보


def move_right():
    print("move right")
    for y in range(530, 90, -5):  # 상단 시작점 조정
        draw_character(780, y)    # 우측 여백 확보


def move_bottom():
    print("move bottom")
    for x in range(780, 20, -5):  # 좌우 여백 20픽셀 확보
        draw_character(x, 90)     # 하단 여백 유지


def move_left():
    print("move left")
    for y in range(90, 530, 5):   # 상단 끝점 조정
        draw_character(20, y)     # 좌측 여백 확보


def move_rect():
    print("move rectangle")
    move_top()
    move_right()
    move_bottom()
    move_left()


def move_circle():
    print("move circle")
    cx, cy = 400, 300  # 원의 중심
    r = 180  # 반지름을 줄여서 화면 안쪽으로 조정

    for deg in range(0, 360, 2):
        x = cx + r * math.cos(math.radians(deg))
        y = cy + r * math.sin(math.radians(deg))
        draw_character(x, y)


def tri_move_bottom1():
    print("move bottom")
    for x in range(400, 760, 5):  # 우측 끝점 조정
        draw_character(x, 90)


def tri_move_right():
    y = 90
    for x in range(760, 400, -5):  # 우측 시작점 조정
        draw_character(x, y)
        y += 6


def tri_move_left():
    y = 530  # 상단 높이 조정
    for x in range(400, 40, -5):  # 좌측 끝점 조정
        draw_character(x, y)
        y -= 6


def tri_move_bottom2():
    print("move bottom")
    for x in range(40, 400, 5):  # 좌측 시작점 조정
        draw_character(x, 90)


def move_tri():
    tri_move_bottom1()
    tri_move_right()
    tri_move_left()
    tri_move_bottom2()


def draw_character(x: float, y: float):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    delay(0.01)


while True:
    move_rect()    # 사각형 운동
    move_circle()  # 원형 운동
    move_tri()     # 삼각형 운동

close_canvas()
