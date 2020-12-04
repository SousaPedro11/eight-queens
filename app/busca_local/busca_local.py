from time import time


class BuscaLocal(object):
    def busca(self, problema, tipo, iteracoes):
        contador = 0
        inicio = time()
        resultados = list()

        for i in range(iteracoes):
            resultado = tipo(problema)
            if problema.heuristica(resultado) == 0:
                contador += 1
                resultados.append(resultado)
        print(f'Ratio: {contador}/{iteracoes}\tTempo: {time() - inicio}')

        return resultados
