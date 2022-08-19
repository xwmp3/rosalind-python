# https://rosalind.info/problems/bins/

def load_data(filepath: str) -> (list, list):
    with open(filepath, 'r') as f:
        n = int(f.readline().replace('\n', '').strip())
        m = int(f.readline().replace('\n', '').strip())
        A = [int(item) for item in f.readline().replace('\n', '').strip().split()]
        K = [int(item) for item in f.readline().replace('\n', '').strip().split()]
    return A, K


# https://en.wikipedia.org/wiki/Binary_search_algorithm
# Binary Search
def binary_search(arr, start, end, hkey):
    if start > end:
        return -1
    mid = start + (end - start) // 2
    if arr[mid] > hkey:
        return binary_search(arr, start, mid - 1, hkey)
    if arr[mid] < hkey:
        return binary_search(arr, mid + 1, end, hkey)
    return mid


if __name__ == "__main__":
    inpath = "./datasets/002.bins.txt"
    outpath = "./datasets/002.bins.out"
    A, K = load_data(inpath)
    results = [index + 1 if index != -1 else -1 for index in [binary_search(A, 0, len(A) - 1, k) for k in K]]
    with open(outpath, 'w') as f:
        f.write(' '.join([str(i) for i in results]) + '\n')
    print(f"Save Results to {outpath}")
