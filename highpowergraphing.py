# Graphing Software
# Source Code (C) James Thomson-Hicks
# NO STEALSIES OR COMMERCIAL USE PERMITTED
from turtle import *
from random import randint
x_max = 25 # The maximum x value to graph. The minimum x is set to the negative of this value.
y_max = 25 # The maximum y value to graph. The minimum y is set to the negative of this value.
height = 500 # The height of the area to graph. As with the x and y maximum values, the area will be graphed from y=-height to y=height.
width = 500 # The width of the area to graph. As with the x and y maximum values, the area will be graphed from x=-width to x=width.
precision = 1 # How many values to calculate and move to for each x value. Increased values will give decreased speed but smoother lines. In order to not increase time taken with no effectiveness, this value should be set to the quotient of the height and y_max variables.
grid_x = 1 # The interval between gridlines on the x-axis.
grid_y = 1 # The interval between gridlines on the y-axis.
ht() # Stop the pointer appearing on screen
speed(0) # Fastest turtle speed
colormode(255) # Enable EpiC RAzeR CHRomA RgB for lines
lines = [ # Lines are stored in this array. Each line is input as an array with each coefficient, highest to lowest power (e.g. y=3x-4 is [3, 4])
    [3, -4],
    [1, 0, 0]
    ]
scatter_lines = [
    [
        [0,0],1,
    ],
    [
        [0,0],[0,1],[1,2],0
    ],
]
for x in range(-x_max, x_max + grid_x, grid_x):
    pu()
    goto(x*width/x_max, height)
    color(192, 192, 192)
    pd()
    goto(x*width/x_max, -height)
for y in range(-y_max, y_max, grid_y):
    pu()
    goto(width, y*height/y_max)
    color(192, 192, 192)
    pd()
    goto(-width, y*height/y_max)
color(0, 0, 0)
pu()
goto(0, 1000)
pd()
goto(0, -1000)
pu()
goto(-1000, 0)
pd()
goto(1000, 0)
pu()
def calc(line, x):
    y = 0
    for i in range(1, len(line)+1, 1):
        y += line[i-1]*(x**(len(line)-i)) # Add to the total the result of multiplying the coefficient by x raised to the power of the index of the coefficient minus one.
    return y
for line in lines:
    pu()
    color(randint(0, 255),randint(0, 255),randint(0, 255))
    for x in range(int(-x_max*precision), int(x_max*precision), 1):
        y = calc(line, x)*height/y_max
        goto(x*width/x_max, y)
        pd()
for line in scatter_lines:
    pu()
    color(randint(0, 255),randint(0, 255),randint(0, 255))
    if line[-1]:
        for i in range(0, len(line)-1, 1):
            x = line[i][0]
            y = line[i][1]
            goto(x, y)
            pd()
            dot(5)
    else:
        for i in range(0, len(line)-1, 1):
            x = line[i][0]
            y = line[i][1]
            pu()
            goto(x*width/x_max,y*height/y_max)
            pd()
            dot(5)
exitonclick()
