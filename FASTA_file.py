from Bio import SeqIO

#create a loop to fetch the sequence from the created FASTA file
for record in SeqIO.parse("sample.fasta", "fasta"):

#Fetches the Id of the sequence
    print("ID:", record.id)
#Fetches the sequence 
    print("Sequence:", record.seq)
#Gives the length of the sequence
    print("Length:", len(record.seq))
