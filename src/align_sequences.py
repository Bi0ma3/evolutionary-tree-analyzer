import os
import subprocess

def align_sequences(input_fasta, output_fasta):
    """
    Align sequences using MUSCLE and save to output_fasta.
    Automatically warns if file is too large.
    """
    muscle_path = r"C:\Program Files\muscle\muscle.exe"
    
    # Warn about large input files
    if os.path.getsize(input_fasta) > 10 * 1024 * 1024:  # 10MB+
        print(f"⚠️ Warning: {input_fasta} is large. Consider aligning manually.")
        return
    
    command = f'"{muscle_path}" -align "{input_fasta}" -output "{output_fasta}"'
    try:
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            capture_output=True,
            text=True
        )
        print("✅ Alignment complete.")
    except subprocess.CalledProcessError as e:
        print("❌ Alignment failed.")
        print("STDOUT:\n", e.stdout)
        print("STDERR:\n", e.stderr)
