## Decided to go back and play around with dictionaries on this one


sequence = ''
answer = []
# A dictionary linking each current nucleotide to its compliment 
complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}

# Looping over each nucleotide appending to the empty answer list
for nucleotide in sequence:
    answer.append(complement[nucleotide])

# Making sure the answer is reveresed
print ''.join(answer[::-1])
