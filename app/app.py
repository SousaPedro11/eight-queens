import argparse

from app.analise_resultado.analise import hill_climbing_analise
from app.busca_local.busca_local import BuscaLocal
from app.busca_local.hill_climbing import hill_climbing_leatorio
from app.busca_local.n_rainhas import BuscaNRainhas
from app.busca_local.quadro import imprime_quadro


def app():
    help_str = "Programa que soluciona o problema das N-rainhas usando algoritmos de busca local."
    author = "Author: Pedro Sousa: https://www.github.com/sousapedro11/"
    args_dict = {"-n": 8, "-i": 50, "--all": 0}
    default_args = 'Default Args: ' + '; '.join(f'{k} = {v}' for k, v in args_dict.items())
    descriptor = '\n\t'.join([help_str, author, default_args])

    parser = argparse.ArgumentParser(description=descriptor, formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument("-n", type=int, default=8, help='Número de rainhas')
    parser.add_argument("-i", type=int, default=50, help='Número de iterações')
    parser.add_argument("-a", "--all", type=int, dest='all', action='store', choices=range(2), default=0,
                        help='0 - mostrar uma solução | 1 - mostrar todas as soluções')
    args = parser.parse_args()
    inicia_busca(args)
    hill_climbing_analise()


def inicia_busca(args):
    teste = BuscaLocal()
    problema = BuscaNRainhas(args.n)
    algoritmos = {
        "Hill Climbing Aleatorio": hill_climbing_leatorio
    }
    problemas = [problema for i in algoritmos]
    for i in algoritmos.keys():
        print(i)
        quadro = teste.busca(problemas[list(algoritmos).index(i)], algoritmos[i], args.i, i.replace(' ', '_').lower())
        # imprime_quadro(quadro, args.all)
