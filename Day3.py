"""
--- Day 3: Perfectly Spherical Houses in a Vacuum ---

Santa is delivering presents to an infinite two-dimensional grid of houses.

He begins by delivering a present to the house at his starting location, and then an elf at the North Pole calls him via radio and tells him where to move next. Moves are always exactly one house to the north (^), south (v), east (>), or west (<). After each move, he delivers another present to the house at his new location.

However, the elf back at the north pole has had a little too much eggnog, and so his directions are a little off, and Santa ends up visiting some houses more than once. How many houses receive at least one present?

For example:

> delivers presents to 2 houses: one at the starting location, and one to the east.
^>v< delivers presents to 4 houses in a square, including twice to the house at his starting/ending location.
^v^v^v^v^v delivers a bunch of presents to some very lucky children at only 2 houses.

--- Part Two ---

The next year, to speed up the process, Santa creates a robot version of himself, Robo-Santa, to deliver presents with him.

Santa and Robo-Santa start at the same location (delivering two presents to the same starting house), then take turns moving based on instructions from the elf, who is eggnoggedly reading from the same script as the previous year.

This year, how many houses receive at least one present?

For example:

^v delivers presents to 3 houses, because Santa goes north, and then Robo-Santa goes south.
^>v< now delivers presents to 3 houses, and Santa and Robo-Santa end up back where they started.
^v^v^v^v^v now delivers presents to 11 houses, with Santa going one direction and Robo-Santa going the other.
"""
##########Part 1##########

srcStr=[]
with open("3.txt", "r", 1) as f:
	for line in f:
		srcStr.extend(list(line))

gridlist = ['0,0']
santa = [0,0,'s']

for x in range(len(srcStr)):

    if srcStr[x] == "^":
        santa = [santa[0] + 1, santa[1], santa[2]]
    elif srcStr[x] == "v":
        santa = [santa[0] - 1, santa[1], santa[2]]
    elif srcStr[x] == ">":
        santa = [santa[0], santa[1] + 1, santa[2]]
    elif srcStr[x] == "<":
        santa = [santa[0], santa[1] - 1, santa[2]]

    if not str(santa[0]) + ',' + str(santa[1]) in gridlist:
        gridlist.append(str(santa[0]) + ',' + str(santa[1]))

print("Answer for part1: ", len(gridlist))

##########Part 2##########

gridlist = ['0,0']
santa = [0,0,'s']
robot = [0,0,'r']

for x in range(len(srcStr)):

    if x % 2 == 0:
        mover = santa
    else:
        mover = robot

    if srcStr[x] == "^":
        mover = [mover[0] + 1, mover[1], mover[2]]
    elif srcStr[x] == "v":
        mover = [mover[0] - 1, mover[1], mover[2]]
    elif srcStr[x] == ">":
        mover = [mover[0], mover[1] + 1, mover[2]]
    elif srcStr[x] == "<":
        mover = [mover[0], mover[1] - 1, mover[2]]

    if not str(mover[0]) + ',' + str(mover[1]) in gridlist:
        gridlist.append(str(mover[0]) + ',' + str(mover[1]))

    if mover[2] == 's':
        santa = mover
    else:
        robot = mover

print("Answer for part2: ", len(gridlist))
