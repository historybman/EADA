fname = input("enter the file name: ")

def text_prep(file):
	a = ''
	fout = open(file, 'w')
	for line in fout:
		line = line.strip()
		fout.write(line)
	fout.close()

text_prep(fname)