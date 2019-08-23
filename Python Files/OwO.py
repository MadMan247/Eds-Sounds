static = 1
while static == 1:
    line = ''
    HP = int(input())
    hpupct = 0
    while hpupct != HP:
        line = line + "-"
        hpupct = hpupct + 1
    print(line)
