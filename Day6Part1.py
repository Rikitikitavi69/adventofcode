"""
--- Day 6: Probably a Fire Hazard ---

Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs. Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

For example:

turn on 0,0 through 999,999 would turn on (or leave on) every light.
toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.
After following the instructions, how many lights are lit?
"""

import re

inputdata = ""

with open("6.txt", "r", 1) as f:
    inputdata = f.read().split("\n")

coord = []
instruct = []

for line in inputdata:
    coord.append(list(map(int, re.findall(r'[0-9]+', line))))
    instruct.append(re.findall(r'[a-z]+', line))

for line in instruct:
    if len(line) == 3:
        line[0] = line[0] + " " + line[1]
        line.remove(line[1])
    line.remove(line[1])


board = []
for line in range(0,1000):
    board.append([0]*1000)


def turnon(x0, y0, x1, y1):
    for i in range(y0, y1+1):
        for j in range(x0,x1+1):
            board[i][j] = 1

def turnoff(x0, y0, x1, y1):
    for i in range(y0, y1+1):
        for j in range(x0, x1+1):
            board[i][j] = 0

def toggle(x0, y0, x1, y1):
    for i in range(y0, y1+1):
        for j in range(x0, x1+1):
            if board[i][j] == 1:
                board[i][j] = 0
            else:
                board[i][j] = 1


for i in zip(coord, instruct):

    x_start = int(i[0][0])
    y_start = int(i[0][1])
    x_end = int(i[0][2])
    y_end = int(i[0][3])

    if i[1][0] == 'turn on':
        turnon(x_start, y_start, x_end, y_end)

    elif i[1][0] == 'turn off':
        turnoff(x_start, y_start, x_end, y_end)

    elif i[1][0] == 'toggle':
        toggle(x_start, y_start, x_end, y_end)
		
        
count_on = 0

for i in board:
    for j in i:
        if j == 1:
            count_on += 1
print(count_on)