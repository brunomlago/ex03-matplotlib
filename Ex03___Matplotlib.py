import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Preparação dos dados
dados = {
    'mes': np.arange(1, 13),
    'creme_facial': [2500, 2630, 2140, 3400, 3600, 2760, 2980, 3700, 3540, 1990, 2340, 2900],
    'limpeza_facial': [1500, 1200, 1340, 1130, 1740, 1555, 1120, 1400, 1780, 1890, 2100, 1760],
    'pasta_dental': [5200, 5100, 4550, 5870, 4560, 4890, 4780, 5860, 6100, 8300, 7300, 7400],
    'sabonete': [9200, 6100, 9550, 8870, 7760, 7490, 8980, 9960, 8100, 10300, 13300, 14400],
    'shampoo': [1200, 2100, 3550, 1870, 1560, 1890, 1780, 2860, 2100, 2300, 2400, 1800],
    'hidratante': [1500, 1200, 1340, 1130, 1740, 1555, 1120, 1400, 1780, 1890, 2100, 1760]
}
df = pd.DataFrame(dados)

# Soma total de todas as vendas para cada mês
df['total_vendido'] = df[['creme_facial', 'limpeza_facial', 'pasta_dental', 'sabonete', 'shampoo', 'hidratante']].sum(axis=1)

# 1-Total de produtos vendidos por mês
fig1, ax1 = plt.subplots()
fig1.set_size_inches(10, 5)
ax1.plot(df['mes'], df['total_vendido'], color='blue', marker='o', linewidth=2, label='Total Vendido')
ax1.set_xlabel('Mês')
ax1.set_ylabel('Total de Produtos Vendidos')
ax1.set_title('1. Total de Produtos Vendidos por Mês')
ax1.set_xticks(df['mes'])
ax1.legend()
ax1.grid(True)

# 2-Todos os produtos vendidos por mês
fig2, ax2 = plt.subplots()
fig2.set_size_inches(10, 5)
produtos = ['creme_facial', 'limpeza_facial', 'pasta_dental', 'sabonete', 'shampoo', 'hidratante']

for produto in produtos:
    ax2.plot(df['mes'], df[produto], marker='o', linewidth=2, label=produto.replace('_', ' ').title())

ax2.set_xlabel('Mês')
ax2.set_ylabel('Quantidade Vendida')
ax2.set_title('2. Vendas de Todos os Produtos por Mês')
ax2.set_xticks(df['mes'])
ax2.legend(loc='upper left')
ax2.grid(True)

# 3-Comparativo de Creme Facial com Limpeza Facial
fig3, ax3 = plt.subplots()
fig3.set_size_inches(10, 5)
largura_barra = 0.35
x = df['mes']

ax3.bar(x - largura_barra/2, df['creme_facial'], largura_barra, label='Creme Facial', edgecolor="white")
ax3.bar(x + largura_barra/2, df['limpeza_facial'], largura_barra, label='Limpeza Facial', edgecolor="white")
ax3.set_xlabel('Mês')
ax3.set_ylabel('Quantidade Vendida')
ax3.set_title('3. Comparativo Mensal: Creme Facial vs Limpeza Facial')
ax3.set_xticks(x)
ax3.legend()
ax3.grid(axis='y', linestyle='--')

# 4-Histograma
fig4, ax4 = plt.subplots()
fig4.set_size_inches(10, 5)
faixas = [15000, 20000, 25000, 30000, 35000, 40000] 

ax4.hist(df['total_vendido'], bins=faixas, edgecolor="white", color='purple')
ax4.set_xlabel('Faixas de Quantidades de Produtos Vendidos')
ax4.set_ylabel('Quantidade de Meses (Frequência)')
ax4.set_title('4. Histograma: Distribuição das Vendas Totais')
ax4.set_xticks(faixas)
ax4.grid(axis='y')

# 5-Pizza
# Somando as vendas de todo o ano para cada produto
vendas_anuais = df[['creme_facial', 'limpeza_facial', 'pasta_dental', 'sabonete', 'shampoo', 'hidratante']].sum()
labels = [p.replace('_', ' ').title() for p in vendas_anuais.index]
explodir = [0.1, 0, 0, 0, 0, 0] # Destaca a primeira fatia (Creme Facial)

fig5, ax5 = plt.subplots()
fig5.set_size_inches(8, 8)
ax5.pie(vendas_anuais, labels=labels, explode=explodir, shadow=True, autopct='%1.1f%%')
ax5.set_title('5. % de Vendas Anuais por Produto')

# Exibir os gráficos
plt.show()