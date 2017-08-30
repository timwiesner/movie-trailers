import webbrowser
import os
import re
import jinja2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)


def create_movie_tiles_content(movies):
    # The HTML content for this section of the page

    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        movie.trailer_youtube_id = trailer_youtube_id

    template = JINJA_ENVIRONMENT.get_template('index.html')

    return template.render({"movies": movies})

    #     # Append the tile for the movie with its content filled in
    #     content += movie_tile_content.format(
    #         movie_title=movie.title,
    #         poster_image_url=movie.poster_image_url,
    #         trailer_youtube_id=trailer_youtube_id,
    #         directors = movie.directors,
    #         screenwriters = movie.screenwriters,
    #         stars = movie.stars,
    #         release_date = movie.release_date,
    #         imdb_rating = movie.imdb_rating
    #     )
    # return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Output the file
    output_file.write(create_movie_tiles_content(movies))
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)