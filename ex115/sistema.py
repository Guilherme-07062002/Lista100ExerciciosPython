from ex115.lib.interface import *
from time import sleep
from ex115.lib.arquivo import *

arq = 'cursoemvideo.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Ver pessoas cadastradas','Cadastrar Pessoa','Sair do Sistema'])
    if resposta == 1:
        # Opção de listar o conteudo
        lerArquivo(arq)
    elif resposta == 2:
        # Opção cadastrar pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        cabeçalho('Saindo do sistema...')
        break
    else:
        cabeçalho('ERRO! Digite uma opção válida.')
    sleep(2)