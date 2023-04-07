su = 0
with open('g') as g:
    for line in g:
        su += int(line)
print(str(su)[:10])
