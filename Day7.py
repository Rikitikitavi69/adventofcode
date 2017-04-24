"""
--- Day 7: Some Assembly Required ---

This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately, little Bobby is a little under the recommended age range, and he needs help assembling the circuit.

Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a signal from one source, but can provide its signal to multiple destinations. A gate provides no signal until all of its inputs have a signal.

The included instructions booklet describes how to connect the parts together: x AND y -> z means to connect wires x and y to an AND gate, and then connect its output to wire z.

For example:

123 -> x means that the signal 123 is provided to wire x.
x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.
Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason, you'd like to emulate the circuit instead, almost all programming languages (for example, C, JavaScript, or Python) provide operators for these gates.

For example, here is a simple circuit:

123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
After it is run, these are the signals on the wires:

d: 72
e: 507
f: 492
g: 114
h: 65412
i: 65079
x: 123
y: 456
In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?

--- Part Two ---

Now, take the signal you got on wire a, override wire b to that signal, and reset the other wires (including wire a). What new signal is ultimately provided to wire a?
"""

import numpy

with open("7.txt") as f:
    inputdata = []
    for line in f:
        inputdata.append(line.strip())

inputdata2 = []

for line in inputdata:
    a,b = line.split('->')
    c = [a.strip().split(" "), b.strip()]
    inputdata2.append(c)

##################################################

def RSHIFT(a, b):
    result = numpy.uint16(a) >> int(b)
    if result > 65535:
        result = result % 65535
    return int(result)

def LSHIFT(a, b):
    result = numpy.uint16(a) << int(b)
    if result > 65535:
        result = result % 65535
    return int(result)

def OR(a, b):
    result = numpy.uint16(a) | numpy.uint16(b)
    return int(result)

def AND(a, b):
    result = numpy.uint16(a) & numpy.uint16(b)
    return int(result)

def NOT(a):
    #result = ~ numpy.uint16(a)
    result = 65535 - int(a)
    return int(result)

##################################################

known_vars = {}

while 'a' not in known_vars.keys():
    if 'a' in known_vars:
        break
    for i in inputdata2:

        if i[0][0].isdigit() and i[1] not in known_vars.keys() and len(i[0]) == 1:
            known_vars[i[1]] = int(i[0][0])

        elif 'AND' in i[0] and (i[0][0] in known_vars or i[0][0].isdigit()) and (i[0][2] in known_vars or i[0][2].isdigit()) and len(i[0]) == 3:
            a = i[0][0] if i[0][0].isdigit() else known_vars[i[0][0]]
            b = i[0][2] if i[0][2].isdigit() else known_vars[i[0][2]]
            known_vars[i[1]] = AND(a, b)

        elif 'OR' in i[0] and (i[0][0] in known_vars or i[0][0].isdigit()) and (i[0][2] in known_vars or i[0][2].isdigit()) and len(i[0]) == 3:
            a = i[0][0] if i[0][0].isnumeric() else known_vars[i[0][0]]
            b = i[0][2] if i[0][2].isnumeric() else known_vars[i[0][2]]
            known_vars[i[1]] = OR(a, b)

        elif 'LSHIFT' in i[0] and i[0][0] in known_vars and len(i[0]) == 3:
            known_vars[i[1]] = LSHIFT(known_vars[i[0][0]], i[0][2])

        elif 'RSHIFT' in i[0] and i[0][0] in known_vars and len(i[0]) == 3:
            known_vars[i[1]] = RSHIFT(known_vars[i[0][0]], i[0][2])

        elif 'NOT' in i[0] and i[0][1] in known_vars and len(i[0]) == 2:
            known_vars[i[1]] = NOT(known_vars[i[0][1]])

        elif i[0][0] in known_vars and i[1] not in known_vars.keys() and len(i[0]) == 1:
                known_vars[i[1]] = known_vars[i[0][0]]

print(known_vars['a'])
