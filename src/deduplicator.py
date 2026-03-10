
# normalizar lineas eliminar espaios en blanco
def normalizer(line):
    if not line:
        return ""
    
    line = line.strip().lower()
    line =  " ".join(line.split())

    return line


def make_keys(ep):
    
    """
    Episodes must be considered duplicates when they refer to the same:
    (SeriesName_normalized, SeasonNumber, EpisodeNumber)
    Or
    (SeriesName_normalized, 0, EpisodeNumber, EpisodeTitle_normalized)
    Or
    (SeriesName_normalized, SeasonNumber, 0, EpisodeTitle_normalized)
    """
    series = normalizer(ep.series)
    title = normalizer(ep.title)

    key1 = (series, ep.season, ep.number)
    key2 = (series, 0,  ep.number, title)
    key3 = (series, ep.season, 0, title)

    return [key1,key2,key3]


def calculate_score(ep):

    score = 0

    if ep.date and ep.date != "Unknown":
        score += 100

    if ep.title and ep.title != "Untitled Episode":
        score += 50

    if ep.season > 0 and ep.number > 0:
        score += 25

    return score


def deduplicate(episodes):

    key_to_best = {}

    for ep in episodes:

        if not ep.is_valid:
            continue

        keys = make_keys(ep)
        score_actual = calculate_score(ep)

        for key in keys:

            if key not in key_to_best:

                key_to_best[key] = ep

            else:
                if score_actual > calculate_score(key_to_best[key]):
                    key_to_best[key] = ep


    unique = list(set(key_to_best.values()))
    unique.sort(key=lambda ep:ep.line)

    return unique