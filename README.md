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
- `matplotlib` – optional display for save images
- `subprocess` – run external tools like MUSCLE
- `importlib.util` – dynamic loading of modular scripts

To install all:
```bash
pip install -r requirements.txt
```

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

🧬 Happy tree building!
