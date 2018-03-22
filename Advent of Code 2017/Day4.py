inp = [i.strip().split() for i in open('input.txt', 'r').readlines()]

p1 = 0
p2 = 0

for i in inp:
    if len(set(i)) == len(i):
        p1 += 1
    if len(set(''.join(sorted(u)) for u in i)) == len(i):
        p2 += 1

print ("Part 1:", p1)
print ("Part 2:", p2)