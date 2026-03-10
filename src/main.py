from parser import load_episodes
from validator import validate_episodes
from deduplicator import deduplicate
from writer import save_data
from writer import save_report

def main():
    path = "data/episodes_input.csv"

    print("iniciando lectura ")
    print(60 * "-")

    listaEpisodios = load_episodes(path)

    print(f"existen : {len(listaEpisodios)} filas")

    for i in listaEpisodios:
        print(f" linea {i.line}: {i.series} - temporada {i.season}")

    print("-" * 60)

    valid_episodes = validate_episodes(listaEpisodios)

    for i in valid_episodes:
        estado = "VALID" if i.is_valid else "INVALID"

        print(
            f"line {i.line} | {i.series} | season: {i.season} | episode: {i.number} | {estado}"
        )

        if i.errors:
            for er in i.errors:
                print(f"  --> {er}")
        print()
    print("-" * 60)

    unique_episodes = deduplicate(valid_episodes)

    print(f"Episodes after deduplication: {len(unique_episodes)}")
    print("-" * 60)
    print("Final episodes:")

    for ep in unique_episodes:
        print(
            f"line {ep.line} | {ep.series} | S{ep.season}E{ep.number} | {ep.title} | {ep.date}"
        )

    save_data(unique_episodes,"output/episodes_clean.csv")
    save_report(listaEpisodios,unique_episodes,"output/report.md")


if __name__ == "__main__":
    main()