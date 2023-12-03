def check(y,x):
    value = "0"
    loop = False
    global schematic
    while schematic[y][x].isdigit() and schematic[y][x]!="." and x > 0:
        loop = True
        x = x-1
    if loop and (schematic[y][x]=="." or not schematic[y][x].isdigit()) or x<0:
        x+=1
    while schematic[y][x].isdigit() and schematic[y][x] != ".":
        value += schematic[y][x]
        if schematic[y][x].isdigit():
            schematic[y][x]="."
        x+=1
        if x == length:
            break
    return int(value)

file=open("day3.txt","r")
total = 0
row = 0
schematic = []

for line in file:
    line = line.strip()
    schematic.append([])
    for character in line:
        schematic[row].append(character)
    row+=1
file.close()

for y in range(len(schematic)):
    for x in range(len(schematic[y])):
        if schematic[y][x] != "." and not schematic[y][x].isdigit():
            length = len(schematic[y])
            if y > 0 and x > 0:
                total += check(y-1,x-1)
            if y > 0:
                total += check(y-1,x)
            if y > 0 and x < length:
                total += check(y-1,x+1)
            if x > 0:
                total += check(y,x-1)
            if x < length:
                total += check(y,x+1)
            if y < len(schematic) and x > 0:
                total += check(y+1,x-1)
            if y < len(schematic):
                total += check(y+1,x)
            if y < len(schematic) and x < length:
                total += check(y+1,x+1)
print(total)
        
