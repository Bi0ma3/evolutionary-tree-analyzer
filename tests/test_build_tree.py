# tests/test_build_tree.py

import os
import sys
import tempfile
from pathlib import Path
import pytest

# Add src/ to path
PROJECT_ROOT = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from src.build_tree import build_parsimony_tree, build_likelihood_tree

# Create a minimal dummy alignment file for testing
DUMMY_ALIGNMENT = """>A
ACTG
>B
ACTG
"""

@pytest.fixture
def dummy_alignment(tmp_path):
    f = tmp_path / "dummy_aligned.fa"
    f.write_text(DUMMY_ALIGNMENT)
    return str(f)

def test_build_parsimony_tree(dummy_alignment, tmp_path):
    output_newick = str(tmp_path / "parsimony_test.newick")
    # Should not raise errors on two identical sequences
    build_parsimony_tree(dummy_alignment, output_newick)
    assert Path(output_newick).exists()
    newick_str = Path(output_newick).read_text().strip()
    # Check that it ends with a semicolon (valid Newick format)
    assert newick_str.endswith(";")

def test_build_likelihood_tree(dummy_alignment, tmp_path):
    output_newick = str(tmp_path / "ml_test.newick")
    build_likelihood_tree(dummy_alignment, output_newick)
    assert Path(output_newick).exists()
    # likewise check formatting
    assert Path(output_newick).read_text().strip().endswith(";")
