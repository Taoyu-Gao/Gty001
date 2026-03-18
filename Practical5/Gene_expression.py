import matplotlib.pyplot as plt
gene_expressions={"TP53":12.4,
    "EGFR":15.1,
    "BRCA1":8.2,
    "PTEN":5.3,
    "ESR1":10.7

}
print("=" * 50)
print("1. GENE EXPRESSION ANALYSIS")
print("=" * 50)
print("Initial gene expression dictionary:")
print(gene_expressions)
print(gene_expressions["TP53"])
gene_expressions["MYC"]=11.6
print(gene_expressions["MYC"])
gene=list(gene_expressions.keys())
expressions=list(gene_expressions.values())
plt.figure(figsize=(10,6))
plt.bar(gene, expressions, color='skyblue')
plt.title('Gene Expression Levels', fontsize=16, fontweight='bold')
plt.xlabel('Genes', fontsize=12)
plt.ylabel('Expression Level', fontsize=12)
for i, v in enumerate(expressions):
    plt.text(i, v + 0.1, str(v), ha='center', fontsize=10)
plt.tight_layout()  # 自动调整布局
plt.savefig('gene_expression.png', dpi=300, bbox_inches='tight')
plt.show()
gene_of_interest = "TP53"
print(f"\nQuerying gene: '{gene_of_interest}'")
if gene_of_interest in gene_expressions:
    print(f"✓ Expression value for {gene_of_interest}: {gene_expressions[gene_of_interest]}")
else:
    print(f"✗ Error: Gene '{gene_of_interest}' not found in the dataset!")
average_expression = sum(expressions) / len(expressions)
print(f"\n📊 Average gene expression level: {average_expression:.2f}")
print(f"   (based on {len(expressions)} genes)")