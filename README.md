# This repository is not yet operational. Say tuned!

# evolutionary-tree-analyzer
A tool to build, visualize, and compare phylogenetic trees from DNA sequences.

## Features
- Upload a FASTA file
- Perform multiple sequence alignment
- Build phylogenetic trees using:
  - Parsimony
  - Maximum Likelihood
- Visualize and compare tree outputs
- Output annotated trees and summary recommendations

## Folder Structure
evolutionary-tree-analyzer/
│
├── data/
│   └── example_sequences.fasta         # Sample FASTA file (placeholder)
│
├── notebooks/
│   └── tree_builder.ipynb              # Jupyter notebook for running the full pipeline
│
├── output/
│   └── tree_images/                    # Auto-saved tree visualizations
│
├── src/
│   ├── fasta_parser.py                 # Load and validate FASTA files
│   ├── align_sequences.py              # Sequence alignment functions
│   ├── build_tree.py                   # Tree construction functions
│   └── visualize_tree.py               # Tree visualization functions
│
├── README.md                           # Project overview
├── requirements.txt                    # Dependencies list
└── LICENSE                             # Optional open-source license

