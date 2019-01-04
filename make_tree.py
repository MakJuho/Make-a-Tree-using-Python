#Recursive Tree Challenge - www.101computing.net/recursive-tree-challenge
import turtle
import math

PROGNAME = 'Tree'

myPen = turtle.Turtle()
myPen.ht()
myPen.speed(0)
myPen.pencolor('#964B00')


#Recursive function to draw a tree, branch by branch
def drawTree(level,size,angle):
  if level >= 0:


    myPen.forward(size)
    # modified code #1
    myPen.left(angle)
    myPen.forward(4*size/5)
    myPen.backward(4*size/5)
    myPen.right(2*angle)
    myPen.forward(4*size/5)
    myPen.backward(4*size/5)
    myPen.left(2*angle)

    #  ~1
#     left(angle)
    drawTree(level-1,4*size/5,angle)
    
    myPen.right(2*angle)
    #Draw right branch of the tree
    drawTree(level-1,4*size/5,angle)
    myPen.left(angle)
    myPen.forward(-size)
    
  else:
    #Stop the recursion
    return

#Main Program Starts Here  

myPen.up()
myPen.goto(0,-230)
myPen.left(90)
myPen.down()

#Draw a tree using a recursive function
size = 150
angle = 20 
level = 7

drawTree(level,4*size/5,angle)

turtle.done()