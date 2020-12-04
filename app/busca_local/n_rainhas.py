from abc import abstractmethod, ABC
from collections import Counter
from random import choice, randrange


class Problema(ABC):

    def __init__(self, inicial=None):
        pass

    @abstractmethod
    def estado_inicial(self):
        pass

    @abstractmethod
    def teste_objetivo(self, estado):
        pass

    @abstractmethod
    def heuristica(self, estado):
        pass

    @abstractmethod
    def estado_proximo(self, estado):
        pass

    def estado_proximo_aleatorio(self, estado):
        return choice(self.estado_proximo(estado))


class BuscaNRainhas(Problema):
    def __init__(self, inicial):
        super().__init__()
        self.number = inicial

    def estado_inicial(self):
        return [randrange(self.number) for i in range(self.number)]

    def teste_objetivo(self, estado):
        colunas_rainha, lc_delta, lc_soma = set(), set(), set()
        for linha, coluna in enumerate(estado):
            if coluna in colunas_rainha or ((linha - coluna) in lc_delta) or ((linha + coluna) in lc_soma):
                return False
            colunas_rainha.add(coluna)
            lc_delta.add(linha - coluna)
            lc_delta.add(linha + coluna)
        return True

    def heuristica(self, estado) -> int:
        colunas_rainha, lc_delta, lc_soma = Counter(), Counter(), Counter()
        colisoes = 0
        for linha, coluna in enumerate(estado):
            colunas_rainha[coluna] += 1
            lc_delta[linha - coluna] += 1
            lc_soma[linha + coluna] += 1

        for contador in [colunas_rainha, lc_delta, lc_soma]:
            for key in contador:
                colisoes += contador[key] * (contador[key] - 1) / 2
        return -colisoes

    def estado_proximo(self, estado):
        estados_proximos = []

        for linha in range(self.number):
            for coluna in range(self.number):
                if coluna != estado[linha]:
                    aux = list(estado)
                    aux[linha] = coluna
                    estados_proximos.append(aux)
        return estados_proximos
