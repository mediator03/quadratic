# convert the sequences in sequences.txt into reverse complement
filename = "sequences.txt"
inFile = open(filename, "r")
complement = {'A':'T','G':'C','T':'A','C':'G'}
#print (complement.keys())
for lines in inFile:
    lines = lines.rstrip('\n') # read in sequence
    lines_reverse = lines[::-1] # for each line of sequences, reverse the sequence
    print ("".join([complement[base] for base in lines_reverse])) # use dictionation complement{} to replace the nucleotide 
