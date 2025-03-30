# This repository is not yet operational. Stay tuned!

# 🌿 Evolutionary Tree Analyzer  
*A phylogenetic tree builder for DNA sequence analysis using parsimony and maximum likelihood methods.*

---

## 🔍 Overview  
The Evolutionary Tree Analyzer is a Python-based tool designed for **educators, students, and researchers** in bioinformatics and evolutionary biology. It parses DNA sequences in **FASTA format**, aligns them, and constructs **phylogenetic trees** using **parsimony** and **maximum likelihood** approaches. It also includes visualizations and method comparisons for educational or analytical use.

---

## 🎯 Features  
- ✅ Upload and validate a FASTA file of DNA sequences  
- ✅ Perform **multiple sequence alignment** using MUSCLE  
- ✅ Build trees using:
  - **Parsimony** (character-based)
  - **Maximum Likelihood** (model-based)
- ✅ Visualize phylogenetic trees using **ete3** or **Plotly**
- ✅ Compare methods side-by-side with annotations
- ✅ (Stretch) Generate PDF/HTML reports
- ✅ (Stretch) Interactive Streamlit app  

---

## 📁 Project Structure

```
evolutionary-tree-analyzer/
│
├── data/                    # Sample FASTA files
│   └── example_sequences.fasta  
│
├── notebooks/               # Jupyter notebooks
│   └── tree_builder.ipynb  
│
├── output/                  # Generated tree images & outputs
│   └── tree_images/
│
├── src/                     # Python modules
│   ├── fasta_parser.py  
│   ├── align_sequences.py  
│   ├── build_tree.py  
│   └── visualize_tree.py  
│
├── requirements.txt         # Python dependencies
├── LICENSE                  # MIT License (or your choice)
└── README.md                # You're reading it!
```

---

## 🚀 Getting Started

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/evolutionary-tree-analyzer.git
cd evolutionary-tree-analyzer
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

**Note**: You must have `MUSCLE` installed and accessible from your system's PATH for alignment.

### 3. Run the main notebook
```bash
jupyter notebook notebooks/tree_builder.ipynb
```

---

## 📦 Dependencies

Core Python libraries used:
- `biopython` – parsing FASTA, alignment tools
- `ete3` – tree visualization
- `matplotlib` / `plotly` – optional visualization
- `subprocess` – run external tools like MUSCLE
- `pandas`, `numpy` – data processing

To install all:
```bash
pip install -r requirements.txt
```

---

## 🧪 Example Use Case

1. Drop your `.fasta` file into the `data/` folder.  
2. Run the notebook or script to:
   - Align sequences
   - Build two trees (parsimony, ML)
   - Visualize them with branch support and leaf labels
   - Compare tree structures and discuss findings  
3. Export results to `output/tree_images/` and (optionally) generate a report.

---

## 🎓 Ideal For

- High school and college biology classrooms  
- Evolution/bioinformatics labs  
- Personal learning and demo projects  
- Teachers Pay Teachers educational bundles  

---

## 🧰 Future Plans

- [ ] Add Streamlit interface  
- [ ] Enable drag-and-drop FASTA upload  
- [ ] Add support for bootstrap analysis  
- [ ] Export PDF/HTML reports  
- [ ] Add tree comparison metrics (e.g., RF distance)

---

## 👩‍💻 Maintainer

**Pipeline Bio** – Simple Bioinformatics for Educators  
🌻 Sunflower logo with a phylogenetic tree  
📫 Contact: biology.mae@gmail.com  
🛒 [Teachers Pay Teachers Store: Pipeline Bio](https://www.teacherspayteachers.com/store/pipeline-bio)  
📌 #teacherspayteachers  

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

🧬 Happy tree building!
