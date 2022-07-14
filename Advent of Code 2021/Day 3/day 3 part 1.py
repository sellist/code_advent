with open('input.txt') as x:
    lines = x.readlines()
    lines = [x.strip() for x in lines]
    power = [' ' for x in range(0, len(lines[0]))]

for x in range(0, len(lines[0])):
    column = []
    for line in lines:
        column.append(int(line[x]))
    if sum(column) > (len(lines) / 2):
        power[x] = 1
    else:
        power[x] = 0

pos = ['1' if x == 1 else '0' for x in power]
neg = ['0' if x == 1 else '1' for x in power]

a = ''.join(pos)
b = ''.join(neg)

print(int(a, 2) * int(b, 2))