class Episode:
    def __init__(self, series_name, season, episode_number, title, date, line):
        self.series = str(series_name).strip()
        self.season = season
        self.number = episode_number
        self.title = str(title).strip() or "Untitled Episode"
        self.date = str(date).strip()

        self.line = line
        self.is_valid = True
        self.errors = []

    def __repr__(self):
        return f"Episode(Line {self.line}: {self.series} S{self.season} E{self.number})"

    def get_uid(self):
        # clave unica para deduplicacion
        return (self.series.lower(), self.season, self.number)