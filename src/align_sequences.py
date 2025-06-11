import os, subprocess

def align_sequences(input_fasta: str, output_fasta: str):
    muscle_path = os.path.join("bin", "muscle")
    if not os.path.isfile(muscle_path):
        raise FileNotFoundError(f"MUSCLE binary not found at {muscle_path}")

    # skip if huge
    if os.path.getsize(input_fasta) > 10 * 1024 * 1024:
        print(f"⚠️ Warning: {input_fasta} is large. Consider aligning manually.")
        return

    # CORRECT flags: -in / -out
    command = [muscle_path,
               "-in",  input_fasta,
               "-out", output_fasta]

    try:
        result = subprocess.run(
            command,
            check=True,
            capture_output=True,
            text=True,
        )
        print("✅ Alignment complete.")
    except subprocess.CalledProcessError as e:
        print("❌ Alignment failed.")
        print("STDOUT:\n", e.stdout)
        print("STDERR:\n", e.stderr)
        
