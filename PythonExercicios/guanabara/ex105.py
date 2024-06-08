#lista = {}


def notas(*num, sit=False):
    """
    Função para analisar notas e situações de vários alunos.
    :param num: uma ou mais notas de alunos (aceita várias).
    :param sit: valor opcional, indicando se deve ou não adicionar a situação.
    :return: dicionário com várias informações sobre a situação da turma.
    """
    lista = {}
    #lista['nota'] = num
    lista['total'] = len(num)
    lista['maior'] = max(num)
    lista['menor'] = min(num)
    lista['média'] = sum(num)/len(num)

    if sit == True:
        if lista['média'] < 6 :
            lista['situação']='REPROVADO'
        elif 6<= lista['média'] < 7:
            lista['situação']='RAZOÁVEL'
        else:
            lista['situação']='APROVADO'
    #del lista['nota']
    print(lista)


notas(6, 5, 6.5, 7, 8, sit=True)
help(notas)
