from pico2d import *
import math

open_canvas()

grass=load_image('grass.png')
character=load_image('character.png')

x=400
y=90

#사각이동
while(x<780):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,90)
    x+=2
    delay(0.01)

while(y<550):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    y+=2
    delay(0.01)

while(x>20):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    x-=2
    delay(0.01)

while(y>90):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    y-=2
    delay(0.01)

while(x<400):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(x,y)
    x+=2
    delay(0.01)

#원형이동
sin=math.sin(270/360*2*math.pi)
cos=math.cos(270/360*2*math.pi)

for i in range(360):
    clear_canvas_now()
    grass.draw_now(400,30)
    character.draw_now(400+230*cos,320+230*sin)
    sin=math.sin((270+i)/360*2*math.pi)
    cos=math.cos((270+i)/360*2*math.pi)
    delay(0.01)

close_canvas()