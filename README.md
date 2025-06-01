# 🌿 Evolutionary Tree Analyzer  
*A phylogenetic tree builder for DNA sequence analysis using parsimony and maximum likelihood methods.*

---

## 🔍 Overview  
The Evolutionary Tree Analyzer is a Python-based pipeline designed for **educators, students, and researchers** in bioinformatics and evolutionary biology. It parses DNA sequences in **FASTA format**, aligns them using MUSCLE, and constructs **phylogenetic trees** using both **parsimony** and **maximum likelihood–style** methods. Output trees are visualized and saved as images for classroom or research use.

---

## 🎯 Features  
- ✅ Upload and validate a FASTA file of DNA sequences  
- ✅ Align sequences using **MUSCLE**  
- ✅ Build phylogenetic trees using:
  - **Parsimony** (character-based method)
  - **Maximum Likelihood–style** (distance-based UPGMA using identity matrix)  
- ✅ Visualize trees using **Biopython’s Phylo module**  
- ✅ Automatically export `.png` tree images  
- ✅ Modular, readable Python code for students and instructors  
- ✅ Built to scale in classroom settings

---

## 📁 Project Structure

```
evolutionary-tree-analyzer/
│
├── data/                    # Sample FASTA files
│   └── example_sequences.fasta  
│   └── example_large.fa  
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

### ⚙️ MUSCLE Alignment Notes

This project uses [MUSCLE](https://drive5.com/muscle/downloads_v3.htm) v3.8.31 to align DNA sequences.

- For small files, alignment runs automatically in Python
- For large files, use the included batch file to run MUSCLE manually from the command line.

#### You must have `MUSCLE` installed and accessible from your system's PATH for alignment.

MUSCLE citation:
Edgar, R.C. (2004) Nucleic Acids Res 32(5):1792–1797. http://www.drive5.com/muscle

✨Please cite this work if you use the alignment functionality in your research or publications.

### 3. Run the main notebook
```bash
jupyter notebook notebooks/tree_builder.ipynb
```

---

## 📦 Dependencies

Core Python libraries used:
- `biopython` – parsing FASTA, alignment tools
- `matplotlib` – optional display for save images
- `subprocess` – run external tools like MUSCLE
- `importlib.util` – dynamic loading of modular scripts

To install all:
```bash
pip install -r requirements.txt
```


✅ Recommended Setup (Manual MUSCLE Alignment)
1. Download MUSCLE v5.3 for Windows
→ From the official site:
https://drive5.com/muscle/downloads.htm

2. Place the downloaded executable here (or adjust the path in your code):
C:\Program Files\muscle\muscle.exe

3. If alignment crashes inside the notebook, use the fallback batch file:
Run this from Git Bash or Command Prompt:
align_manual.bat

This will:
   - Align your FASTA file
   - Save the result to:
      output/aligned_sequences.fasta

4. Then reopen the notebook and skip the alignment step.
Go directly to tree construction.

🧠 Tips for Large Input Files
   - Use smaller test files to debug your workflow
   - Trim sequences or split large FASTA files into smaller sets
   - Avoid running MUSCLE v5 inside Python if memory use exceeds ~16GB

---

## 🧪 Example Use Case

1. Drop your `.fasta` file into the `data/` folder.  
2. Run 'notebooks/tree_builder.ipynb'
3. The notebook will:
   - Align sequences using MUSCLE
   - Build two trees (parsimony, ML)
   - Render and safe images to `output/tree_images/`
Perfect for:
   - Classroom demos
   - Independent student exploration
   - Curriculum development

---

## 🎓 Ideal For

- High school and college biology classrooms  
- Evolution/bioinformatics labs  
- Personal learning and demo projects  
- Supplementing Teachers Pay Teachers Pipeline Bio Curriculum   

---

## 🧰 Future Plans

- [ ] Interactive Streamlit UI 
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

## 🧾 Citations & Attributions

This project uses the MUSCLE alignment tool developed by Robert C. Edgar.

> Edgar, R.C. (2004) MUSCLE: multiple sequence alignment with high accuracy and high throughput. *Nucleic Acids Research*, 32(5):1792–1797.  
> [http://www.drive5.com/muscle](http://www.drive5.com/muscle)

Please cite this work if you use the alignment functionality in your research or publications.

---

🧬 Happy tree building!
