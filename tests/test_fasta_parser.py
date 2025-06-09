# tests/test_fasta_parser.py

import os
import sys
import tempfile
from pathlib import Path
import pytest
from Bio import SeqIO

# Add project src to path so imports work
PROJECT_ROOT = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from src.fasta_parser import parse_fasta

def test_parse_valid_fasta(tmp_path):
    # Write a small FASTA file for testing
    fasta_content = """>seq1
ACTGACTGACTG
>seq2
TTGGAACC
"""
    test_file = tmp_path / "sample.fasta"
    test_file.write_text(fasta_content)

    records = list(parse_fasta(str(test_file)))
    # We expect exactly 2 records, with correct sequence lengths:
    assert len(records) == 2
    ids = [rec.id for rec in records]
    assert "seq1" in ids and "seq2" in ids
    # Sequence lengths:
    assert len(records[0].seq) == 12
    assert len(records[1].seq) == 8

def test_parse_empty_fasta(tmp_path):
    empty_file = tmp_path / "empty.fasta"
    empty_file.write_text("")  # no content
    with pytest.raises(ValueError):
        _ = list(parse_fasta(str(empty_file)))
