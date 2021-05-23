# Analisando e gerando Dicionario
def notas(*nota, sit = 0):
    """
    -> Função para analisar notas do aluno.
    :param nota: Recebe nota (ou varias notas) do aluno.
    :param sit: (Opcional), diz baseado em sua média se sua situação está boa ou ruim
    :return: Dicionario com informações do aluno.
    Criado por Guilherme Gomes
    """
    dados = list()
    valores = dict()
    quant = maior = menor = soma = 0
    for n in nota:
        soma += n
        if quant == 0:
            maior = n
            menor = n
        else:
            if n > maior:
                maior = n
            if n < menor:
                menor = n
        quant += 1
    media = soma / quant
    valores['total'] = quant
    valores['maior'] = maior
    valores['menor'] = menor
    valores['média'] = media
    if sit == True:
        if media > 6:
            valores['situação'] = 'Boa'
        elif media < 6:
            valores['situação'] = 'Ruim'
    dados.append(valores)
    print(dados)


help(notas)
notas(5.5, 9.5, 10, 6.5, sit=True)
