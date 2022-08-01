# https://rosalind.info/problems/long/

from data import load_fasta

# https://noobest.medium.com/rosalind-genome-assembly-as-shortest-superstring-1db2c7408a64
def get_superstring(reads_list, superstring=''):
    if len(reads_list) == 0:
        return superstring

    elif len(superstring) == 0:
        superstring = reads_list.pop(0)
        return get_superstring(reads_list, superstring)

    else:
        for current_read_index in range(len(reads_list)):
            current_read = reads_list[current_read_index]
            current_read_length = len(current_read)

            for trial in range(current_read_length // 2):
                overlap_length = current_read_length - trial

                if superstring.startswith(current_read[trial:]):
                    reads_list.pop(current_read_index)
                    return get_superstring(reads_list, current_read[:trial] + superstring)

                if superstring.endswith(current_read[:overlap_length]):
                    reads_list.pop(current_read_index)
                    return get_superstring(reads_list, superstring + current_read[overlap_length:])
    
if __name__ == '__main__':
    inpath = "./datasets/025.long.txt"
    outpath = "./datasets/025.long.out"
    seqs = load_fasta(inpath)[1]
    super_string = get_superstring(seqs)
    with open(outpath, 'w') as f:
        f.write(f"{super_string}\n")
    print(f"Save Results to {outpath}")