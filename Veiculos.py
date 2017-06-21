import re

dados_Veiculos = {}
veiculos_alugados = {}
DB_Veiculos = "DB_Veiculos.dat"
DB_Veiculos_alugados = "DB_Veiculos_alugados.dat"

class newCar(object):
    def __init__(self, a, b, c, d, e, f, g):
        dados_Veiculos[len(dados_Veiculos)] = [a, b, c, d, e, f, g]

def salvarDados():
    conteudo = ''
    Arquivo = open(DB_Veiculos, 'a+')
    for i in range(len(dados_Veiculos)):
        conteudo += dados_Veiculos[i][0] + '|' + dados_Veiculos[i][1] + '|' + dados_Veiculos[i][2] + '|' + dados_Veiculos[i][3] + '|' + \
                    dados_Veiculos[i][4] + '|' + dados_Veiculos[i][5] + '|' + dados_Veiculos[i][6] + '|\n'
    Arquivo.writelines(conteudo)
    Arquivo.close()


def limparDados():
    Arquivo = open(DB_Veiculos, 'w+')
    Arquivo.writelines("")
    Arquivo.close()


def puxarDados():
    try:
        Arquivo = open(DB_Veiculos, 'r+')
        Linha = Arquivo.readline()
        while Linha:
            valores = Linha.split("|")
            dados_Veiculos[len(dados_Veiculos)] = valores[0], valores[1], valores[2], valores[3], valores[4], valores[5], valores[6]
            Linha = Arquivo.readline()
        Arquivo.close()
    except:
        print("Não existe Dados")

def alugar():
    puxarDados(DB_Veiculos)
    j = 1
    print("Carros disponíveis:")
    for i in dados_Veiculos:
        print(j,"-",dados_Veiculos[i][0])
        j += 1
    print("\n0 - Nenhum")
    escolha_d_carro = int(input("Qual Carro quer alugar?"))
    if escolha_d_carro != 0:
        cont = input("Você irá alugar o veículo:\n",dados_Veiculos[escolha_d_carro-1],"\n Continuar? (S/n)").upper()
        if cont == "S":
            veiculos_alugados = dados_Veiculos[escolha_d_carro - 1][:]
            dados_Veiculos.pop(escolha_d_carro - 1)

def pesquisar(termo):
    puxarDados()
    for i in dados_Veiculos:
        if termo.upper() in dados_Veiculos[i][0].upper():
            print(dados_Veiculos[i])


#VALIDAÇÕES
def validaPlaca(m):
    while bool(re.match("^\w{3}-\d{4}$", m)) is False:
        Car_Plate = input("Placa do veículo inválida!\nDigite a placa do carro no formato 'XXX-0000': ")

def validaRenavam(ano, renavam):
    ano = int(ano)
    tam = len(renavam)

    while bool((ano < 2013 and tam == 9) or (ano >= 2013 and tam == 11)) is False:
        renavam = input("Número renavam inválido!\nDigite um número renavam válido: ")
