import os
import shutil
import subprocess

def align_sequences(input_fasta, output_fasta):
    """
    Align sequences using MUSCLE and save to output_fasta.
    Automatically detects MUSCLE path for portability.
    """
    muscle_path = shutil.which("muscle")

    if not muscle_path:
        raise FileNotFoundError("MUSCLE executable not found in system PATH. Make sure it is installed.")

    if os.path.getsize(input_fasta) > 10 * 1024 * 1024:  # 10MB
        print(f"⚠️ Warning: {input_fasta} is large. Consider aligning manually.")
        return

    command = [muscle_path, "-align", input_fasta, "-output", output_fasta]

    try:
        result = subprocess.run(
            command,
            check=True,
            capture_output=True,
            text=True
        )
        print("✅ Alignment complete.")
    except subprocess.CalledProcessError as e:
        print("❌ Alignment failed.")
        print("STDOUT:\n", e.stdout)
        print("STDERR:\n", e.stderr)
