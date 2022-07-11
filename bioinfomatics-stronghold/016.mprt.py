# https://rosalind.info/problems/mprt/

import requests
import os

def load_uniprot_ids(filepath: str):
    ids = []
    with open(filepath, 'r') as f:
        for line in f.readlines():
            data = line.replace('\n', '').strip()
            ids.append(data)
    return ids

def save_prot_seq_from_uniprot(uniprot_id: str, basedir: str):
    url = f"https://rest.uniprot.org/uniprotkb/{uniprot_id}.fasta"
    # print(f"Get Content from [{url}] ...")
    res = requests.get(url)
    if res.status_code != 200:
        return None
    fasta = res.text
    # print(fasta)
    filepath = os.path.join(basedir, f"{uniprot_id}.fasta")
    # print(f"Saved to path: [{filepath}] ...")
    with open(filepath, 'w') as f:
        f.write(fasta)
    return filepath

def load_fasta(filepath: str):
    name_list, seq_list = [], []
    with open(filepath, 'r') as fasta:
        while True:
            line = fasta.readline()
            if not line:
                break
            data = line.replace('\n', '').strip()
            if data.startswith('>'):
                name_list.append(data[1:])
                line = fasta.readline().replace('\n', '').strip()
                seq_list.append(line)
            else:
                seq_list[len(seq_list) - 1] += line.replace('\n', '').strip()
    return name_list, seq_list

def check_motif(t: str):
    return t[0] == 'N' and t[1] != 'P' and (t[2] == 'S' or t[2] == 'T') and t[3] != 'P'

def find_protein_motif_n_gly(s: str):
    pos_list = []
    for i in range(0, len(s) - 4):
        if check_motif(s[i:i+4]):
            pos_list.append(i + 1)
    return pos_list

if __name__ == '__main__':
    path = './datasets/016.mprt.txt'
    uniprot_ids = load_uniprot_ids(path)
    for pid in uniprot_ids:
        fasta_path = save_prot_seq_from_uniprot(uniprot_id=pid.split('_')[0], basedir='./datasets/016.mprt.protseqs')
        if fasta_path == None: 
            print(f"No fasta data for {pid}")
            continue
        prot_seq = load_fasta(fasta_path)[1][0]
        pos_list = find_protein_motif_n_gly(prot_seq)
        if len(pos_list) == 0: 
            continue
        print(f"{pid}\n{' '.join([str(pos) for pos in pos_list])}")