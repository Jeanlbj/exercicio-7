from Model.Funcionario import Funcionario

if __name__ == '__main__':

    # Criando Funcionário

    funcionario1 = Funcionario()
    funcionario1.setNome("Jean Lucas")
    funcionario1.setSalarioBruto(2000)
    funcionario1.setTotalAcrescimos(500)
    funcionario1.setTotalDescontos(100)

    funcionario2 = Funcionario()
    funcionario2.setNome("Murilo")
    funcionario2.setSalarioBruto(3250)
    funcionario2.setTotalAcrescimos(750)
    funcionario2.setTotalDescontos(200)

    funcionario3 = Funcionario()
    funcionario3.setNome("Giacopo")
    funcionario3.setSalarioBruto(10000)
    funcionario3.setTotalAcrescimos(350)
    funcionario3.setTotalDescontos(400)

    # Criando variavel para armazenar o nome e salário de cada funcionário

    salario1 = funcionario1.toStr()
    salario2 = funcionario2.toStr()
    salario3 = funcionario3.toStr()

    # Printado salários

    print("Salários:")

    print(salario1)
    print(salario2)
    print(salario3)

    print("\nPrograma finalizado")
