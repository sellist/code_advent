with open('day 1/input.txt') as x:
    lines = x.readlines()

depths = [int(x) for x in lines]
count = 0

for n, x in enumerate(depths):
    if x > depths[n-1]:
        count += 1

print(count)