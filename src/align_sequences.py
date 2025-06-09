import os, subprocess

def align_sequences(input_fasta, output_fasta):
    """
    Align sequences using MUSCLE and save to output_fasta.
    Automatically uses local ./bin/muscle for Render compatibility.
    """
    # Point to the unzipped binary we just committed
    muscle_path = os.path.join(".", "bin", "muscle")

    if not os.path.isfile(muscle_path):
        raise FileNotFoundError(f"MUSCLE binary not found at {muscle_path}")

    # Warn if huge FASTA
    if os.path.getsize(input_fasta) > 10 * 1024 * 1024:  # 10 MB size check
        print(f"⚠️ Warning: {input_fasta} is large. Consider aligning manually.")
        return

    # Build a list invocation—**no shell=True**
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
        
# for pytest’s test_run_muscle_alignment import…
run_muscle_alignment = align_sequences