from pathlib import Path

def huidigStation():
    path = Path('').absolute()
    while not Path.joinpath(path, "lokaal station").exists() :
        path = path.parent
    file = Path.joinpath(path, 'lokaal station')
    infile = open(file)
    return (infile.readline())