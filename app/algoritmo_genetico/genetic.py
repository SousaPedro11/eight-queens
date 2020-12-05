import random


def gerar_cromossomo(nrainhas: int) -> list[int]:
    return [random.randint(1, nrainhas) for _ in range(nrainhas)]


def fitness(cromossomo: list) -> int:
    colisoes_horizontais = sum([cromossomo.count(rainha) - 1 for rainha in cromossomo]) / 2
    colisoes_diagonais = 0

    n_elementos_cromossomo = len(cromossomo)

    diagonal_esquerda = [0] * 2 * n_elementos_cromossomo
    diagonal_direita = [0] * 2 * n_elementos_cromossomo

    for i in range(n_elementos_cromossomo):
        diagonal_esquerda[i + cromossomo[i] - 1] += 1
        diagonal_direita[len(cromossomo) - i + cromossomo[i] - 2] += 1

    for i in range(2 * n_elementos_cromossomo - 1):
        contador = 0
        if diagonal_esquerda[i] > 1:
            contador += diagonal_esquerda[i] - 1
        if diagonal_direita[i] > 1:
            contador += diagonal_direita[i] - 1
        colisoes_diagonais += contador / (n_elementos_cromossomo - abs(i - n_elementos_cromossomo + 1))

    return int(max_fitness - (colisoes_horizontais + colisoes_diagonais))


def probabilidade(cromossomo, fitness):
    return fitness(cromossomo) / max_fitness


def escolha_aleatoria(populacao, probabilidade):
    populacao_probabilidade = zip(populacao, probabilidade)
    total = sum(prob for pop, prob in populacao_probabilidade)
    probabilidade_aleatoria = random.uniform(0, total)
    valor = 0
    for pop, prob in zip(populacao, probabilidade):
        if valor + prob >= probabilidade_aleatoria:
            return pop
        valor += prob
    assert False


def reproducao(individuo_1, individuo_2):
    tamanho_individuo = len(individuo_1)
    indice_aleatorio = random.randint(0, tamanho_individuo - 1)
    return individuo_1[0:indice_aleatorio] + individuo_2[indice_aleatorio:tamanho_individuo]


def mutacao(individuo):
    tamanho_individuo = len(individuo)
    indice_individuo = random.randint(0, tamanho_individuo - 1)
    valor = random.randint(1, tamanho_individuo)
    individuo[indice_individuo] = valor
    return individuo


def genetc_rainha(populacao, fitness):
    mutacao_probabilidade = 0.03
    populacao_nova = []
    probabilidades = [probabilidade(pop, fitness) for pop in populacao]
    for _ in range(len(populacao)):
        melhor_cromossomo_1 = escolha_aleatoria(populacao, probabilidades)
        melhor_cromossomo_2 = escolha_aleatoria(populacao, probabilidades)
        filho = reproducao(melhor_cromossomo_1, melhor_cromossomo_2)
        if random.random() < mutacao_probabilidade:
            filho = mutacao(filho)
        # imprime_cromossomo(filho)
        populacao_nova.append(filho)
        if fitness(filho) == max_fitness:
            break
    return populacao_nova


def imprime_cromossomo(cromossomo):
    print(f"Cromossomo = {str(cromossomo)},  Fitness = {fitness(cromossomo)}")


if __name__ == "__main__":
    numero_rainhas = 8
    max_fitness = (numero_rainhas * (numero_rainhas - 1)) / 2
    populacao = [gerar_cromossomo(numero_rainhas) for _ in range(200)]

    geracao = 1

    while not max_fitness in [fitness(cromossomo) for cromossomo in populacao]:
        print(f"=== Geração {geracao} ===")
        populacao = genetc_rainha(populacao, fitness)
        # print("")
        print(f"Fitness Máximo = {max([fitness(pop) for pop in populacao])}")
        geracao += 1
    cromossomos_saida = []
    print(f"Resolvido na Geração {geracao - 1}!")
    for individuo in populacao:
        if fitness(individuo) == max_fitness:
            print("Uma das soluções: ")
            cromossomos_saida = individuo
            imprime_cromossomo(cromossomos_saida)

    quadro = []

    for x in range(numero_rainhas):
        quadro.append(["x"] * numero_rainhas)

    for i in range(numero_rainhas):
        quadro[numero_rainhas - cromossomos_saida[i]][i] = "Q"


    def imprime_quadro(quadro):
        for linha in quadro:
            print(" ".join(linha))


    print()
    imprime_quadro(quadro)
