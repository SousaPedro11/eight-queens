import os


def salvar(name, data, method='w'):
    BASEDIR = os.path.abspath(os.path.dirname(__name__))
    with open(os.path.join(BASEDIR, name), method) as f:
        if isinstance(data, list):
            f.writelines('\n'.join(data))
        else:
            f.write(data.__str__() + '\n')
