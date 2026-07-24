from Bio import SeqIO
record = SeqIO.read("blaTEM_sequence.fasta", "fasta") #Read the fasta file
sequence = record.seq  #Extract the DNA equence
reverse = sequence.reverse_complement() #Generate the reverse complement

print(f"Sequence ID: {record.id}")
print(f"Description: {record.description}")
print(f"Original Sequence: {sequence}")
print(f"Reverse Complement: {reverse}")