from Bio import AlignIO
from Bio.Phylo.TreeConstruction import DistanceCalculator, DistanceTreeConstructor
from Bio import Phylo

def build_parsimony_tree(aligned_fasta, output_newick="output/parsimony_tree.newick"):
    """
    Build a simple tree using distance-based approximation to parsimony.
    Saves the tree in Newick format.
    """
    # Step 1: Read the aligned sequences
    alignment = AlignIO.read(aligned_fasta, "fasta")
    
    # Step 2: Create a distance matrix (e.g., using identity)
    calculator = DistanceCalculator("identity")  # or use "blosum62" for proteins
    distance_matrix = calculator.get_distance(alignment)

    # Step 3: Construct a tree using  NJ (approximation of parsimony)
    constructor = DistanceTreeConstructor()
    tree = constructor.nj(distance_matrix)  

    # Step 4: Save the tree to file in Newick format
    Phylo.write(tree, output_newick, "newick")
    print(f"Parsimony-like tree saved to: {output_newick}")

def build_likelihood_tree(aligned_fasta, output_newick="output/ml_tree.newick"):
    """
    Builds a simple ML-like tree (UPGMA using identity) and saves it in Newick format.
    """
    alignment = AlignIO.read(aligned_fasta, "fasta")
    calculator = DistanceCalculator("identity")
    distance_matrix = calculator.get_distance(alignment)

    constructor = DistanceTreeConstructor()
    tree = constructor.upgma(distance_matrix)

    Phylo.write(tree, output_newick, "newick")
    print(f"Likelihood-like tree saved to: {output_newick}")
