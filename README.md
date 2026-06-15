# 💼 Sistema Gerenciador Salarial

![Language](https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white) 
![Library](https://img.shields.io/badge/Library-Rich-blueviolet?style=for-the-badge)

Python

## 🚀 Tecnologias e Ferramentas  
Linguagem Principal: Python  
Bibliotecas/Dependências: Rich  
Paradigma: Programação Orientada a Objetos (POO)  
IDE Recomendada: Visual Studio Code  

## 📌 Funcionalidades  
Cadastrar Funcionários: Registro de funcionários horistas e mensalistas utilizando herança e classes abstratas.  

Cálculo Salarial: Processamento automático do salário líquido com aplicação do desconto do INSS.  

Análise Salarial: Comparação do salário final com o salário mínimo vigente, exibindo quantos salários mínimos o funcionário recebe.  

Interface Visual no Console: Exibição formatada com painéis estilizados utilizando a biblioteca Rich.  

## ⚡ Diferenciais Técnicos (Boas Práticas)  
Uso de Classes Abstratas: Implementação da classe abstrata `Funcionario` utilizando `ABC` e `@abstractmethod` para obrigar a implementação do método `Calcular_salario()`.  

Polimorfismo & Herança: Estrutura orientada a objetos com especialização para `FuncionarioHorista` e `FuncionarioMensalista`.  

Reaproveitamento de Código: Uso de `super()` para reutilização do construtor da classe base, reduzindo redundância.  

Padronização da Regra de Negócio: Centralização do desconto do INSS e salário mínimo como atributos de classe, facilitando manutenção futura.  

Clean Code & UX no Console: Organização dos métodos com responsabilidade única e interface visual aprimorada com cores e painéis no terminal.  

## ▶️ Como Executar  

Pré-requisitos (VS Code é opcional)  
- [Python 3](https://www.python.org/downloads/) instalado.  
- Biblioteca Rich instalada.  
- [Visual Studio Code](https://code.visualstudio.com/) instalado (Opcional).  

```bash
Passo a Passo  

  # 1. UMA SOLUÇÃO:

  # 1.1. Clone o projeto
  $ git clone https://github.com/seu-usuario/seu-repositorio.git
  
  # 1.2. Acesse a pasta
  $ cd seu-repositorio

  # 1.3. Instale as dependências
  $ pip install rich

  # 1.4. Execute a aplicação
  $ python main.py

# 2. OUTRA SOLUÇÃO:

# 2.1. Baixe o projeto:
Clique no botão verde 'Code' e selecione 'Download ZIP' (ou clone o repositório).

# 2.2. Abra o projeto:
Extraia os arquivos e abra a pasta no Visual Studio Code.

# 2.3. Instale a biblioteca necessária:
Execute no terminal:

pip install rich

# 2.4. Execute a aplicação:
Rode o arquivo principal com:

python main.py
```

# 👨‍💻 Autor

Desenvolvido por Kauan Koenigkan.
