from Bio import Phylo
import matplotlib.pyplot as plt

def visualize_tree(newick_file, show_plot=True, save_path=None):
    """
    Visualizes a phylogenetic tree from a Newick file.

    Parameters:
    - newick_file (str): Path to the Newick file.
    - show_plot (bool): If True, displays the tree.
    - save_path (str or None): If provided, saves the figure to this path.
    """
    tree = Phylo.read(newick_file, "newick")
    fig = plt.figure(figsize=(10, 6))
    axes = fig.add_subplot(1, 1, 1)
    Phylo.draw(tree, do_show=False, axes=axes)
    plt.title("Phylogenetic Tree")
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path)
        print(f"Tree image saved to: {save_path}")

    if show_plot:
        plt.show()
