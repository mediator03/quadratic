#Takes five arguments, generate fake fasta files
#Useage: python fakeFastaGenerator.py outputFasta.txt a b c
#a:number of sequence to generate
#b:minimum length of the sequence
#c:maximum length of the sequence
import sys
import random as rd
def rand_seq(a):
    import numpy
    from numpy import random
    nt = ["A","T","G","C"]
    return ''.join(numpy.random.choice(nt,a))
if len(sys.argv) == 5:
    outFile = str(sys.argv[1])
    numSeqs = int(sys.argv[2])
    minLength = int(sys.argv[3])
    maxLength = int(sys.argv[4])
else:
    print("You must provide four arguments")
    sys.exit()
outFile1 = open(outFile, 'w')
count = 0
while count <= numSeqs:
    for i in range(numSeqs):
        count += 1
        a = rd.randint(minLength,maxLength)
        x = ">seq"+str(count)+"\n"+rand_seq(a)+"\n"
        outFile1.write(x)
outFile1.close()
