import webbrowser


class Filme():
    """ Esta classe armazena informacoes relacionadas a filmes"""

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, titulo_filme, enredo_filme, imagem, trailer):
        self.title = titulo_filme
        self.enredo = enredo_filme
        self.poster_image_url = imagem
        self.trailer_youtube_url = trailer

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
