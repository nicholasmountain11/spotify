class Song_Attributes:
    danceability = 0.0
    loudness = 0.0
    valence = 0.0
    energy = 0.0
    speechiness = 0.0
    id = ''


    def __init__(self,attribute, id) -> None:
        self.danceability = attribute['danceability']
        self.loudness = attribute['loudness']
        self.valence = attribute['valence']
        self.energy = attribute['energy']
        self.speechiness = attribute['speechiness']
        self.id = id