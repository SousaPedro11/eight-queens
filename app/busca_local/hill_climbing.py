from app.busca_local.util import salvar


def hill_climbing(problema):
    atual = problema.estado_inicial()
    while True:
        vizinhos = problema.estado_proximo(atual)

        if not vizinhos:
            break

        vizinho = max(vizinhos, key=lambda estado: problema.heuristica(estado))

        if problema.heuristica(vizinho) <= problema.heuristica(atual):
            break
        atual = vizinho
    return atual


def hill_climbing_leatorio(problema, limite=10):
    estado = problema.estado_inicial()
    contador = 0
    while problema.teste_objetivo(estado) is False and contador < limite:
        estado = hill_climbing(problema)
        contador += 1
    salvar('hill_climbing_count.txt', contador, 'a')
    return estado
