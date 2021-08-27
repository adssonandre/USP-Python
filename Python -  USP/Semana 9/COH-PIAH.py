import re


def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")
    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))
    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")

    return textos


def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)


def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()


def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    i = 0
    soma = 0
    while i < len(as_a):
        similaridade = abs(as_a[i] - as_b[i])
        soma += similaridade
        i += 1

    return soma / 6


def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    wal_a = tamanho_medio_palavra(texto)
    ttr_a = relacao_type_token(texto)
    hlr_a = razao_hapax_legomana(texto)
    sal_a = tamanho_medio_sentenca(texto)
    sac_a = complexidade_media_sentenca(texto)
    pal_a = tamanho_medio_frase(texto)

    return [wal_a, ttr_a, hlr_a, sal_a, sac_a, pal_a]


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    i = 0
    t = 1
    infectado = 0
    grau = compara_assinatura(calcula_assinatura(textos[i]), ass_cp)
    while i < len(textos):
        i += 1
        infectado = grau
        infectado = compara_assinatura(calcula_assinatura(textos[i]), ass_cp)
        if infectado < grau:
            grau = infectado
            t += 1

    return t

def main():
    '''Inicia o programa'''
    textos = le_textos()
    ass_cp = le_assinatura()
    for texto in textos:
        avalia_textos(textos, ass_cp)

    return print("O autor do texto ", avalia_textos(textos, ass_cp) ," está infectado com COH-PIAH")

def tamanho_medio_palavra(texto):
    '''Soma dos tamanhos das palavras dividida pelo número total de palavras'''
    soma_dos_tamanhos_das_palavras = 0
    lista_de_palavras = []
    for sentenca in separa_sentencas(texto):
        for frase in separa_frases(sentenca):
            for palavra in separa_palavras(frase):
                soma_dos_tamanhos_das_palavras += len(palavra)
                lista_de_palavras.append(palavra)
    return soma_dos_tamanhos_das_palavras / len(lista_de_palavras)


def relacao_type_token(texto):
    '''Número de palavras diferentes dividido pelo número total de palavras'''
    lista_de_palavras = []
    for sentenca in separa_sentencas(texto):
        for frase in separa_frases(sentenca):
            for palavra in separa_palavras(frase):
                lista_de_palavras.append(palavra)
    return n_palavras_diferentes(lista_de_palavras) / len(lista_de_palavras)


def razao_hapax_legomana(texto):
    '''Número de palavras que aparecem uma única vez dividido pelo total de palavras'''
    lista_de_palavras = []
    for sentenca in separa_sentencas(texto):
        for frase in separa_frases(sentenca):
            for palavra in separa_palavras(frase):
                lista_de_palavras.append(palavra)
    return n_palavras_unicas(lista_de_palavras) / len(lista_de_palavras)


def tamanho_medio_sentenca(texto):
    '''Soma dos números de caracteres em todas as sentenças dividida pelo número de sentenças'''
    soma_dos_tamanhos_das_sentencas = 0
    lista_de_sentencas = []
    for sentenca in separa_sentencas(texto):
        lista_de_sentencas.append(sentenca)
        soma_dos_tamanhos_das_sentencas += len(sentenca)
    return soma_dos_tamanhos_das_sentencas / len(lista_de_sentencas)


def complexidade_media_sentenca(texto):
    '''Número total de frases dividido pelo número de sentenças'''
    numero_de_sentecas = 0
    numero_total_de_frases = 0
    for sentenca in separa_sentencas(texto):
        numero_de_sentecas += 1
        for frase in separa_frases(sentenca):
            numero_total_de_frases += 1
    return numero_total_de_frases / numero_de_sentecas


def tamanho_medio_frase(texto):
    '''Soma do número de caracteres em cada frase dividida pelo número de frases no texto'''
    numero_total_de_frases = 0
    lista_de_frases = []
    caracteres_nas_frases = 0
    for sentenca in separa_sentencas(texto):
        for frase in separa_frases(sentenca):
            lista_de_frases.append(frase)
            numero_total_de_frases += 1
            for palavra in frase:
                caracteres_nas_frases += len(palavra)
    return caracteres_nas_frases / len(lista_de_frases)


# Start
main()
