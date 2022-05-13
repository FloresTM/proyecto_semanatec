from turtle import update
from turtle import setup, hideturtle, tracer, onscreenclick, done
import turtle

from freegames import line

# Importamos todas las turtles que se van a usar, conozcan a Sam
# Y a Mike, son muy amables solo que muy timidos.
sam = turtle.Turtle()
mike = turtle.Turtle()
mike.hideturtle()
sam.hideturtle()

d = {}

s1 = True
s2 = True
s3 = True
s4 = True
s5 = True
s6 = True
s7 = True
s8 = True
s9 = True

# La definición de grid nos permite crear el fondo
# Las lineas que sirven para formar el fondo.


def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)

# Definir draw nos permite dibujar al jugador que usará la X.
# Para esto utilizamos a nuestro amigo Mike.


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

# Se definen las variables de los espacios como
# Globales para evitar errores. Además de eso
# Se le añaden varios IFs para que así el
# Código detecte cuando un espacio ya fue
# Utilizado


def tap(x, y):
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)
    global s1
    global s2
    global s3
    global s4
    global s5
    global s6
    global s7
    global s8
    global s9
    if x == -200 and y == -200 and s1 is True:
        player = state['player']
        draw = players[player]
        draw(x, y)
        update()
        state['player'] = not player
        s1 = False
    elif x == -200 and y == -67 and s2 is True:
        player = state['player']
        draw = players[player]
        draw(x, y)
        update()
        state['player'] = not player
        s2 = False
    elif x == -200 and y == 66 and s3 is True:
        player = state['player']
        draw = players[player]
        draw(x, y)
        update()
        state['player'] = not player
        s3 = False
    elif x == -67 and y == -200 and s4 is True:
        player = state['player']
        draw = players[player]
        draw(x, y)
        update()
        state['player'] = not player
        s4 = False
    elif x == -67 and y == -67 and s5 is True:
        player = state['player']
        draw = players[player]
        draw(x, y)
        update()
        state['player'] = not player
        s5 = False
    elif x == -67 and y == 66 and s6 is True:
        player = state['player']
        draw = players[player]
        draw(x, y)
        update()
        state['player'] = not player
        s6 = False
    elif x == 66 and y == -200 and s7 is True:
        player = state['player']
        draw = players[player]
        draw(x, y)
        update()
        state['player'] = not player
        s7 = False
    elif x == 66 and y == -67 and s8 is True:
        player = state['player']
        draw = players[player]
        draw(x, y)
        update()
        state['player'] = not player
        s8 = False
    elif x == 66 and y == 66 and s9 is True:
        player = state['player']
        draw = players[player]
        draw(x, y)
        update()
        state['player'] = not player
        s9 = False
    else:
        print('Selecciona otra casilla')


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()

# X = -200, -67, 66
# Y = -200, -67, 66
