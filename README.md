# Analisador de Portas com Nmap em Python

Este projeto foi desenvolvido como parte dos meus estudos em **segurança da informação** e **programação em Python**.  
A ideia principal é integrar o **Nmap**, uma ferramenta de varredura de redes, com scripts em Python para automatizar e personalizar a análise de portas e serviços em hosts.

---

# Funcionalidades

- Varredura de portas em um ou múltiplos alvos.  
- Identificação de serviços rodando nas portas abertas.  
- Uso de threads para acelerar o processo.  
- Saída colorida no terminal para melhor visualização.  
- Possibilidade de exportar resultados.  

---

# Tecnologias Utilizadas

- **Python 3**  
- Biblioteca `nmap`  
- Biblioteca `colorama`  
- Threads para execução paralela  

---

# Como Executar

1. Instale as dependências necessárias:  
```bash
pip install python-nmap colorama
