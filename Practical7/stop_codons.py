import re

input_file = 'Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa'
output_file = 'stop_genes.fa'
stop_codons = ['TAA', 'TAG', 'TGA']

def parse_fasta(filename):
    """读取 FASTA 文件，返回基因名和序列的列表"""
    genes = []
    with open(filename, 'r') as f:
        current_name = ''
        current_seq = []
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if current_name:
                    genes.append((current_name, ''.join(current_seq)))
                current_name = line[1:].split()[0]
                current_seq = []
            else:
                current_seq.append(line)
        if current_name:
            genes.append((current_name, ''.join(current_seq)))
    return genes

def contains_stop_codon(seq, stop_codons):
    """检查序列中是否包含任何终止密码子"""
    for stop in stop_codons:
        if stop in seq:
            return True
    return False

def get_stop_codons_present(seq, stop_codons):
    """返回序列中存在的终止密码子类型（去重）"""
    present = []
    for stop in stop_codons:
        if stop in seq:
            present.append(stop)
    return present
genes = parse_fasta(input_file)
print(f"共读取 {len(genes)} 个基因")
count = 0
with open(output_file, 'w') as out:
    for name, seq in genes:
        if contains_stop_codon(seq, stop_codons):
            stops = get_stop_codons_present(seq, stop_codons)
            new_name = f"{name}_{'_'.join(stops)}"
            out.write(f">{new_name}\n")
            for i in range(0, len(seq), 60):
                out.write(seq[i:i+60] + '\n')
            count += 1

print(f"找到 {count} 个包含终止密码子的基因")
print(f"结果已保存到 {output_file}")