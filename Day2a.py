file=open("day2.txt","r")
total = 0
for line in file:
    current = line.split(":")
    game = current[0]
    game = int(game[5:])
    handfulls = current[1].split(";")
    valid = True
    for outcome in handfulls:
        result = outcome.split(",")
        for i in result:
            number = ""
            for letter in i:
                if letter.isdecimal():
                    number += letter
            number = int(number)
            if "red" in i:
                if number > 12:
                    valid = False
            if "green" in i:
                if number > 13:
                    valid = False
            if "blue" in i:
                if number > 14:
                    valid = False
    if valid:
        total += game
print(total)
file.close()
