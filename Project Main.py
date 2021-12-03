
#* import
import turtle
screen = turtle.Screen()
screen.bgcolor("#AAFFEE")
width=768
height=512
screen.setup(width, height) #! setup the screen height and width to multiples of 64 then figure out how many blocks can fit widthwards and heightwards
screen.setworldcoordinates(0,height,width,0)
blockHeight = height/64
blockWidth = width/64
print(blockHeight)#! print those values of how many blocks can fit widthwards and heightwards
print(blockWidth)
global blocks,xblocks,yblocks
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
plank = block('plank','solid','planks.gif',64,64)
turtle.register_shape(grass.image)
turtle.register_shape(dirt.image)
turtle.register_shape(stone.image)
turtle.register_shape(log.image)
turtle.register_shape(plank.image)
turtle.register_shape('none.gif')
turtle.register_shape('Grass..gif')
turtle.register_shape('Dirt..gif')
turtle.register_shape('Stone..gif')
turtle.register_shape('Plank.gif')
turtle.register_shape('Log.gif')
#* initialize
moveAmount = 4 #! currently for development only
player = turtle.Turtle()
displayBlock = turtle.Turtle()
draw = turtle.Turtle()
draw.speed(0)
draw.up()
draw.hideturtle()
displayBlock.hideturtle()
displayBlock.up()
displayBlock.goto(32,-8)
displayBlock.shape('none.gif')
displayBlock.showturtle()
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
    currentBlock = grass
    displayBlock.shape('Grass..gif')
def slotTwo():
    print("slot 2")
    global currentBlock
    currentBlock = dirt
    displayBlock.shape('Dirt..gif')
def slotThree():
    print("slot 3")
    global currentBlock
    currentBlock = stone
    displayBlock.shape('Stone..gif')
def slotFour():
    print("slot 4")
    global currentBlock
    currentBlock = log
    displayBlock.shape('Log.gif')
def slotFive():
    print('slot 5')
    global currentBlock
    currentBlock = plank
    displayBlock.shape('Plank.gif')
def gotoBreakBlock(x,y):
    breakBlock(x,y,blocks)
def gotoPlaceBlock(x,y):
    placeBlock(x,y,currentBlock)
def searchBlocks(blocks,x,y):
    ifBlock = None
    searchQueryData = None
    global i
    i = 0
    while i<len(blocks):
        search = blocks[i]
        if search[1] == x and search[2] == y:
            searchQueryData = blocks[i]
            break
        i+=1
    if searchQueryData != None:
        ifBlock = True
        blockTurtle = searchQueryData[0]
        x = searchQueryData[1]
        y = searchQueryData[2]
        return (ifBlock,blockTurtle,x,y,i)
    elif searchQueryData == None:
        ifBlock = False
        blockTurtle = None
        x = None
        y = None
        return (ifBlock,blockTurtle,x,y,i)
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
    searchOutput = searchBlocks(blocks,x,y)
    if searchOutput[0]:
        print(blocks)
        searchOutput[1].hideturtle()
        blocks.remove((searchOutput[1],searchOutput[2],searchOutput[3]))
        screen.update()
        print(blocks)
    else:
        print('no block to break there')
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
    searchOutput = searchBlocks(blocks,x,y)
    if not searchOutput[0]:
        currentTurtle = turtle.Turtle()
        currentTurtle.speed(0)
        currentTurtle.hideturtle()
        currentTurtle.up()
        currentTurtle.goto((x*64)-32,(y*64)-32)
        currentTurtle.shape(currentBlock.image)
        print(currentBlock)
        currentTurtle.showturtle()
        blocks.append((currentTurtle,x,y))
        print(blocks)
    else:
        print('there is already a block in that location')
#* call functions
screen.onscreenclick(gotoBreakBlock,1)
screen.onscreenclick(gotoPlaceBlock,3)
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
screen.onkeypress(slotFive,'5')

screen.listen()
screen.mainloop()


