import csv
from models import Episode

def load_episodes(file_path):

    lista_resultado = []

    with open(file_path, mode='r', encoding='utf-8') as f:
            #el dict reader usa como diccionario columna:valor
        reader = csv.DictReader(f)

        for i, fila in enumerate(reader, start=2):

            last_ep = Episode(

                series_name=fila['series_name'],
                season=fila['season_number'],
                episode_number=fila['episode_number'],
                title=fila['episode_title'],
                date=fila['air_date'],
                line=i
            )

            lista_resultado.append(last_ep)

    return lista_resultado
