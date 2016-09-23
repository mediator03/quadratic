#Generate random number of nucleotides.
def rand_seq(a):
    import numpy
    from numpy import random
    nt = ["A","T","G","C"]
    return ''.join(numpy.random.choice(nt,x))
x = 50 #Number of nucleotides per line.
for i in range(20): #Number of lines.
    rand_seq(x)
    print (rand_seq(x))
