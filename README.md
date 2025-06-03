# 🌿 Evolutionary Tree Analyzer  
*A phylogenetic tree builder for DNA sequence analysis using parsimony and maximum likelihood methods.*

---

## 🔍 Overview  
The Evolutionary Tree Analyzer is a Python-based web app and notebook toolkit designed for **educators, students, and researchers** in bioinformatics and evolutionary biology.

It parses DNA sequences in **FASTA format**, aligns them using **MUSCLE**, and constructs **phylogenetic trees** using both **parsimony** and **maximum likelihood–style** methods. Tree outputs are visualized and exported as `.png` images for teaching, presentations, or research use.

---

## 🎯 Features  
- ✅ Upload and validate DNA FASTA files  
- ✅ Align sequences using **MUSCLE v3.8.31**  
- ✅ Generate phylogenetic trees via:
  - **Parsimony** (UPGMA clustering)
  - **ML-style** (distance-based using identity matrix)  
- ✅ Visualize trees with **Biopython’s Phylo module**  
- ✅ Export `.png` images automatically  
- ✅ Modular, classroom-friendly Python structure  
- ✅ Built for scalability in teaching and student exploration  

---

## 📁 Project Structure


```
evolutionary-tree-analyzer/
│
├── assets/ # Logo and static UI assets
├── data/ # Input FASTA files
│ ├── example_sequences.fasta
│ └── example_large.fa
│
├── notebooks/ # Jupyter notebook version
│ └── tree_builder.ipynb
│
├── output/ # Alignment files and rendered tree images
│ └── tree_images/
│
├── src/ # Core Python logic
│ ├── fasta_parser.py
│ ├── align_sequences.py
│ ├── build_tree.py
│ └── visualize_tree.py
│
├── app.py # Dash web app interface
├── align_manual.bat # Batch file for manual MUSCLE alignment (Windows)
├── requirements.txt # Python dependencies
├── LICENSE # MIT License
└── README.md # You are here!
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
