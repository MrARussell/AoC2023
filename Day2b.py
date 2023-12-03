file=open("day2.txt","r")
total = 0
for line in file:
    current = line.split(":")
    game = current[0]
    game = int(game[5:])
    red = green = blue = 0
    handfulls = current[1].split(";")
    for outcome in handfulls:
        result = outcome.split(",")
        for i in result:
            number = ""
            for letter in i:
                if letter.isdecimal():
                    number += letter
            number = int(number)
            if "red" in i:
                if number > red:
                    red = number
            if "green" in i:
                if number > green:
                    green = number
            if "blue" in i:
                if number > blue:
                    blue = number
    total += red * green * blue 
print(total)
file.close()
