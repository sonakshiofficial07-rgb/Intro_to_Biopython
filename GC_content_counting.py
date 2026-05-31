#Taking dna sequence input from user
dna = input("Enter DNA sequence: ").upper()

#Counting guanine and cytosine content form the whole dna sequence
g = dna.count("G")
c = dna.count("C")

#Calculating the gc content 
gc_content = ((g + c) / len(dna)) * 100

#Printing the answer
print("GC Content:", gc_content, "%")
