## Have to print out the number of 'A' 'T' 'C' and 'G' separated by a space
# Relatively simple, just printed the count of each line

f = open("filename", 'r')
seq = f.readline().rstrip()
f.close()

print(seq.count("A")),
print(seq.count("C")),
print(seq.count("G")),
print(seq.count("T")))
