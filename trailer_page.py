import fresh_tomatoes
import movies


# Create multiple instances of the Movie class
# containing some of my favorite movies

habla_con_ella = movies.Movie("Hable Con Ella", "Two men bond over their love \
                              for two comatose women.",
                              "http://www.gstatic.com/tv/thumb/movieposters/31117/p31117_p_v8_aa.jpg",   # noqa
                              "https://www.youtube.com/watch?v=7fl8tyEIXXI")

ghostbusters = movies.Movie("Ghostbusters", "Scientists save New York City",
                            "http://t3.gstatic.com/images?q=tbn:ANd9GcRJG5IBNzP5r0lNiVbjvc-V4ejuqDRWorvC9cAx8eBYQ4hb5eVY",  # noqa
                            "www.youtube.com/watch?v=t06VnA01LJg")

nine_to_five = movies.Movie("9 to 5", "Three secretaries deal with their \
                            misogynistic boss",
                            "https://upload.wikimedia.org/wikipedia/en/thumb/e/e0/9_to_5_moviep.jpg/220px-9_to_5_moviep.jpg",   # noqa
                            "https://www.youtube.com/watch?v=aOYDV3IIWFQ")

romancing_stone = movies.Movie("Romancing the Stone", "A Romance writer teams \
                                up with a mercenary to rescue her sister.",
                                "https://upload.wikimedia.org/wikipedia/en/thumb/8/84/Romancing_the_stone.jpg/220px-Romancing_the_stone.jpg",  # noqa
                                "https://www.youtube.com/watch?v=WokoWHHAxp4")

johnny_guitar = movies.Movie("Johnny Guitar", "Colorful western noir",
                              "http://t1.gstatic.com/images?q=tbn:ANd9GcTgnr0HnWzf-X3IQtLtKkUKQVPeICfGA0bgX2gTyR91D--NJiZP",  # noqa
                              "https://www.youtube.com/watch?v=ACgSyxdV9vE")

big_trouble_china = movies.Movie("Big Trouble in Little China", "Jack Burton \
                                saves Chinatown",
                                "http://t1.gstatic.com/images?q=tbn:ANd9GcSoqgsX65XvcSJuFlZ7kTSqRe3uSSpCjeklW-XudHB1TM0ej2e0",  # noqa
                                "https://www.youtube.com/watch?v=592EiTD2Hgo")


# Create a list containing my movie instances

movies = [habla_con_ella, ghostbusters,
          nine_to_five, romancing_stone, johnny_guitar,
          big_trouble_china]

# Call the open_movies_page function from the
# Fresh Tomatoes module

fresh_tomatoes.open_movies_page(movies)
