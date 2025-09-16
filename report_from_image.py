from pico2d import *
import math

open_canvas()

# 이미지 로드
grass = load_image('grass.png')
character = load_image('character.png')

def draw_scene(x, y):
    clear_canvas_now()
    grass.draw_now(400, 30)
    character.draw_now(x, y)
    delay(0.01)

def square_move():
    print("Square Movement Start")
    # 시작 위치: 400, 90

    # 1. 왼쪽에서 오른쪽으로 (x: 0 -> 800, y: 90)
    for x in range(0, 800 + 1, 5):
        draw_scene(x, 90)

    # 2. 아래에서 위로 (x: 800, y: 90 -> 550)
    for y in range(90, 550 + 1, 5):
        draw_scene(800, y)

    # 3. 오른쪽에서 왼쪽으로 (x: 800 -> 0, y: 550)
    for x in range(800, -1, -5):
        draw_scene(x, 550)

    # 4. 위에서 아래로 (x: 0, y: 550 -> 90)
    for y in range(550, 90 - 1, -5):
        draw_scene(0, y)

def circle_move():
    print("Circle Movement Start")
    # 원의 중심: (400, 300), 반지름: 200
    cx, cy = 400, 300  # 원의 중심점
    r = 200  # 반지름

    for deg in range(0, 360, 2):
        x = cx + r * math.cos(math.radians(deg))
        y = cy + r * math.sin(math.radians(deg))
        draw_scene(x, y)

def main():
    while True:
        square_move()  # 사각 운동
        circle_move()  # 원 운동
        break

    close_canvas()

if __name__ == '__main__':
    main()
