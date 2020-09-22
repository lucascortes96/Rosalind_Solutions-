## Again, this one was a little bit tough for me, 
## Had to comput the GC content of each string and then return the string with the highest GC content
 

import operator 

def returnHighGC(fastaName):
    def read_fasta(fp): # This section just reads in the file and stores the IDs and the sequences
        name = None
        seq = []
        for line in fp:
            line = line.rstrip()
            if line.startswith('>'):
                if name: yield (name, ''.join(seq))
                name = line
                seq = []
            else:
                seq.append(line)
        if name: yield (name, ''.join(seq))
    genes = {}
    with open(fastaName) as fp:
        for name, seq in read_fasta(fp):
            
            genes[name] = seq
    gene_gcs = {}
    for gene in genes: #Getting the count of G's and C's for each gene
        geneLength = len(genes[gene])
        gORc = genes[gene].count('G') + genes[gene].count('C')
        percentage = (gORc / geneLength) * 100 # Calculating the percentage content
        gene_gcs[gene] = percentage
    
    sortedByGC = sorted(gene_gcs.items(), key=operator.itemgetter(1), reverse = True) # Sorting by largest % content
    return(sortedByGC[0])

returnHighGC('rosalind_gc1.txt')
