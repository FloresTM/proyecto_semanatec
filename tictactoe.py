"""Tic Tac Toe

Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""

import sys

from turtle import up, goto, down, circle, update, color
from turtle import setup, hideturtle, tracer, onscreenclick, done
import turtle

from freegames import line

import sys

sam = turtle.Turtle()
mike = turtle.Turtle()
mike.hideturtle()
sam.hideturtle()

# La definición de grid nos permite crear el fondo
# Las lineas que sirven para formar el fondo.


def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)

# Definir draw nos permite dibujar al jugador que usará la X.


def drawx(x, y):
    """Draw X player."""
    mike.color('blue')
    mike.up()
    mike.goto(x + 50, y + 75)
    mike.down()
    mike.goto(x + 85, y + 40)
    mike.up()
    mike.goto(x + 85, y + 75)
    mike.down()
    mike.goto(x + 50, y + 40)
    mike.up()

    # Las lineas de código de abajo son simplemente
    # Para ilustrar los puntos que se usaron inicialmente
    # (ya achicados)
    # line(x + 50, y + 75, x + 85, y + 40)
    # line(x + 85, y + 75, x + 50, y + 40)

   
    
# Drawo dibuja al jugador que usará O.


def drawo(x, y):
    """Draw O player."""
    sam.hideturtle()
    sam.color('red')
    sam.up()
    sam.goto(x + 67, y + 20)
    sam.down()
    sam.circle(35)
    
    

# Detecta donde se pulsa en el espacio, así que
# Ahí pone el simbolo correspondiente


def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawx, drawo]

# Dibuja la O o la X en el cuadro que se presione.


def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)
    player = state['player']
    draw = players[player]
    draw(x, y)
    update()
    state['player'] = not player


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
