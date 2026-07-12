def reverse_complement(sequence): #Defining a function
    complements = {"A":"T","T":"A","G":"C","C":"G"} #Defining complementary bases
    complementary_sequence = ""
    for base in sequence:
        complement = complements[base] #Making complementary sequence
        complementary_sequence += complement #Joning the bases in complementary sequence
    rev_comp = complementary_sequence[::-1] #Reversing the sequence
    return(sequence, complementary_sequence, rev_comp) 
sequence = "ATCGGATCGTACGTGGCCCTTAGTGCTGCT" 
sequence, complementary_sequence, rev_comp = reverse_complement(sequence)
print(f"Original DNA sequence: {sequence}")
print(f"Complementary_sequence: {complementary_sequence}")
print(f"Reverse complement: {rev_comp}")