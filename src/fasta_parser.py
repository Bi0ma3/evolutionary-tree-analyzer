from Bio import SeqIO

def parse_fasta(filepath):
    """
    Parses a FASTA file and returns a list of sequence records.
    """
    records = list(SeqIO.parse(filepath, "fasta"))
    if not records:
        raise ValueError("No sequences found in the FASTA file.")
    return records
