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
blocks = []
#* other
class block:
    def __init__(self, name, type, image, xwidth, ywidth):
        self.name = name
        self.type = type
        self.image = image
        self.width = xwidth,ywidth
        self.xwidth = xwidth
        self.ywidth = ywidth
        self.locations = []
global grass, dirt, stone, log
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
draw.hideturtle()
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
    ycor -= moveAmount 
    player.goto(xcor,ycor)
def down():
    xcor = player.xcor()
    ycor = player.ycor()
    ycor += moveAmount 
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
global currentBlock
currentBlock = None
def slotOne():
    print("slot 1")
    global currentBlock
    currentBlock = grass.image
def slotTwo():
    print("slot 2")
    global currentBlock
    currentBlock = dirt.image
def slotThree():
    print("slot 3")
    global currentBlock
    currentBlock = stone.image
def slotFour():
    print("slot 4")
    global currentBlock
    currentBlock = log.image
def gotoBreakBlock(x,y):
    breakBlock(x,y,blocks)
def gotoPlaceBlock(x,y):
    placeBlock(x,y,currentBlock)
def breakBlock(x,y,blocks):
    print('break')
    xSubtr = x%64
    x -= xSubtr
    x /= 64
    x += 1
    print(x)
    print(xSubtr)
    ySubtr = y%64
    y -= ySubtr
    y /= 64
    y += 1
    print(y)
    print(ySubtr)
def placeBlock(x,y,currentBlock):
    print('place')
    xSubtr = x%64
    x -= xSubtr
    x /= 64
    x += 1
    print(x)
    print(xSubtr)
    ySubtr = y%64
    y -= ySubtr
    y /= 64
    y += 1
    print(y)
    print(ySubtr)
    currentTurtle = turtle.Turtle()
    currentTurtle.speed(0)
    currentTurtle.hideturtle()
    currentTurtle.up()
    currentTurtle.goto((x*64)-32,(y*64)-32)
    currentTurtle.shape(currentBlock)
    print(currentBlock)
    currentTurtle.showturtle()
    blocks.append(currentTurtle)
#* call functions
screen.onscreenclick(gotoBreakBlock,3)
screen.onscreenclick(gotoPlaceBlock,1)
screen.onkeypress(up,"w")
screen.onkeypress(down,"s")
screen.onkeypress(right,"d")
screen.onkeypress(left,"a")
screen.onkeypress(up,"Up")
screen.onkeypress(down,"Down")
screen.onkeypress(right,"Right")
screen.onkeypress(left,"Left")
screen.onkeypress(slotOne,'1')
screen.onkeypress(slotTwo,'2')
screen.onkeypress(slotThree,'3')
screen.onkeypress(slotFour,'4')

screen.listen()
screen.mainloop()


