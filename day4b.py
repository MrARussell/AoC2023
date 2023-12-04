file=open("day4.txt","r")

num_of_cards = [0]
position = 0

for line in file:
    num_of_cards[position]+=1
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
    count = 0
    for i in numbers:
        if i in winners:
            count+=1
    position += 1
    for i in range(count):
        num_of_cards.append(0)
        num_of_cards[position + i] += num_of_cards[position-1]
file.close()
total = 0
for i in num_of_cards:
    total += i
print(total)

    
    
