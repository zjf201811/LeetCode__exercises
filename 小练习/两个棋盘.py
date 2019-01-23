#Author:ZJF
import turtle

def draw_diamond(l):
    for i in range(4):
        turtle.forward(l)
        turtle.right(90)
def drawChessboard(startx,endx,starty,endy):
    turtle.color("black")
    w_x = float((endx - startx)/8)
    for m in range(8):
        for n in range(8):
            turtle.penup()
            turtle.goto(startx+n*w_x,starty-m*w_x)
            turtle.pendown()
            if (m + n)%2==1:
                turtle.begin_fill()
                draw_diamond(w_x)
                turtle.end_fill()
            else:
                draw_diamond(w_x)
drawChessboard(0,400,400,0)
turtle.done()