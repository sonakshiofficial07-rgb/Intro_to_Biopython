#Taking DNA sequence input from user
dna = input('ENTER THE DNA SEQUENCE:").upper()

#Counting each content seperataly 
a = dna.count("A")
t = dna.count("T")
g = dna.count("G")
c = dna.count("C")

#Printing each sequence and their count
print("A = ", a)
print("T = ", t)
print("G = ", g)
print("C = ", c) 
