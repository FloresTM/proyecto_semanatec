"""Pacman, classic arcade game.

Exercises

1. Change the board..
2. Change the number of ghosts..
3. Change where pacman starts..
4. Make the ghosts faster/slower..
5. Make the ghosts smarter.
"""

from random import choice

# turtle is a library that allows people to create shapes and figures.
# It is used to develop smaller games and programs.
from turtle import up, goto
from turtle import update, ontimer
from turtle import setup, hideturtle
from turtle import onkey
from turtle import listen
from turtle import done
from turtle import tracer
from turtle import clear
from turtle import dot
from turtle import bgcolor
from turtle import Turtle

# vector is imported and use to indicate the position of the objects.
from freegames import floor, vector

# Initially the score will be 0.
state = {'score': 0}
path = Turtle(visible=False)
writer = Turtle(visible=False)

# aim sets the direction of the object when initiated,
# since it is postive in the x-axis is starting direction is to the right
aim = vector(5, 0)

# Vector indicates the initial position of this object in x and y axis.
pacman = vector(-40, 0)

# As we can see, 4 ghosts or enemies will appear at the beggining of the game.
# We can also see the ghosts have a predetermined position as indicated by
# the vectors which are (x, y) axis.
# the second vector indicates the starting direction of the object.
# Also, the direction integrates the speed, oringinally the speed was 5,
# but I changed it to 10 to make the ghosts faster.
ghosts = [
    [vector(-180, 160), vector(10, 0)],
    [vector(-180, -160), vector(0, 10)],
    [vector(120, 160), vector(0, -10)],
    [vector(100, -160), vector(-10, 0)],
    # I created the last ghost for the excercise
    [vector(0, 80), vector(-10, 0)],
]

# fmt: off

# A binary language is used to create the "arena". In total we have a playing
# field of 20 x 20.
# As we know, a 0 indicates false, and a 1 indicates true. When we see a zero
# the tile will be "deactivated/blocked off."
# If the tiles are blocked of they will act as walls since they don't allow
# any movement.
# On the other hand a 1(true) will let the objects trough.
tiles = [
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0,
    0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0,
    0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0,
    0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 0,
    0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0,
    0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0,
    0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
]
# fmt: on


def square(x, y):
    """Draw square using path at (x, y)."""
    path.up()
    path.goto(x, y)
    path.down()
    path.begin_fill()

    for count in range(4):
        path.forward(20)
        path.left(90)

    path.end_fill()


def offset(point):
    """Return offset of point in tiles."""
    x = (floor(point.x, 20) + 200) / 20
    y = (180 - floor(point.y, 20)) / 20
    index = int(x + y * 20)
    return index


def valid(point):
    """Return True if point is valid in tiles."""
    index = offset(point)

    if tiles[index] == 0:
        return False

    index = offset(point + 19)

    if tiles[index] == 0:
        return False

    return point.x % 20 == 0 or point.y % 20 == 0


# the function world is used to indicate the board and its
# properties such as its color
def world():
    """Draw world using path."""

    # Here we specify the color of the background of the board
    bgcolor('blue')

    # We indicate the color of the path
    path.color('gray')

    for index in range(len(tiles)):
        tile = tiles[index]

        if tile > 0:
            x = (index % 20) * 20 - 200
            y = 180 - (index // 20) * 20
            square(x, y)

            if tile == 1:
                path.up()
                path.goto(x + 10, y + 10)
                path.dot(2, 'white')


# this section of the code will allow us to display or to 'write' the score.
def move():
    """Move pacman and all ghosts."""
    writer.undo()
    writer.write(state['score'])

    clear()

    # this portion of the code will be used to update the score
    if valid(pacman + aim):
        pacman.move(aim)

    index = offset(pacman)

    if tiles[index] == 1:
        # the squares that have been covered will changed to a 2
        tiles[index] = 2

        # this will update the score by one point
        state['score'] += 1
        x = (index % 20) * 20 - 200
        y = 180 - (index // 20) * 20
        square(x, y)

    up()
    goto(pacman.x + 10, pacman.y + 10)

    # the first number indicates the size of the object
    # and the second indicates the color
    dot(20, 'purple')

    # this sets the movement of the ghost
    for point, course in ghosts:
        if valid(point + course):
            point.move(course)
        else:
            # we can see the 4 option in which the ghost can move
            # oringinally the speed was 5, but I changed it to 10
            # to make the ghosts faster.
            options = [
                vector(10, 0),
                vector(-10, 0),
                vector(0, 10),
                vector(0, -10),
            ]
            plan = choice(options)
            # the ghost can move towards x(left or why), or towards
            # y (up or down)
            course.x = plan.x
            course.y = plan.y

        up()
        goto(point.x + 10, point.y + 10)

    # the first number indicates the size of the object and the
    # second indicates the color

        dot(20, 'green')

    update()

    # this section finishes the game in case a ghost hits pacman
    for point, course in ghosts:
        if abs(pacman - point) < 20:
            return

    ontimer(move, 100)


# this function will allow the user to change the postion of the
# object (pacman) when a key is pressed.
def change(x, y):
    """Change pacman aim if valid."""

    if valid(pacman + vector(x, y)):
        aim.x = x
        aim.y = y
        # this allows to change the direction of the object with our arrows.


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
# position of the text/score
writer.goto(160, 160)
# color of the text/score
writer.color('white')
writer.write(state['score'])
listen()
onkey(lambda: change(5, 0), 'Right')
onkey(lambda: change(-5, 0), 'Left')
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')

# we need to call our funtion world used for the board
world()
# we need to call our funtion move
move()
done()
