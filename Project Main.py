#* import
import turtle
screen = turtle.Screen()
width=768
height=512
screen.setup(width, height) #! setup the screen height and width to multiples of 64 then figure out how many blocks can fit widthwards and heightwards
screen.setworldcoordinates(0,height,width,0)
blockHeight = height/64
blockWidth = width/64
print(blockHeight)#! print those values of how many blocks can fit widthwards and heightwards
print(blockWidth)

#* other
class block:
    def __init__(self, name, type, image, xwidth, ywidth):
        self.name = name
        self.type = type
        self.image = image
        self.width = xwidth,ywidth
        self.xwidth = xwidth
        self.ywidth = ywidth
grass = block('grass','solid','grass.gif',64,64)
dirt = block('dirt','solid','dirt.gif',64,64)
stone = block('stone','solid','stone.gif',64,64)
log = block('log','solid','wood.gif',64,64)
turtle.register_shape(grass.image)
turtle.register_shape(dirt.image)
turtle.register_shape(stone.image)
turtle.register_shape(log.image)
#* initialize
moveAmount = 16 #! currently for development only
player = turtle.Turtle()
draw = turtle.Turtle()
draw.speed(0)
draw.up()
#* create devlopment grid
i = -1
while i<blockWidth:
    i += 1
    draw.goto(i*64,0)
    draw.down()
    draw.goto(i*64,blockHeight*64)
    draw.up()
i = -1
while i<blockHeight:
    i += 1
    draw.goto(0,i*64)
    draw.down()
    draw.goto(blockWidth*64,i*64)
    draw.up()


#* functions
def up():
    xcor = player.xcor()
    ycor = player.ycor()
    ycor += moveAmount 
    player.goto(xcor,ycor)

def down():
    xcor = player.xcor()
    ycor = player.ycor()
    ycor -= moveAmount 
    player.goto(xcor,ycor)

def right():
    xcor = player.xcor()
    ycor = player.ycor()
    xcor += moveAmount 
    player.goto(xcor,ycor)

def left():
    xcor = player.xcor()
    ycor = player.ycor()
    xcor -= moveAmount 
    player.goto(xcor,ycor)

#* call functions
screen.onkeypress(up,"w")
screen.onkeypress(down,"s")
screen.onkeypress(right,"d")
screen.onkeypress(left,"a")
screen.onkeypress(up,"Up")
screen.onkeypress(down,"Down")
screen.onkeypress(right,"Right")
screen.onkeypress(left,"Left")

screen.listen()
screen.mainloop()


