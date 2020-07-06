import random
outfile = "Max_dist.txt"
afile = open(outfile,"w")
for i in range(1000):
	line = str(random.randint(10000,99999)) +'\n'
	afile.write(line)
afile.close()

