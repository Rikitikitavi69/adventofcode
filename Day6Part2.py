"""
--- Part Two ---

You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from Ancient Nordic Elvish.

The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. The lights all start at zero.

The phrase turn on actually means that you should increase the brightness of those lights by 1.

The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.

The phrase toggle actually means that you should increase the brightness of those lights by 2.

What is the total brightness of all lights combined after following Santa's instructions?

For example:

turn on 0,0 through 0,0 would increase the total brightness by 1.
toggle 0,0 through 999,999 would increase the total brightness by 2000000.
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
        for j in range(x0, x1+1):
            board[i][j] += 1

def turnoff(x0, y0, x1, y1):
    for i in range(y0, y1+1):
        for j in range(x0, x1+1):
            if board[i][j] != 0:
                board[i][j] -= 1
     
def toggle(x0, y0, x1, y1):
    for i in range(y0, y1+1):
        for j in range(x0, x1+1):
            board[i][j] += 2

			
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

		
total_brightness = 0
for i in board:
    for j in i:
        total_brightness += j

print(total_brightness)