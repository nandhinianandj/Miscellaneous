import fileinput

lines = list()
for line in fileinput():
    lines.append(int(line))
