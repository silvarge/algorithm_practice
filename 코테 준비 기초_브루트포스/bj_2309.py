import sys
input = sys.stdin.readline

dwarf = []

for i in range(9):
    dwarf.append(int(input().strip()))

diff = sum(dwarf)-100

for i in dwarf:
    if (diff-i) in dwarf and i != (diff-i):
        dwarf.remove(i)
        dwarf.remove(diff-i)
        break

dwarf.sort()

for i in dwarf:
    print(i)
