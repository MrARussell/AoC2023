def check_number(line,number):
    if len(line)<len(number):
        return False
    place = 0
    same = True
    while same and place < len(number):
        if line[place]==number[place]:
            place+=1
        else:
            same = False
    return same

def get_number(line,start,change):
    words=["zero","one","two","three","four","five","six","seven","eight","nine"]
    place = start
    result="False"
    while result=="False":
        if line[place].isdecimal():
            result=int(line[place])
        for i in range(10):
            if check_number(line[place:],words[i]):
                result = i
        place += change
    return result

file=open("day1a.txt","r")
total = 0
for line in file:
    first = get_number(line,0,1)
    second = get_number(line,len(line)-1,-1)
    total += 10*first + second
file.close()
print(total)
