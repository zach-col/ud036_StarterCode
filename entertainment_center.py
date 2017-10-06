# import package's

import fresh_tomatoes
import media

# creating movie object's work cited: Wikipedia and Youtube.
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life.",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=c3986gGp3Qs"
                        )

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=a0CDJZu4M5I"
                     )

good_will_hunting = media.Movie("Good Will Hunting",
                                "A story of a 20 year old genius"
                                " who find's himself in trouble. "
                                "The only way out is to take therapy "
                                "session's and study math",
                                "https://upload.wikimedia.org/wikipedia/en/thumb/b/b8/Good_Will_Hunting_theatrical_poster.jpg/220px-Good_Will_Hunting_theatrical_poster.jpg",  # NOQA
                                "https://www.youtube.com/watch?v=CSZeSlTrgMA"
                                )

transformers = media.Movie("Transformer's",
                           "In a world were everything seem's"
                           "to be normal a teenager named Sam, "
                           "find's out his car is secretly part "
                           "of an alien group called the Autobot's.",
                           "https://upload.wikimedia.org/wikipedia/en/thumb/6/66/Transformers07.jpg/220px-Transformers07.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=WiBwU2JjYz8"
                           )

tron_legacy = media.Movie("Tron Legacy",
                          "Flynn the owner of an arcade shop "
                          "send's a message to his son Sam after "
                          "his father has been lost for quite some "
                          "time, after responding sam find's himself"
                          "in a virtual reality",
                          "https://upload.wikimedia.org/wikipedia/en/thumb/c/c2/Tron_Legacy_poster.jpg/220px-Tron_Legacy_poster.jpg",  # NOQA
                          "https://www.youtube.com/watch?v=TiUmrX7CxGA"
                          )

the_great_gatsby = media.Movie("The Great Gatsby",
                               "The journalist Nick Carraway write's of "
                               "the legandary J.Gatsby a man everyone has "
                               "heard of but have never really met.",
                               "https://upload.wikimedia.org/wikipedia/en/thumb/c/c2/TheGreatGatsby2013Poster.jpg/220px-TheGreatGatsby2013Poster.jpg",  # NOQA
                               "https://www.youtube.com/watch?v=hZvpYtvAcTA"
                               )

# creating list of all movie's
movies = [toy_story,
          avatar,
          good_will_hunting,
          transformers,
          tron_legacy,
          the_great_gatsby
          ]

# creating html page
fresh_tomatoes.open_movies_page(movies)

