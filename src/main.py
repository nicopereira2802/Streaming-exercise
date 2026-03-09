from parser import load_episodes

def test_parseo():
    path = "data/episodes_input.csv"

    print("iniciando lectura ")
    print(60 * "-")

    listaEpisodios = load_episodes(path)

    print(f"existen : {len(listaEpisodios)} filas")

    for i in listaEpisodios:
        print(f" linea {i.line}: {i.series} - temporada {i.season}")

if __name__ == "__main__":
    test_parseo()