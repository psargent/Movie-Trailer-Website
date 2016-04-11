__author__ = "Petra Sargent"
import media
import fresh_tomatoes

#Create instances of the Movie Class
home = media.Movie("Home",
                   "PG",
                   "A girl goes on the run with Oh, a funny fugitive alien",
                   "Release date: March 27,2015",
                   "Cast: Jim Parsons, Rihanna, Jennifer Lopez",
                   "https://upload.wikimedia.org/wikipedia/en/8/85/Home_%282015_film%29_poster.jpg",
                   "https://www.youtube.com/watch?v=MyqZf8LiWvM")


selma = media.Movie("Selma",
                    "PG-13",
                     "Historical drama film based on the 1965 Selma to Monegomery voting rights marches.",
                     "Release date: Janaury 9, 2015",
                     "Cast: David Oyelowo, Carmen Ejogo, Cuba Gooding Jr",
                     "https://upload.wikimedia.org/wikipedia/en/8/8f/Selma_poster.jpg",
                     "https://www.youtube.com/watch?v=x6t7vVTxaic")


insideout = media.Movie("Inside Out",
                        "PG",
                        "A 11-year-old emotions try to guide her through her families move.",
                        "Release date: June 19, 2015",
                        "Cast: Mindy Kaling, Amy Poheler, Phyllis Smith",
                        "https://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_%282015_film%29_poster.jpg",
                        "https://www.youtube.com/watch?v=seMwpP0yeu4")

slumdog_millionaire = media.Movie("Slumdog Millionaire",
                                  "R",
                                  "An eighteen year-old orphan is one question away from winning 20 million rupees",
                                  "Release date: December 25, 2008",
                                  "Cast:Dev Patel, Freida Pino, Madhur Mittal",
                                  "https://upload.wikimedia.org/wikipedia/en/f/fe/Slumdog_millionaire_ver2.jpg",
                                  "https://www.youtube.com/watch?v=AIzbwV7on6Q")

the_martian = media.Movie("The Martian",
                          "PG-13",
                          "An Astronaut is stranded and alone on Mars after presumed dead.",
                          "Release date: October 2, 2015",
                          "Cast: Matt Damon, Jessica Chastain, Kristin Wiig",
                          "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg",
                          "https://www.youtube.com/watch?v=ej3ioOneTy8")

best_man_holiday = media.Movie("Best Man Holiday",
                               "R",
                               "College friends get together for a holiday reunion.",
                               "Release date: November 15, 2013",
                               "Cast:  Morris Chestnut, Taye Diggs, Regina Hall",
                               "https://upload.wikimedia.org/wikipedia/en/d/d6/The_Best_Man_Holiday.jpg",
                               "https://www.youtube.com/watch?v=k6iNiJivOOQ")

#Create a list of movies
movies = [home, selma, insideout, slumdog_millionaire, the_martian, best_man_holiday]

#Create a webpage allowing users to review movies and watch the trailers 
fresh_tomatoes.open_movies_page(movies)
