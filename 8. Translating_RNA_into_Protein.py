# Not elegant, can use a module, but wanted to do it from scratch. Probably could and should have used dictionaries, but this solution does function 


def rna_2_prot(seq):

    F = ['UUU','UUC'] # Defining each protein 
    L = ['UUA','UUG','CUU' ,'CUC', 'CUA','CUG']
    S = ['UCC','UCU','UCA','UCG','AGU', 'AGC']
    Y = ['UAU' , 'UAC']
    C = ['UGU' , 'UGC']
    W = ['UGG']
    P = ['CCC','CCU','CCA','CCG']
    H = ['CAU' ,'CAC']
    Q = ['CAA' , 'CAG']
    R = ['CGU' , 'CGC' , 'CGA' , 'CGG' , 'AGA' , 'AGG']
    I = ['AUU' , 'AUC' , 'AUA']
    M = ['AUG']
    T = ['ACU' , 'ACC' , 'ACA' , 'ACG']
    N = ['AAU' , 'AAC']
    K = ['AAA' , 'AAG']
    V = ['GUU' , 'GUC' , 'GUA' , 'GUG'] 
    A = ['GCU' , 'GCC' , 'GCA' , 'GCG']
    D = ['GAU' , 'GAC']
    E = ['GAA' , 'GAG']
    G = ['GGU' , 'GGC' , 'GGA' , 'GGG']
    Stop = ['UAA', 'UAG', 'UGA']
    
    new_list = [] # initiating a list 
    n = 3 
    seq2 = [seq[i:i+n] for i in range(0, len(seq), n)] # Looping over for the length of the sequence
    print(seq2)
    
    for l in seq2:
        
        if l in F:
            new_list.append('F') # Appending the letter for each protein 
        elif l in L:
            new_list.append('L')
        elif l in S:
            new_list.append('S')
        elif l in Y:
            new_list.append('Y')
        elif l in C:
            new_list.append('C')
        elif l in W:
            new_list.append('W')
        elif l in P:
            new_list.append('P')
        elif l in H:
            new_list.append('H')
        elif l in Q:
            new_list.append('Q')
        elif l in R:
            new_list.append('R')
        elif l in I:
            new_list.append('I')
        elif l in M:
            new_list.append('M')
        elif l in T:
            new_list.append('T')
        elif l in N:
            new_list.append('N')
        elif l in K:
            new_list.append('K')
        elif l in V:
            new_list.append('V')
        elif l in A:
            new_list.append('A')
        elif l in D:
            new_list.append('D')
        elif l in E:
            new_list.append('E')
        elif l in G:
            new_list.append('G')
        elif l in Stop:
            new_list.append('Stop') # Wasn't 100% sure of what they wanted from the stop codons
    print(*new_list, sep = '')
    
rna_2_prot('')
