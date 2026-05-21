from rich import inspect
from funcionarios import *

def main():
    f1 = FuncionarioHorista("Kaike Silva", 45)
    f1.Calcular_salario()
    f1.Analisar_salario()

    f2 = FuncionarioMensalista("Jorge de Almeida", 4000)
    f2.Calcular_salario()
    f2.Analisar_salario()

if __name__ == "__main__":
    main()