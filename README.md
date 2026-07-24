# DNA_Reverse_Complement_Generator

## Problem Statement

Generating the reverse complement of a DNA sequence is a foundational step
in molecular biology and bioinformatics workflows used, for example, in
primer design and sequence alignment. This tool calculates the reverse
complement of a real antimicrobial resistance gene, implemented both from
scratch and using an established bioinformatics library, to demonstrate
the underlying logic as well as standard practice.

## What This Tool Does

Given a DNA sequence from a FASTA file, the tool returns its reverse
complement, the sequence that would pair with the original strand,
read in the opposite direction (5' to 3').

Two implementations are included:

| File | Description |
|---|---|
| `Reverse_Complement_Manual.py` | Builds the complement using a manual base-pairing map (A↔T, G↔C), then reverses it, written from scratch to demonstrate understanding of the underlying logic. |
| `Reverse_Complement_Biopython.py` | Uses [Biopython](https://biopython.org/)'s built-in `Seq.reverse_complement()` method, reflecting standard bioinformatics practice. |

Both files are kept separate intentionally, so each can be read and
evaluated independently.

## Example Data

- **Gene used:** *blaTEM* (TEM family beta-lactamase), *Salmonella Typhi*
- **Source:** NCBI GenBank, accession [MW805241](https://www.ncbi.nlm.nih.gov/nuccore/MW805241)
- **Relevance:** *blaTEM* confers resistance to β-lactam antibiotics connected to my Master's thesis research on antimicrobial resistance in
  *Salmonella typhi*.
- Note: this is a **partial cds** sequence, which does not affect reverse
  complement calculation.

## Requirements

- Python 3.x
- Biopython (`pip install biopython`) required only for
  `Reverse_Complement_Biopython.py`

## Usage

```bash
python Reverse_Romplement_Manual.py
python Reverse_Complement_Biopython.py
```

(Each script reads `blaTEM_sequence.fasta` directly, make sure it's in the same
folder as the script.)

## Sample Output

Running `Reverse_Complement_Biopython.py` on the *blaTEM* sequence produces:

```
Sequence ID: MW805241.1
Description: MW805241.1 Salmonella enterica subsp. enterica serovar Typhi strain InMoAh-5 TEM family beta-lactamase (blaTEM) gene, partial cds
Original Sequence: CGTTTTCCAATGATGAGCACTTTTAAAGTTCTGCTATGTGGTGCGGTATTATCCCGTGTTGACGCC...
Reverse Complement: GATAACTACGATACGGGAGGGCTTACCATCTGGCCCCAGTGCTGCAATGATACCGCGAGACCCACG...
```

*(Sequence truncated above for readability; full output is produced when
running the script.)*

The manual version (`Reverse_Complement_Manual.py`) produces the same
reverse complement result, since both implementations apply the same
underlying base-pairing logic.

## How It Works

- **Manual version:** Maps each base to its complement (A→T, T→A, G→C,
  C→G) using a dictionary, builds the complementary strand, then reverses
  it to produce the final reverse complement.
- **Biopython version:** Parses the FASTA file with `SeqIO.read()` and
  calls `.reverse_complement()` on the resulting `Seq` object.