# tests/test_align_sequences.py

import os
import sys
import tempfile
import pytest
import platform
from pathlib import Path

# Ensure the src/ folder is on sys.path
PROJECT_ROOT = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from src.align_sequences import align_sequences as run_muscle_alignment

@pytest.mark.skipif(
    (platform.system() == "Windows")             # don’t even try on Windows
    or not Path("bin/muscle").exists(),          # or if no muscle binary present
    reason="MUSCLE binary not available or not compatible; skipping alignment test."
)

def test_run_muscle_alignment(tmp_path):
    # Create a small multi‐fasta file
    fasta_content = """>seqA
ACTGACTG
>seqB
ACTGACTG
"""
    input_fasta = tmp_path / "input.fa"
    output_fasta = tmp_path / "aligned.fa"
    input_fasta.write_text(fasta_content)

    # This function should call the muscle binary and produce aligned output
    run_muscle_alignment(str(input_fasta), str(output_fasta))
    assert output_fasta.exists()
    aligned = output_fasta.read_text()
    # The aligned file should start with a ">" and have sequences
    assert aligned.startswith(">")
