
#import
import turtle as trtl

#other
wn = trtl.Screen()

#initialize
player = trtl.Turtle()
xcor = player.xcor()
ycor = player.ycor() # need to account for new coords once moved
rightx = xcor + 10
leftx = xcor - 10
upy = ycor + 10
downy = ycor -10

#functions
def up():
  player.goto(xcor,upy)

def down():
  player.goto(xcor,downy)

def right():
  player.goto(rightx,ycor)

def left():
  player.goto(leftx,ycor)

#call functions
wn.onkeypress(up,"w")
wn.onkeypress(down,"s")
wn.onkeypress(right,"d")
wn.onkeypress(left,"a")

wn.listen()
wn.mainloop()


