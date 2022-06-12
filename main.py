import turtle
import time
import queue

degrees = 30
branch_size = input("What should be the branch size?")
branch_size = int(branch_size)
branch_decay = input("What should be the branch decay?")
branch_decay = float(branch_decay)
termination_num = input("When should the tree stop?")
termination_num = int(termination_num)

turtle = turtle.Turtle()
turtle.speed(0)

turtle.penup()
turtle.goto(0, -300)
turtle.left(90)
turtle.pendown()

queue_x = queue.Queue()
queue_y = queue.Queue()
queue_rotation = queue.Queue()
queue_branch = queue.Queue()
queue_x.put(0)
queue_y.put(-300)
queue_rotation.put(90)
queue_branch.put(branch_size)

while not queue_x.empty():
    x = queue_x.get()
    y = queue_y.get()
    rotation = queue_rotation.get()
    size = queue_branch.get()
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(rotation)
    turtle.forward(size)

    if size >= termination_num:
        queue_x.put(turtle.xcor())
        queue_y.put(turtle.ycor())
        queue_rotation.put(rotation - degrees)
        queue_branch.put(size * branch_decay)

        queue_x.put(turtle.xcor())
        queue_y.put(turtle.ycor())
        queue_rotation.put(rotation + degrees)
        queue_branch.put(size * branch_decay)

time.sleep(100000000)
