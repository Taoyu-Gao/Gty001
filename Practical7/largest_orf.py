seq = 'AAGAUCACUGCAAUGUGUGUGUCUGUUCUGAGAGGCUAAAAG'

start_codon = 'AUG'
stop_codons = ['UAA', 'UAG', 'UGA']

def find_longest_orf(seq):
    longest_orf = ''
    longest_length = 0
    
    for i in range(len(seq)):
        if seq[i:i+3] == start_codon:
            for j in range(i, len(seq) - 2, 3):
                codon = seq[j:j+3]
                if codon in stop_codons:
                    orf = seq[i:j+3]
                    if len(orf) > longest_length:
                        longest_length = len(orf)
                        longest_orf = orf
                    break  
    return longest_orf, longest_length
longest_orf, length = find_longest_orf(seq)
print(f"最长 ORF 序列: {longest_orf}")
print(f"最长 ORF 长度: {length} 个核苷酸")