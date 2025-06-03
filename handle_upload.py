import base64
from io import StringIO
from Bio import SeqIO
import os
import subprocess

def parse_uploaded_fasta(contents):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string).decode('utf-8')
    fasta_io = StringIO(decoded)
    records = list(SeqIO.parse(fasta_io, "fasta"))
    return records

def save_fasta_and_align(contents):
    # Decode and save uploaded FASTA
    content_string = contents.split(",")[1]
    decoded = base64.b64decode(content_string)
    
    input_path = os.path.abspath("data/uploaded_input.fa")
    output_path = os.path.abspath("output/aligned_sequences.fasta")
    
    with open(input_path, "wb") as f:
        f.write(decoded)

    # Run MUSCLE 
    muscle_path = os.path.join(".", "bin", "muscle")
    cmd = [muscle_path, "-in", input_path, "-out", output_path]

    try:
        subprocess.run(cmd, check=True)
        return f"✅ Alignment complete! Saved to {output_path}"
    except subprocess.CalledProcessError as e:
        return f"⚠️ Alignment failed: {e}"
