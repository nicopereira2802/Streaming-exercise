class Episode:
    def __init__(self,series_name,season,episode_number,title,date,line):
        self.series = str(series_name).strip()
        self.season = season
        self.number = self.number
        self.title = str(title).strip or "Untitle"
        self.date = str(date).strip

        self.line = line
        self.is_valid = True  # es verdadero hasta que la validacion diga lo contrario
        self.errors = []     #se guarda el motivo del fallo de validar


    def __repr__(self):
        return f"Episode(Line {self.line}: {self.series} S{self.season} E{self.number})"
    
    
    def get_uid(self):
        #clave unica para depuplicacion
        # usa el nombre, temporada y numero
        return (self.series.lower(), str(self.season), str(self.number))
    
