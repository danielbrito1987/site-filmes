import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Filmes - Daniel Brito</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
	<link rel="stylesheet" href="assets/css/main.css" />
	<style type="text/css" media="screen">
        body {
            padding-top: 80px;
        }
        #trailer #enredo .modal-dialog {
            margin-top: 80px;
            width: 800px;
            height: 400px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
		
		.movie-tile:hover h3{
			color: black;
		}
		
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
    </style>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body id="top">
    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>
	
	<!-- Enredo Modal -->
    <div class="modalEnredo" id="enredo">
      <div class="modal-dialog">
        <div class="modal-content">
          <div>
			{movie_enredo}
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
	<section id="banner" data-video="images/banner">
		<div class="inner">
			<header>
				<h1>Daniel Brito - Trailers</h1>
				<p>Aqui voce tera acesso a trailers de varios filmes<br />
				Todos os videos estao em alta resolucao e com som de altissima qualidade.</p>
			</header>
			<a href="#main" class="more">Learn More</a>
		</div>
	</section>	
	<div class="main">
		<div class="inner">
			<div class="thumbnails">
				{movie_tiles}
			</div>
		</div>
	</div>
	<footer id="footer">
		<div class="inner">
			<h2>Daniel Brito</h2>
			<p>Formado em Analise de Sistemas ha 4 anos, mas com experiencia em desenvolvimento de sites e softwares ha pelo menos 8 anos. Escolhi a area de TI, porque sempre gostei de informatica, sempre fui curioso para saber como os sites e os sistemas eram criados, sempre quis aprender o que esta por traz das paginas web. Hoje faco o curso de Desenvolvimento Web Full Stack para aprimorar os meus conhecimentos.</p>

			<p class="copyright">&copy; Untitled. Desenvolvido por <a href="http://danielbrito.net.br">Daniel Brito</a>.</p>
		</div>
	</footer>
	
	<script src="assets/js/jquery.min.js"></script>
	<script src="assets/js/jquery.scrolly.min.js"></script>
	<script src="assets/js/jquery.poptrox.min.js"></script>
	<script src="assets/js/skel.min.js"></script>
	<script src="assets/js/util.js"></script>
	<script src="assets/js/main.js"></script>
    <!--<div class="container">
      {movie_tiles}
    </div>-->
  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="box movie-tile" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
	<img src="{poster_image_url}" alt="" style="width: 300px; height: 400px;" />
	<div class="inner">
		<h3>{movie_title}</h3>
		<a href="{movie_enredo}" class="button fit" data-toggle="modalEnredo" data-target="#enredo">Enredo</a>
	</div>
</div>
'''


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            trailer_youtube_id=trailer_youtube_id,
			movie_enredo=movie.enredo
        )
		
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)
