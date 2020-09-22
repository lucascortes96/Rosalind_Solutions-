## Have to replace each 'T' in the original sequence to a 'U'
## Simplest solution is to use the replace function in python


def transcribeDNA(seq):
    seq = seq.replace("T","U")
    return seq
transcribeDNA('sequence')
