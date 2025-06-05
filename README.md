# 🌿 SimplePhylo  
*A phylogenetic tree builder for DNA sequence analysis using parsimony and maximum likelihood methods.*

---

## 📋 Table of Contents
1. [Overview](#overview)  
2. [🚀 Quick Start](#quick-start)  
3. [📁 Project Structure](#project-structure)  
4. [📦 Dependencies](#dependencies)  
5. [⚙️ MUSCLE Alignment Notes](#muscle-alignment-notes)  
6. [🧪 Example Workflow](#example-workflow)  
7. [🎓 Ideal For](#ideal-for)  
8. [📅 Future Plans](#future-plans)  
9. [🧰 Maintainer](#maintainer)  
10. [📄 License](#license)  
11. [📜 Citations & Attributions](#citations--attributions)

---

## 🧐 Overview  
**SimplePhylo** is a Python-based web app (built with Dash) and a companion Jupyter notebook toolkit for educators, students, and researchers in bioinformatics and evolutionary biology.

It enables you to:
- Parse DNA sequences in **FASTA** format.  
- Align them using **MUSCLE v3.8.31**.  
- Build phylogenetic trees via both **Parsimony** (UPGMA) and **ML-style** (distance-based on identity).  
- Visualize and export tree images as `.png` for teaching slides, lab reports, or research.  

Whether you’re running a quick classroom demo or prototyping a research pipeline, SimplePhylo keeps everything modular and accessible.

---

## 🚀 Quick Start

### 1. Clone this repository
```bash
git clone https://github.com/yourusername/evolutionary-tree-analyzer.git
cd evolutionary-tree-analyzer
---

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### ⚙️ MUSCLE Alignment Notes

This project uses [MUSCLE](https://drive5.com/muscle/downloads_v3.htm) v3.8.31 to align DNA sequences.

- For small files, alignment runs automatically in Python
- For large files, use the batch script: align_manual.bat

#### You must have `MUSCLE` installed and accessible from your system's PATH for alignment.
💡 Ensure the muscle.exe binary is placed in:
C:\Program Files\muscle\muscle.exe
Or edit the .bat file to reflect the correct path.

MUSCLE citation:
Edgar, R.C. (2004) Nucleic Acids Res 32(5):1792–1797. http://www.drive5.com/muscle

✨Please cite this work if you use the alignment functionality in your research or publications.

### 3. Launch the App (Web Interface)
```bash
python app.py 
```
Alternatively, you can run notebooks/tree_builder.ipynb in Jupyter Notebook.
---

## 📁 Project Structure

```
evolutionary-tree-analyzer/
│
├── assets/                  # Logo and static UI assets
│   ├── PB_logo_noback_solid.png
│   └── PB_logo_watermark.png
│
├── data/                    # Input FASTA files
│   ├── example_large.fa
│   └── example_smaller.fa
│
├── notebooks/               # Jupyter notebook version
│   └── tree_builder.ipynb
│
├── output/                  # Alignment files and rendered tree images
│   └── tree_images/
│       ├── parsimony_tree.png
│       └── ml_tree.png
│
├── src/                     # Core Python logic (library modules)
│   ├── fasta_parser.py      # Parse FASTA → SeqIO records
│   ├── align_sequences.py   # Run MUSCLE alignment
│   ├── build_tree.py        # Build parsimony & ML-style trees
│   └── visualize_tree.py    # Render trees to PNG via Biopython Phylo
│
├── app.py                   # Dash web-app entrypoint (layout + callbacks)
├── align_manual.bat         # Windows batch script for manual MUSCLE alignment
├── requirements.txt         # All Python dependencies
├── LICENSE                  # MIT License (see below)
└── README.md                # You are here!

```

## 📦 Dependencies

Core Python libraries used:
- `biopython` – parsing FASTA, alignment tools
- `matplotlib` – optional display for save images
- `subprocess` – run external tools like MUSCLE
- `importlib.util` – dynamic loading of modular scripts
- `dash` + `dash-bootstrap-components` – dashboard
- `tkinter` – for local image rendering in the notebook

---

## 🧠 Tips for Large Input Files
   - Use smaller test files to debug your workflow
   - Trim sequences or split large FASTA files into smaller sets
   - Avoid running MUSCLE v5 inside Python if memory use exceeds ~16GB

---

## 🧪 Example Workflow
1. Drop your .fasta file into the data/ folder
2. Launch the app or notebook
3. You’ll get:
  - A multiple sequence alignment (FASTA)
  - Two phylogenetic trees (Parsimony & ML-style)
  - PNG files saved in output/tree_images/

Perfect for:
🧬 Biology class demonstrations
🧪 Research prototyping
📚 Curriculum development
💡 Student-led investigations

---

## 🎓 Ideal For
- High school biology & AP Bio courses
- Undergraduate bioinformatics/evolution units
- Curriculum writers and lab instructors
- Pipeline Bio resources  

---

## 🧰 Future Plans
  
- [ ] Add support for bootstrap analysis  
- [ ] Export PDF/HTML reports  
- [ ] Add tree comparison metrics (e.g., RF distance)
Want to see SimplePhylo improved? I welcome all feedback and I can't wait to hear from you!

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

## 🧾 Citations & Attributions

This project uses the MUSCLE alignment tool developed by Robert C. Edgar.

> Edgar, R.C. (2004) MUSCLE: multiple sequence alignment with high accuracy and high throughput. *Nucleic Acids Research*, 32(5):1792–1797.  
> [http://www.drive5.com/muscle](http://www.drive5.com/muscle)

Please cite this work if you use the alignment functionality in your research or publications.

---

🧬 Happy tree building!
© 2025 Mae Warner (Pipeline Bio). All rights reserved.
