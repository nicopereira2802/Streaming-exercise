from parser import load_episodes
from validator import validate_episodes

def test_parseo():
    path = "data/episodes_input.csv"

    print("iniciando lectura ")
    print(60 * "-")

    listaEpisodios = load_episodes(path)

    print(f"existen : {len(listaEpisodios)} filas")

    for i in listaEpisodios:
        print(f" linea {i.line}: {i.series} - temporada {i.season}")

    
    validate_episodes(listaEpisodios)

    for i in listaEpisodios:
        estado = "VALID" if i.is_valid else "INVALID"

        print(
            f"line {i.line} | {i.series} | season: {i.season} | episode: {i.number} | {estado}"
        )

        if i.errors:
            for er in i.errors:
                print(f"  --> {er}")
        print()


if __name__ == "__main__":
    test_parseo()