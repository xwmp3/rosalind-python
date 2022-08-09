# https://rosalind.info/problems/deg/

# Degree Array

from utils import load_edge_list, degree_array

if __name__ == "__main__":
    inpath = "./datasets/003.deg.txt"
    outpath = "./datasets/003.deg.out"
    nodes, edges = load_edge_list(inpath)
    results = degree_array(nodes, edges)
    with open(outpath, 'w') as f:
        outstr = ' '.join([str(item) for item in results])
        print(outstr)
        f.write(outstr + '\n')
    print(f"Save Results to {outpath}")
