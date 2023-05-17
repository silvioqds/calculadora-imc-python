class Pessoa:
    def __init__(self, nome, altura, peso):
        self.nome = nome
        self.altura = altura
        self.peso = peso

    def setNome(self, nome):
        self.nome = nome

    def setAltura(self, altura):
        self.altura = altura

    def setPeso(self, peso):
        self.peso = peso

    def getNome(self):
        return self.nome

    def getAltura(self):
        return self.altura

    def getPeso(self):
        return self.peso

    def __getIMC(self):
        return self.peso/self.altura ** 2

    def printIMC(self):
        descricao = ''
        imc = self.__getIMC()
        if imc < 18.5:
            descricao = 'Magreza'
        elif imc < 25:
            descricao = 'Normal'
        elif imc < 30:
            descricao = 'Sobrepeso'
        elif imc > 30:
            descricao = 'Obesidade'

        print(self.nome + " seu IMC é %.2f" %imc + ":" + descricao)
