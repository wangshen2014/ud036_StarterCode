import media
"create empty list"
movie_list = []

"prepare all the materials of toy story"

title = "Toy Story"
story_line = "This article is about the original Toy Story film. For the film franchise, see Toy Story (franchise). For the video game, see Toy Story (video game). For other uses, see Toy Story (disambiguation)."
poster_image = "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg"
trailer = "https://www.youtube.com/watch?v=_CH6Os4tfyg"
"create toy_story objects"
toy_story = media.Movie(title,story_line,poster_image,trailer)

"same as above"
title = "Avatar"
story_line = "By 2154, humans have depleted Earth's natural resources, leading to a severe energy crisis. The Resources Development Administration (RDA for short) min"
poster_image = "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg"
trailer = "https://www.youtube.com/watch?v=a0CDJZu4M5I"

avatar = media.Movie(title,story_line,poster_image,trailer)

"add all of the movies into the list"
movie_list.append(toy_story)
movie_list.append(avatar)

"define a function"
def get_movie_list():
    return movie_list



    
