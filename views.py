from django.shortcuts import render
import os

# Create your views here.

#FUNCAO PARA SALVAR OS DADOS DE INPUT NO ARQUIVO HTML
#USA-SE ARQUIVO.WRITE PARA DIZER QUE O USUÁRIO VAI ESCREVER NO INPUT
#USAR A MESMA NOMENCLATURA USADA NO HTML, EX: INPUT_NOME
def cadastroCliente(request):
    if request.POST:
        with open('dados.txt', 'a') as arquivo:
            arquivo.write(request.POST['input_nome'] + '\n')
            arquivo.write(request.POST['input_endereco'] + '\n')
            arquivo.write(request.POST['input_complemento'] + '\n')
            arquivo.write(request.POST['input_cep'] + '\n')
            arquivo.write(request.POST['input_cidade'] + '\n')
            arquivo.write('--------------------------------\n')
            arquivo.close()
#ESSA SEGUNDA PARTE SERVE PARA ABRIR A PASTA "DADOS" E FAZER LEITURA DELA, EXIBINDO DEPOIS USANDO PYTHON NO HTML
    contexto = {}
    if os.path.isfile('dados.txt'):
        arquivo=open('dados.txt', 'r')
        lista = []
        for linha in arquivo:
            linha = linha.rstrip()
            lista.append(linha)
        arquivo.close()
        contexto={'dados':lista}


# RETORNA O TEMPLATE LIMPO E NOVO QUANDO A FUNÇÃO ACABA
    return render(request, 'cadastro_cliente.html', contexto)
