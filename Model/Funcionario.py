class Funcionario:

    def __init__(self):
        self.__nome = ""
        self.__salarioBruto = 0
        self.__totalAcrescimos = 0
        self.__totalDescontos = 0

    def setNome(self, nome):
        self.__nome = nome

    def getNome(self):
        return self.__nome

    def setSalarioBruto(self, salarioBruto):
        self.__salarioBruto = salarioBruto

    def getSalarioBruto(self):
        return self.__salarioBruto

    def setTotalAcrescimos(self, totalAcrescimos):
        self.__totalAcrescimos = totalAcrescimos

    def getTotalAcrescimos(self):
        return self.__totalAcrescimos

    def setTotalDescontos(self, totalDescontos):
        self.__totalDescontos = totalDescontos

    def getTotalDescontos(self):
        return self.__totalDescontos

    def __calcularSalarioLiquido(self):
        salarioLiquido = self.__salarioBruto + self.__totalAcrescimos - self.__totalDescontos
        return salarioLiquido

    def toStr(self):
        return f"\nNome do Funcionário: {self.getNome()}\nSalário Líquido: {self.__calcularSalarioLiquido()}"
