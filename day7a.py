def add(array,hand,bid,score):
    if len(array[0]) == 0:
        array[0].append(hand)
        array[1].append(bid)
        array[2].append(score)
    else:
        index = 0
        found = False
        while index < len(array[2]) and found == False:
            if score > array[2][index]:
                index+=1
            else:
                found = True
        array[0].insert(index,hand)
        array[1].insert(index,bid)
        array[2].insert(index,score)

file = open("day7.txt","r")
five =[[],[],[]]
four = [[],[],[]]
fullHouse = [[],[],[]]
three = [[],[],[]]
twoPair = [[],[],[]]
pair = [[],[],[]]
high = [[],[],[]]
special = ["T","J","Q","K","A"]
for line in file:
    line = line.strip()
    result = line.split()
    hand = result[0]
    cards = [["2","3","4","5","6","7","8","9","T","J","Q","K","A"],[0]*13]
    for card in hand:
        for i in range(13):
            if card == cards[0][i]:
                cards[1][i]+=1
    handCards = []
    for card in hand:
        if card in special:
            card = 10 + special.index(card)
        handCards.append(card)
    score = 0
    for i in range(5):
        score += 13**(4-i)*int(handCards[i])
    twos = 0
    for i in cards[1]:
       if i == 2:
           twos += 1
    if max(cards[1])==5:
        add(five,hand,int(result[1]),score)
    elif max(cards[1])==4:
        add(four,hand,int(result[1]),score)
    elif max(cards[1]) == 3:
        if twos == 1:
            add(fullHouse,hand,int(result[1]),score)
        else:
            add(three,hand,int(result[1]),score)
    elif twos == 2:
        add(twoPair,hand,int(result[1]),score)
    elif twos == 1:
        add(pair,hand,int(result[1]),score)
    else:
        add(high,hand,int(result[1]),score)
file.close()
answer = 0
position = 1
for i in high[1]:
    answer += position * i
    position += 1
for i in pair[1]:
    answer += position * i
    position += 1
for i in twoPair[1]:
    answer += position * i
    position += 1
for i in three[1]:
    answer += position * i
    position += 1
for i in fullHouse[1]:
    answer += position * i
    position += 1
for i in four[1]:
    answer += position * i
    position += 1
for i in five[1]:
    answer += position * i
    position += 1
print(answer)
