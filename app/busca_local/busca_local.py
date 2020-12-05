import os
from time import time

from app.busca_local.util import salvar


class BuscaLocal(object):
    def busca(self, problema, tipo, iteracoes, nome):
        contador = 0
        inicio = time()
        resultados = list()
        sum = 0
        data = []
        path = os.path.join(os.path.abspath(os.path.dirname(__name__)), 'hill_climbing_count.txt')
        path_res = os.path.join(os.path.abspath(os.path.dirname(__name__)), 'hill_climbing_results.csv')
        self.create_file(path)
        self.create_file(path_res)

        for i in range(iteracoes):

            time_iter = time()
            status = 0
            resultado = tipo(problema)
            if problema.heuristica(resultado) == 0:
                contador += 1
                resultados.append(resultado)
                status = 1
                salvar('hill_climbing_results.csv', f'{i + 1}; {resultado}', 'a')
            sum += (time() - time_iter)
            data.append(f'{i + 1}; {time() - time_iter}; {sum}; {status}')
        salvar(nome + '.csv', data)
        print(f'Ratio: {contador}/{iteracoes}\tTempo: {time() - inicio}')

        return resultados

    def create_file(self, path):
        try:
            f = open(path)
            os.remove(path)
        except FileNotFoundError as e:
            print(e)
