import matplotlib.pyplot as plt

input_file = 'stop_genes.fa'

start_codon = 'ATG'  
stop_codons = ['TAA', 'TAG', 'TGA']

def parse_fasta(filename):
    """读取 FASTA 文件，返回基因名和序列的字典"""
    genes = {}
    with open(filename, 'r') as f:
        current_name = ''
        current_seq = []
        for line in f:
            line = line.strip()
            if line.startswith('>'):
                if current_name:
                    genes[current_name] = ''.join(current_seq)
                current_name = line[1:] 
                current_seq = []
            else:
                current_seq.append(line)
        if current_name:
            genes[current_name] = ''.join(current_seq)
    return genes

def find_longest_orf_for_stop(seq, target_stop):
    """在序列中找出以 ATG 开始，以 target_stop 结束的最长 ORF"""
    longest_orf = ''
    longest_length = 0
    
    for i in range(len(seq) - 2):
        if seq[i:i+3] == start_codon:
            for j in range(i, len(seq) - 2, 3):
                codon = seq[j:j+3]
                if codon == target_stop:
                    orf = seq[i:j+3]
                    if len(orf) > longest_length:
                        longest_length = len(orf)
                        longest_orf = orf
                    break 
    return longest_orf

def count_codons_in_orf(orf):
    """统计 ORF 中所有密码子的出现次数（从起始密码子开始，每3个一组）"""
    codon_counts = {}
    for i in range(0, len(orf) - 2, 3):
        codon = orf[i:i+3]
        codon_counts[codon] = codon_counts.get(codon, 0) + 1
    return codon_counts

def main():
    print("可选的终止密码子: TAA, TAG, TGA")
    target_stop = input("请输入一个终止密码子: ").strip().upper()
    
    if target_stop not in stop_codons:
        print("错误：请输入有效的终止密码子 (TAA, TAG, TGA)")
        return
    try:
        genes = parse_fasta(input_file)
        print(f"共读取 {len(genes)} 个基因")
        print(f"基因名称示例: {list(genes.keys())[:5]}")  
    except FileNotFoundError:
        print(f"错误：找不到文件 {input_file}")
        print("请先运行 stop_codons.py 生成该文件")
        return
    target_genes = {}
    for name, seq in genes.items(): 
    
        if f"_{target_stop}" in name or name.endswith(f"_{target_stop}"):
            target_genes[name] = seq
    
    if not target_genes:
        print(f"没有找到包含 {target_stop} 的基因")
        return
    
    print(f"找到 {len(target_genes)} 个包含 {target_stop} 的基因")

    all_codon_counts = {}
    genes_with_orf = 0
    
    for name, seq in target_genes.items(): 
        orf = find_longest_orf_for_stop(seq, target_stop)
        if orf: 
            codon_counts = count_codons_in_orf(orf)
            for codon, count in codon_counts.items():
                all_codon_counts[codon] = all_codon_counts.get(codon, 0) + count
            genes_with_orf += 1
    
    if not all_codon_counts:
        print(f"在包含 {target_stop} 的基因中没有找到有效的 ORF")
        return
    
    print(f"在 {genes_with_orf} 个基因中找到了有效的 ORF")
    print(f"共统计了 {sum(all_codon_counts.values())} 个密码子")






    
    sorted_codons = sorted(all_codon_counts.items(), key=lambda x: x[1], reverse=True)
    top_15 = dict(sorted_codons[:15])
    other_count = sum(count for codon, count in sorted_codons[15:])
    
    if other_count > 0:
        top_15['Other'] = other_count
    plt.figure(figsize=(12, 8))
    plt.pie(top_15.values(), labels=top_15.keys(), autopct='%1.1f%%')
    plt.title(f'密码子使用频率分布\n终止密码子: {target_stop} (最长 ORF 分析)\n总计 {sum(all_codon_counts.values())} 个密码子')
    output_plot = f'codon_usage_{target_stop}.png'
    plt.savefig(output_plot, dpi=300, bbox_inches='tight')
    print(f"饼图已保存到: {output_plot}")
    plt.show()

if __name__ == "__main__":
    main()
