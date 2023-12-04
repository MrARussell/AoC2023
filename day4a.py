file=open("day4.txt","r")
total = 0

for line in file:
    line = line.strip()
    start = line.index(":")
    middle = line.index("|")
    actual = line[start+2:middle]
    yours = line[middle+2:]
    winners = actual.split()
    for i in range(len(winners)):
        if len(winners[i])==1:
            winners[i]="0"+winners[i]
    numbers = yours.split()
    for i in range(len(numbers)):
        if len(numbers[i])==1:
            numbers[i]="0"+numbers[i]
    count = -1
    for i in numbers:
        if i in winners:
            count+=1
    if count >= 0:
        total += 2**count
print(total)

    
    
