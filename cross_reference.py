#Here you will extract and print the data from init_sites.txt that corresponds to genes with high expression. There isn't gene expression data in init_sites.txt, so we'll have to integrate information from another file.

#    First, use gene_expr.txt to create a list of genes with high expression. We'll say high expression is anything >= 50.
#    Then read through init_sites.txt and print the GeneName (2nd column) and PeakScore (11th column) from any line that matches an ID in your high-expression list.
#    Finally, separately compute the average PeakScore for high expression genes and non-high expression genes. Print both averages to the screen.
#[ Check your answer ] There should be 10 lines corresponding to high-expression genes that you print info about. Your average peak scores should be 4.371 and 4.39325 for high and non-high expression genes, respectively.
#My solution uses dictionary, probably not the most effecient one.
expression_filename = "gene_expr.txt"
expression = open(expression_filename, "r")
expression = expression.readlines()[1:]
gene_list_high = []
gene_list_low = []
for lines in expression: 
    lines = lines.rstrip('\n')
    data = lines.split()
    x = dict(zip([data[1]], [data[0]]))
    for expression, gene_name in x.items():
        if int(expression) >= 50:
            #print (gene_name)
            gene_list_high.append(str(gene_name)) # Save the high genes to a list
        elif int(expression) < 50:
            #print (gene_name)
            gene_list_low.append(str(gene_name)) # Save the low genes to a list
gene_expression_high = []
gene_expression_low = []
filename = "init_sites.txt"
inFile = open(filename, "r")
inFile = inFile.readlines()[1:]
for lines in inFile: 
    lines = lines.rstrip('\n')
    data = lines.split()
    gene_name = data[0]
    PeakScore = data[10]
    y = dict(zip([str(gene_name)], [PeakScore])) # Create a dictionary where key is gene name and value is peak score. 
    for key, high_value in y.items():
        if key in gene_list_high: # Find the matching value(paek score) for key, where the key is the list of highly expressed gene.
            gene_expression_high.append(high_value)
            gene_expression_high = [float(i) for i in gene_expression_high]
        if key in gene_list_low:
            gene_expression_low.append(high_value)
            gene_expression_low = [float(i) for i in gene_expression_low]    
print ("The average peak score for highly expressed genes is:", sum(gene_expression_high)/len(gene_expression_high))
print ("The average peak score for lowly expressed genes is:",sum(gene_expression_low)/len(gene_expression_low))
