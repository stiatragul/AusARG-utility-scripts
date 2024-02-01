# For renaming tips if there's a lot of correction. Just need to supply csv with columns: old, new

import sys

def replace_text(old_vs_new_file, tree_file, output_file):
    # Read old vs replacements from the CSV file into a dictionary
    old_vs_new = {}
    with open(old_vs_new_file, 'r') as f:
        for line in f:
            old, new = line.strip().split(',')
            old_vs_new[old] = new

    # Read the Newick tree file
    with open(tree_file, 'r') as f:
        newick_tree = f.read()

    # Replace old text with replacements
    for old, new in old_vs_new.items():
        newick_tree = newick_tree.replace(old, new)

    # Write the modified Newick tree to a new file
    with open(output_file, 'w') as f:
        f.write(newick_tree)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python rename_tips_stree.py old_vs_new.csv tree.tree modified_tree.tree")
        sys.exit(1)
    
    old_vs_new_file = sys.argv[1]
    tree_file = sys.argv[2]
    output_file = sys.argv[3]

    replace_text(old_vs_new_file, tree_file, output_file)
