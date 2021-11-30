
#import
import turtle

#other
class block:
    def __init__(self, name, type, xwidth, ywidth):
        self.name = name
        self.type = type
        self.width = xwidth,ywidth
        self.xwidth = xwidth
        self.ywidth = ywidth
grass = block('grass','solid',16,16)
dirt = block('dirt','solid',16,16)
stone = block('stone','solid',16,16)
log = block('log','solid',16,16)
wn = turtle.Screen()

#initialize
player = turtle.Turtle()
dirt = turtle.turtles
xcor = player.xcor()
ycor = player.ycor() # need to account for new coords once moved
rightx = xcor + 10
leftx = xcor - 10
upy = ycor + 10
downy = ycor - 10

#functions
def up():
    xcor = player.xcor()
    ycor = player.ycor()
    ycor += 10
    player.goto(xcor,ycor)

def down():
    xcor = player.xcor()
    ycor = player.ycor()
    ycor -= 10
    player.goto(xcor,ycor)

def right():
    xcor = player.xcor()
    ycor = player.ycor()
    xcor += 10
    player.goto(xcor,ycor)

def left():
    xcor = player.xcor()
    ycor = player.ycor()
    xcor -= 10
    player.goto(xcor,ycor)

#call functions
wn.onkeypress(up,"w")
wn.onkeypress(down,"s")
wn.onkeypress(right,"d")
wn.onkeypress(left,"a")
wn.onkeypress(up,"Up")
wn.onkeypress(down,"Down")
wn.onkeypress(right,"Right")
wn.onkeypress(left,"Left")

wn.listen()
wn.mainloop()


