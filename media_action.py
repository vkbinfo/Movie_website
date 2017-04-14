import media
import fresh_tomatoes

beautiful_mind=media.Movie("A Beautiful Mind",
                      "John Nash, a brilliant but asocial mathematical genius,"+
                      " finds himself in pain when he encounters"+
                      "da cruel disorder. He ultimately overcomes his struggles and emerges free of any trauma.",
                      "http://www.geeksundergrace.com/wp-content/uploads/2015/11/toystory4.jpg",
                      "https://www.youtube.com/watch?v=JcpWXaA2qeg")

lord_of_the_ring=media.Movie("The Lord of the Rings: The Fellowship of the Ring",
                   "A young hobbit, Frodo, who has found the One Ring that belongs to the Dark Lord Sauron,"
                   " begins his journey with eight companions to Mount Doom, the only place where it can be destroyed.",
                    "https://www.gstatic.com/tv/thumb/movieposters/28828/p28828_p_v8_as.jpg",
                    "https://www.youtube.com/watch?v=V75dMMIW2B4")

shawshank_redemption=media.Movie("The Shawshank Redemption",
                   "Andy Dufresne, a successful banker, is arrested for the murders of his wife and her lover,and is "
                   "sentenced to life imprisonment at the Shawshank prison. He becomes the most unconventional prisoner.",
                    "https://t0.gstatic.com/images?q=tbn:ANd9GcSkmMH-bEDUS2TmK8amBqgIMgrfzN1_mImChPuMrunA1XjNTSKm",
                    "https://www.youtube.com/watch?v=6hB3S9bIaco")

avatar=media.Movie("Avatar",
                   "A marine on a alien planet.",
                    "https://t0.gstatic.com/images?q=tbn:ANd9GcQCfmvrE4fMo2cd8esc7mDZPtFSJThAujddMPkRtti1_ij6u-jp",
                    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

man_from_earth=media.Movie("The Man from Earth",
                   "College professors discuss many topics with a colleague who claims to be thousands of years old.",
                    "https://www.gstatic.com/tv/thumb/dvdboxart/174565/p174565_d_v8_aa.jpg",
                    "https://www.youtube.com/watch?v=9mOIxyRTY5I")

dil_chahta_hai=media.Movie("Dil Chahta Hai",
                   "Three friends who share a deep bond are separated due to their different approaches towards "
                   "relationships. Akash goes to Australia, Sameer gets busy wooing a girl and Siddharth devotes himself to art.",
                    "https://www.gstatic.com/tv/thumb/movieposters/73893/p73893_p_v8_aa.jpg",
                    "https://www.youtube.com/watch?v=m13b25V0B10")

movie_list=[beautiful_mind,lord_of_the_ring,shawshank_redemption,avatar,man_from_earth,dil_chahta_hai]
fresh_tomatoes.open_movies_page(movie_list)