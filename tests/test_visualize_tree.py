# tests/test_visualize_tree.py

import os
import sys
from pathlib import Path
import pytest

# Add src/ to path
PROJECT_ROOT = Path(__file__).parent.parent.resolve()
sys.path.insert(0, str(PROJECT_ROOT / "src"))

from src.visualize_tree import visualize_tree
from Bio import Phylo
import tempfile

# Create a trivial Newick string
DUMMY_NEWICK = "(A:0.1,B:0.2);"

@pytest.fixture
def dummy_newick_file(tmp_path):
    f = tmp_path / "tree.newick"
    f.write_text(DUMMY_NEWICK)
    return str(f)

def test_visualize_tree_creates_png(dummy_newick_file, tmp_path):
    out_png = str(tmp_path / "tree.png")
    # Should generate a PNG even for a tiny tree
    visualize_tree(dummy_newick_file, out_png, show_plot=False)
    assert Path(out_png).exists()
    # Optionally, load it with PIL or check file size > 0
    assert Path(out_png).stat().st_size > 0
