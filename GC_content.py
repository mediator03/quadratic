filename = "sequences.txt"
inFile = open(filename, "r")
length_list = []
for lines in inFile:
    lines = lines.rstrip('\n')
    count_C = 0
    count_G = 0
    for G in lines:
        if G == "G":
            count_G = count_G + 1 # calculate number of the "G"s in each line
    for C in lines:
        if C == "C":
            count_C = count_C + 1 # calculate number of the "C"s in each line
    print ((count_G + count_C)/len(lines))
    length_list.append(((count_G + count_C)/len(lines))) # save the GC content for each line to list length_list
print ("Average GC content is:",sum(length_list)/len(length_list))
