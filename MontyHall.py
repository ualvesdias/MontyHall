import random as rd

wins = 0
losses = 0
games = 0
change = True

while games < 100000:
    doors = ['CAR', 'GOAT', 'GOAT']
    rd.shuffle(doors)
    windoor = doors.index('CAR')
    firstchoice = rd.choice([0,1,2])

    while True:
        opened = rd.choice([0,1,2])
        if opened not in {windoor, firstchoice}:
            doors[opened] = 'OPENED GOAT'
            break

    if change:
        for door in doors:
            if doors.index(door) == firstchoice or door == 'OPENED GOAT':
                continue
            else:
                secondchoice = doors.index(door)

    if not change and doors[firstchoice] == 'CAR':
        wins += 1
    elif not change and doors[firstchoice] == 'GOAT':
        losses += 1
    elif change and doors[secondchoice] == 'CAR':
        wins +=1
    elif change and doors[secondchoice] == 'GOAT':
        losses += 1

    games +=1
    print('WINS: %i ---- LOSSES: %i ---- WIN RATE: %.2f' % (wins, losses, wins/games), end='\r', flush=True)

print('WINS: %i ---- LOSSES: %i ---- WIN RATE: %.2f' % (wins, losses, wins/games))
