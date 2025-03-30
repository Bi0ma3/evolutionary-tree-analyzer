from Bio.Align.Applications import MuscleCommandline
import subprocess

def align_sequences(input_fasta, output_fasta):
    """
    Align sequences using MUSCLE and save to output_fasta.
    """
    muscle_cline = MuscleCommandline(input=input_fasta, out=output_fasta)
    subprocess.run(str(muscle_cline), shell=True, check=True)
