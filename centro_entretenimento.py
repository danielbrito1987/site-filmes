#Importa��o das classes necess�rias para a execu��o do projeto
import fresh_tomatoes;
import media;

#Inst�ncia da classe Filme
toy_story = media.Filme("Toy Story",
                        "Hist�ria de um menino e seus brinquedos que ganham vida.",
                        "https://i.pinimg.com/originals/9d/cf/51/9dcf514305b66681c188fff05ae4ca54.jpg",
                        "https://www.youtube.com/watch?v=4KPTXpQehio")

#Inst�ncia da classe Filme
avatar = media.Filme("Avatar",
                     "Hist�ria de um soldado em um planeta de alien�genas.",
                     "http://www.mundoreal.xyz/wp-content/uploads/2014/08/Capa-do-Filme-Avatar.jpg",
                     "https://www.youtube.com/watch?v=WNW9Wz7k4pM")

#Inst�ncia da classe Filme
tropa_elite = media.Filme("Tropa de Elite",
                          "Filme que mostra as a��es do BOPE para conter a viol�ncia na cidade do Rio de Janeiro.",
                          "https://londripost.files.wordpress.com/2010/10/tropadeelite2_01.jpg",
                          "https://www.youtube.com/watch?v=A6W-nNPl1T8")

#Inst�ncia da classe Filme
ratatouille = media.Filme("Ratatouille",
                          "Um rato que � chefe de cozinha",
                          "http://megapix.img.estaticos.tv.br/cache/cartazes/rat_cartaz_220x284.jpe",
                          "https://www.youtube.com/watch?v=c3sBBRxDAqk")

#Inst�ncia da classe Filme
midnight_in_paris = media.Filme("Midnight in Paris",
                          "Storyline",
                          "http://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",
                          "https://www.youtube.com/watch?v=FAfR8omt-CY")

#Inst�ncia da classe Filme
hunger_games = media.Filme("Jogos Vorazes",
                          "Storyline",
                          "http://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",
                          "https://www.youtube.com/watch?v=PbA63a7H0bo")

#Vari�vel que recebe uma lista com os filmes que ser� exibidos no site
movies = [toy_story, avatar, tropa_elite, ratatouille, midnight_in_paris, hunger_games]

fresh_tomatoes.open_movies_page(movies)

#print(media.Filme.VALID_RATINGS)
#print(media.Filme.__doc__)

#print(tropa_elite.enredo)
#tropa_elite.show_trailer()
