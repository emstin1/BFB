#!usr/bin/env python3

#for compiling c code
#cc -std=c99 -Wall $filename.c -o $filename


"""
    Transpiling from Brainfuck intermediate into C
    Copyright (C) 2018  Eric Stinger

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from sys import argv

transpile = {'>': '++ptr;\n', '<': '--ptr;\n', '+': '++*ptr;\n', '-': '--*ptr;\n',
             '.': 'putchar(*ptr);\n', ',': '*ptr=getchar;\n', '[': 'while (*ptr) {\n', ']': '}\n',
             'start': '#include <stdio.h>\n\n\nchar array[30000] = {0};\nchar *ptr=array;\n'}

bf_file_open = argv[1]
c_file = "{}.c".format(bf_file_open.split('.')[0])

with open(bf_file_open, 'r') as bf:
    bf_file = bf.read()

c_file_chars = transpile['start']
c_file_chars += 'int main() {\n'

bf_chars = '[+-<>,.]'

for char in bf_file:
    if char in bf_chars:
        c_file_chars += transpile[char]

c_file_chars += '}'

with open(c_file, 'w') as cf:
    cf.write(c_file_chars)
