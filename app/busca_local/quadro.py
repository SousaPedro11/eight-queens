from random import choice


def imprime_quadro(result, param):
    if not result:
        print([None])
    if param == 0 and result:
        element = choice(result)
        quadro = []
        for coluna in element:
            linha = ['.'] * len(element)
            linha[coluna] = 'Q'
            quadro.append(' '.join(linha))

        lista_caracteres = [x for x in quadro]
        for linha in lista_caracteres:
            print(' '.join(linha))
    else:
        quadro = []
        for element in result:
            for coluna in element:
                linha = ['.'] * len(element)
                linha[coluna] = 'Q'
                quadro.append(''.join(linha))

        lista_caracteres = [x for x in quadro]

        for i in range(0, len(lista_caracteres)):
            if i % len(lista_caracteres[i]) == 0:
                print('\n')
            print('  '.join(lista_caracteres[i]))
    print('\n')

