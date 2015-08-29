import webbrowser
import os
import re


# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <script src="http://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
        body {
            padding-top: 80px;
            background-color:rgba(0,0,0,0.8);
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
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
        .overlay{
            position:absolute;
            height:100%;
            width:100%;
            top:0;
            left:0;
            background-color:rgba(0,0,0,0.8);
        }
        .desc{
            color:white;
            position:relative;
            align-self:center;   
            padding:50px 25px;
            line-height:1.7;
        }
        .rat{
            position:relative;
            color:white;
            align-self:center;
        }
        .trailer_btn{
            margin : 10px 0;
        }
        .ses{
            color:#fff;
            margin:0px;
        }
        .watch_trailer{
            color: white;
            font-weight: bold;
            position: absolute;
            font-size: 22px;
            margin: 20px 0px 0px 0px;
            bottom: 0px;
            left: 0px;
            right: 0px;
            background-color: lightslategrey;        
        }
    </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        //create overlay for ratings discriptions and submit button
        $(document).on('mouseenter','.hover',function(){
            //get description and ratings
            var description = $(this).attr('data-description');
            var rating = $(this).attr('data-rating');
            var seasons = $(this).attr('data-seasons');
            var seasonTemplate = '';
            //check if seasons exist and create html 
            if(seasons != "None"){
                seasonTemplate += '<h4 class="ses"> Seasons : '+seasons+'</h4>'
            }
            //append html code to the block
            $(this).append('<span class="overlay"><h4 class="desc">'+description+'</h4><br>'+seasonTemplate+'<br>'+
                            '<h3 class="rat"><img width=100 height=60 src="http://www.userlogos.org/files/logos/2690_fernandosantucci/imdb.new_.logo_.png"/> Rating : '+rating+'</h3>'+
                            '<span class="watch_trailer">Click To Watch Trailer</span></span>')
        });
        //remove overlay on mouseleave
        $(document).on('mouseleave','.hover',function(){
            $('div.hover').find('.overlay').remove();
        });
        //prevent video from playing when clicked on overlay
        $(document).on('click','span.overlay',function(e){
            //e.preventDefault();
            //e.stopPropagation();

        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.overlay', function (event) {
            var trailerYouTubeId = $(this).parent().attr('data-trailer-youtube-id')
            var sourceUrl = 'http://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''


# The main page layout and title bar
main_page_content = '''
  <body>
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

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Fresh Tomatoes Movie Trailers</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>
  </body>
</html>
'''


# A single movie entry html template
movie_tile_content = '''
<div class="col-md-6 col-lg-4 movie-tile hover text-center" data-seasons={seasons} data-description="{description}" data-rating="{rating}" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
    <img src="{poster_image_url}" width="220" height="342">
    <h2 style="color:#fff">{movie_title}</h2>
</div>
'''

movie_header = '''<div class="row well"><h2>Movies</h2></div>'''
# tv series header
tvseries_header = '''<div class="row well"><h2>TV series</h2></div>'''
def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content_movies = ''
    content_tv_series = ''
    content = ''
    
    #generate html as string for movies and concatinate to content_movies 
    for movie in movies[0]:
        content_movies += get_html_content(movie,True)        
    #generate html as string for Tv series and concatinate to content_tv_series
    for tvs in movies[1]:
        content_tv_series += get_html_content(tvs,False)

    content = movie_header+'<div class="row">'+content_movies+'</div>'+tvseries_header+'<div class="row">'+content_tv_series+'</div>'
    return content

# extract youtube id and generate html
# returns a string of html containing title,description,seasons(if tv series),rating and image url for all videos
def get_html_content(video,season_flag):
    # Extract the youtube ID from the url
    youtube_id_match = re.search(
        r'(?<=v=)[^&#]+', video.youtube_link)
    youtube_id_match = youtube_id_match or re.search(
        r'(?<=be/)[^&#]+', video.youtube_link)
    trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

    seasonNo = None;
    # check if its tvseries or movie and get number of seasons 
    if(not season_flag):
        seasonNo = video.seasons


    # Append the tile for the movie with its content filled in
    content = movie_tile_content.format(
        movie_title=video.title,
        poster_image_url=video.poster_image_url,
        rating = video.rating,
        description= video.description,
        trailer_youtube_id=trailer_youtube_id,
        seasons=seasonNo
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
