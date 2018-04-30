#Importação das classes necessárias para a execução do projeto
import fresh_tomatoes;
import media;

#Instância da classe Filme
toy_story = media.Filme("Toy Story",
                        "História de um menino e seus brinquedos que ganham vida.",
                        "https://i.pinimg.com/originals/9d/cf/51/9dcf514305b66681c188fff05ae4ca54.jpg",
                        "https://www.youtube.com/watch?v=4KPTXpQehio")

#Instância da classe Filme
avatar = media.Filme("Avatar",
                     "História de um soldado em um planeta de alienígenas.",
                     "http://www.mundoreal.xyz/wp-content/uploads/2014/08/Capa-do-Filme-Avatar.jpg",
                     "https://www.youtube.com/watch?v=WNW9Wz7k4pM")

#Instância da classe Filme
tropa_elite = media.Filme("Tropa de Elite",
                          "Filme que mostra as ações do BOPE para conter a violência na cidade do Rio de Janeiro.",
                          "https://londripost.files.wordpress.com/2010/10/tropadeelite2_01.jpg",
                          "https://www.youtube.com/watch?v=A6W-nNPl1T8")

#Instância da classe Filme
ratatouille = media.Filme("Ratatouille",
                          "Um rato que é chefe de cozinha",
                          "http://megapix.img.estaticos.tv.br/cache/cartazes/rat_cartaz_220x284.jpe",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

#Instância da classe Filme
midnight_in_paris = media.Filme("Midnight in Paris",
                          "Storyline",
                          "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                          "https://www.youtube.com/watch?v=FAfR8omt-CY")

#Instância da classe Filme
hunger_games = media.Filme("Jogos Vorazes",
                          "Storyline",
                          "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                          "https://www.youtube.com/watch?v=PbA63a7H0bo")

#Variável que recebe uma lista com os filmes que será exibidos no site
movies = [toy_story, avatar, tropa_elite, ratatouille, midnight_in_paris, hunger_games]

fresh_tomatoes.open_movies_page(movies)

#print(media.Filme.VALID_RATINGS)
#print(media.Filme.__doc__)

#print(tropa_elite.enredo)
#tropa_elite.show_trailer()
