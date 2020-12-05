import operator

from app.analise_resultado.solucoes import ler


def hill_climbing_analise():
    path_results = 'hill_climbing_results.csv'
    results = ler(path_results)
    h = {}
    cont = 0
    for r in results:
        cont += 1
        r = r.split('; ')
        if r[1] in h.keys():
            valor = h[r[1]]
            valor += 1
            h.update({r[1]: valor})
            continue
        h.update({r[1]: 1})
    print(f'Numero de soluções únicacs: {len(h)}')
    print('Soluções mais recorrentes:')
    print('\n'.join([f'{k}: {h.get(k)}' for k in h.keys() if h.get(k) > 1]))
    maximo = max(h.items(), key=operator.itemgetter(1))[1]
    hmax = {k: v for k, v in h.items() if v == maximo}
    print('Maior(es) ocorrencia(s):')
    for k, v in hmax.items():
        print(f'{k} ocorreu {v} vezes')
