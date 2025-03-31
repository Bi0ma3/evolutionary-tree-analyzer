import subprocess

def align_sequences(input_fasta, output_fasta):
    """
    Align sequences using MUSCLE and save to output_fasta.
    """
    muscle_path = r"C:\Program Files\muscle\muscle.exe"

    subprocess.run(
        [muscle_path, "-align", input_fasta, "-output", output_fasta],
        check=True
    )
    print("Alignment complete.")
