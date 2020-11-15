# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)


count = 0
textneed = 0
for line in fh:
	if not line.startswith("X-DSPAM-Confidence:") : continue
	textneed += float(line[20:-1].strip()) #adding loop number together
	count = count+1

print('Average spam confidence:', (textneed/count))
