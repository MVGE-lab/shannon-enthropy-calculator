import math
import sys
from pylab import *
w = open(sys.argv[1]+'.output', 'w')
ids = []
seqs = []
n = 0
print("Reading from FASTA file....\n")
with open(sys.argv[1], 'r') as r:
	for line in r:
		if line[0] == ">":
			ids.append(line[1:len(line)-1])
			n=1
		else:
			l = line.strip("\n")
			if n == 1:
				seqs.append(l)
				n = 0
			else:
				seqs[len(seqs)-1] = seqs[len(seqs)-1]+l
print("Read "+str(len(seqs))+"sequences, "+str(len(seqs[0]))+" bases length")
print("Data is ready for processing\n")
Shan = []
print("Calculating Shannon enthropy....\n")
for j in range(0,len(seqs[0])):
    Acount = 0
    Gcount = 0
    Ccount = 0
    Tcount = 0
    GAPcount = 0
    for i in range(0, len(seqs)):
        if (seqs[i][j] == "A" or seqs[i][j] == "a"):
            Acount = Acount + 1
        elif (seqs[i][j] == "G" or seqs[i][j] == "g"):
            Gcount = Gcount + 1
        elif (seqs[i][j] == "C" or seqs[i][j] == "c"):
            Ccount = Ccount + 1
        elif (seqs[i][j] == "T" or seqs[i][j] == "t"):
            Tcount = Tcount + 1
        else:
            GAPcount = GAPcount + 1
    PA = float(Acount)/len(seqs)
    PG = float(Gcount)/len(seqs)
    PC = float(Ccount)/len(seqs)
    PT = float(Tcount)/len(seqs)
    PGAP = float(GAPcount)/len(seqs)
    if PA != 0.0:
        AENT = -1*PA*math.log(PA,2)
    else:
        AENT = 0.0
    if PG != 0.0:
        GENT = -1*PG*math.log(PG,2)
    else:
        GENT = 0.0
    if PC != 0.0:
        CENT = -1*PC*math.log(PC,2)
    else:
        CENT = 0.0
    if PT != 0.0:
        TENT = -1*PT*math.log(PT,2)
    else:
        TENT = 0.0
    if PGAP != 0.0:
        GAPENT = -1*PGAP*math.log(PGAP,2)
    else:
        GAPENT = 0.0
    ShanJ = AENT + GENT + CENT + TENT + GAPENT
    w.write(str(j+1)+"\t"+str(ShanJ)+"\n")
    Shan.append(ShanJ)
    print("Calculating enthropy in position: "+str(j+1)+" Value: "+str(ShanJ))
print("Calculation finished\n")
print("Drawing picture\n")
plot(range(0, len(seqs[0])), Shan, 'r-')
savefig(sys.argv[1]+'.png')
r.close
w.close
show()
