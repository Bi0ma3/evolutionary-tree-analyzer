from Bio import Phylo
import matplotlib.pyplot as plt

def visualize_tree(newick_file, save_path=None, show_plot=False):
    """
    Visualizes a phylogenetic tree from a Newick file.

    Parameters:
    - newick_file (str): Path to the Newick file.
    - save_path (str or None): If provided, saves the figure to this path.
    - show_plot (bool): If True, displays the tree (for local testing only).
    """
    tree = Phylo.read(newick_file, "newick")
    fig = plt.figure(figsize=(10, 6))
    ax = fig.add_subplot(1, 1, 1)
    Phylo.draw(tree, do_show=False, axes=ax)
    plt.title("Phylogenetic Tree")
    plt.tight_layout()

    if save_path:
        plt.savefig(save_path)
        print(f"Tree image saved to: {save_path}")

    if show_plot:
        plt.show()

    plt.close()

