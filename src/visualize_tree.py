from ete3 import Tree, TreeStyle

def visualize_tree(newick_file):
    """
    Visualize a tree from a Newick file.
    """
    t = Tree(newick_file)
    ts = TreeStyle()
    ts.show_leaf_name = True
    t.show(tree_style=ts)
