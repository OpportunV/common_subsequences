import numpy as np
from skimage.feature import peak_local_max


def cns(seq1, seq2):
    """returns ss - list of (x1, x2, y1, y2) such as seq1[x1:x2] == seq2[y1:y2]"""
    if not isinstance(seq1, (str, tuple, set, list)) or not isinstance(seq2, (str, tuple, set, list)):
        return None
    
    ss = []
    n, m = len(seq1), len(seq2)
    
    table = np.zeros((n, m), dtype=int)
    table[0, :] = np.array([int(i == seq1[0]) for i in seq2])
    table[:, 0] = np.array([int(i == seq2[0]) for i in seq1])
    
    for i in range(1, n):
        for j in range(1, m):
            table[i, j] = table[i - 1, j - 1] + 1 if seq1[i] == seq2[j] else 0
    
    tmp = np.flip(peak_local_max(table, exclude_border=False), axis=0)
    for x, y in tmp:
        if (seq_len:=table[x, y]) > 1:
            ss.append((x - seq_len + 1, x + 1, y - seq_len + 1, y + 1))
    
    return ss


def main():
    a = 'abragakedabra'
    b = 'ragaabdabra'
    ss = cns(a, b)
	
    for x1, x2, y1, y2 in ss:
        print(f'{a[x1:x2]=}, {b[y1:y2]=}')


if __name__ == '__main__':
    main()
