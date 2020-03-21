from Array_ADT import Array
import random

value_list = Array(10)
for i in range(len(value_list)):
    value_list[i] = random.random()

for value in value_list:
    print(value)


counters = Array(127)
counters.clear(0)

file = open('somefile.txt', 'r')
for line in file:
    for letter in line:
        code = ord(letter)
        counters[code] += 1

file.close()

for i in range(26):
    print("%c - %4d     %c - %4d"%(chr(65+i), counters[65+i], chr(97+i), counters[97+i]))