import fresh_tomatoes
import media

# Instância da classe Filme
toy_story = media.Filme("Toy Story",
                        "Historia de um menino e "
                        "seus brinquedos que ganham vida.",
                        "https://i.pinimg.com/originals/9d/cf/51/"
                        "9dcf514305b66681c188fff05ae4ca54.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Filme("Avatar",
                     "Historia de um soldado "
                     "em um planeta de alienigenas.",
                     "http://www.mundoreal.xyz/wp-content/uploads/"
                     "2014/08/Capa-do-Filme-Avatar.jpg",
                     "https://www.youtube.com/watch?v=WNW9Wz7k4pM")


tropa_elite = media.Filme("Tropa de Elite",
                          "Filme que mostra as acoes do BOPE "
                          "para conter a violencia"
                          " na cidade do Rio de Janeiro.",
                          "https://londripost.files.wordpress.com"
                          "/2010/10/tropadeelite2_01.jpg",
                          "https://www.youtube.com/watch?v=A6W-nNPl1T8")

ratatouille = media.Filme("Ratatouille",
                          "Um rato que e chefe de cozinha",
                          "http://megapix.img.estaticos.tv.br"
                          "/cache/cartazes/rat_cartaz_220x284.jpe",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

vingadores = media.Filme("Os Vingadores",
                         "Nick Fury, diretor da agencia "
                         "de espionagem S.H.I.E.L.D., "
                         "chega a um centro de pesquisa "
                         "remoto durante uma evacuacao. "
                         "O Tesseract, uma fonte de energia "
                         "de potencial desconhecido, "
                         "ja ativado, abriu um portal atraves "
                         "do espaco, do qual o deus "
                         "nordico exilado Loki ressurge. "
                         "Loki leva o Tesseract (Cubo Cosmico) "
                         "e usa suas habilidades para controlar "
                         "as mentes de varias pessoas da "
                         "S.H.I.E.L.D., a fim de que eles "
                         "o ajudem em sua fuga.",
                         "https://cdn.movieweb.com/img.teasers.posters/"
                         "FIruhzrtaK9Buw_364_a/Marvels-The-Avengers.jpg",
                         "https://www.youtube.com/watch?v=eOrNdBpGMv8")

hunger_games = media.Filme("Jogos Vorazes",
                           "A historia e estabelecida em "
                           "um periodo distopico pos-apocaliptico "
                           "na nacao de Panem, onde garotos e "
                           "garotas de 12 a 18 anos devem "
                           "participar dos Jogos Vorazes, "
                           "um evento anual televisionado na qual "
                           "os tributos precisam lutar ate "
                           "a morte ate que sobre apenas um, "
                           "que e coroado vencedor.",
                           "http://upload.wikimedia.org/wikipedia/"
                           "en/4/42/HungerGamesPoster.jpg",
                           "https://www.youtube.com/watch?v=PbA63a7H0bo")

# Variável que recebe uma lista com os filmes que será exibidos no site
movies = [toy_story, avatar, tropa_elite,
          ratatouille, vingadores, hunger_games]

# Geração da página com os filmes
fresh_tomatoes.open_movies_page(movies)
