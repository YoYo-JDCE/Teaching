fname = input("Enter file name: ")
fh = open(fname)
counts = dict()
for line in fh:
    if not line.startswith('From'):
        continue
    if line.startswith('From:'):
        continue
    else:
        line = line.split()
        time = line[5]
        line = time.split(':')
        words = line[0]
counts[words]=counts.get(words,0)+1

counts = sorted(counts.items())

for v,k in counts:
    print(v,k)
