
def validate_series(ep):
    # si no hay nombre descartar
    if not ep.series:
        ep.is_valid = False
        ep.errors.append("Missing series naem")


def validate_season(ep):
    # si no hay, esta vacio, es negativo o no es numero poner cero
    try:
        season = int(ep.season)
        if season < 0:
            ep.season = 0
            ep.errors.append("Invalid number, so it stablish cero (0)")
        else:
            ep.season = season
    except:
        ep.season = 0
        ep.is_valid = False
        ep.errors.append("Season number Not numeric so season set cero (0)")

def validate_episode_number(ep):
    try:
        number = int(ep.number)
        if(number < 0):
            ep.number = 0
            ep.errors.append("Invalida number, set cero (0)")
        else:
            ep.number = number
    except:
        ep.number = 0
        ep.is_valid = False
        ep.errors.append("Episode number not numeric, set cero")

def validate_episodes(episodes):
    for ep in episodes:
        validate_series(ep)
        validate_season(ep)
        validate_episode_number(ep)
        validate_title(ep)
        
