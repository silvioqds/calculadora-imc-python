from pessoa import Pessoa

def main():
    try:
        nome = input('Digite seu nome: ')
        altura = float(input('Digite sua altura:'))
        peso = float(input('Digite seu peso:'))

        pessoa = Pessoa(nome, altura, peso)       
        pessoa.printIMC()
    except:
        print('Ocorreu um erro.')


main()