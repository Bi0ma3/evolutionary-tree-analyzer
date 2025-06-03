import os
import subprocess
import shutil

def align_sequences(input_fasta, output_fasta):
    """
    Align sequences using MUSCLE and save to output_fasta.
    Automatically warns if file is too large.
    """

    # Detect MUSCLE path dynamically
    muscle_path = shutil.which("muscle")
    if not muscle_path:
        raise FileNotFoundError("MUSCLE executable not found in PATH. "
                                "Make sure MUSCLE is installed and added to your system PATH.")

    # Warn about large input files
    if os.path.getsize(input_fasta) > 10 * 1024 * 1024:  # 10MB+
        print(f"⚠️ Warning: {input_fasta} is large. Consider aligning manually.")
        return

    # Build MUSCLE command
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
