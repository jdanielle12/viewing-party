# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    if title is None or genre is None or rating is None:
        return None
    movie = {"title": title, "genre": genre, "rating": rating}
    return movie
    
def add_to_watched(user_data, movie):
     user_data["watched"].append(movie)
     return user_data
 
def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data, title):
    watchlist_value = user_data["watchlist"]
    watched_value = user_data["watched"]
    
    for item in watchlist_value:
        item_title = item["title"]
        if  title == item_title:
            watchlist_value.remove(item)
            watched_value.append(item)
            return user_data
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
import statistics

def get_watched_avg_rating(user_data):

    try:
        number_of_movies = 0
        average_rating = 0.0
        for movie in user_data["watched"]: 
            average_rating += movie["rating"]
            number_of_movies += 1
        average_rating = average_rating / number_of_movies
        return average_rating
    
    except ZeroDivisionError:
        return 0.0


def get_most_watched_genre(user_data):
    genre = []
    if user_data["watched"] == []:
        return None
    
    for movie in user_data["watched"]:
        genre.append(movie["genre"])
    return statistics.mode(genre)
  

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def all_movies_friends_watched(user_data):
    friends_watched = []
    for item in user_data["friends"]:
        for movie in item["watched"]:
            friends_watched.append(movie) 
    return friends_watched   

def get_unique_watched(user_data):
    user_unique_movies = []
    friends_watched = all_movies_friends_watched(user_data)
    for movie in user_data["watched"]:
            if movie not in friends_watched:
                user_unique_movies.append(movie)
    return user_unique_movies   


def get_friends_unique_watched(user_data):
    friends_watched = all_movies_friends_watched(user_data)
    unique_movies = []
    for movie in friends_watched:
        if movie not in user_data["watched"] and movie not in unique_movies: 
            unique_movies.append(movie)
    return unique_movies

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    recommended_movies = []
    unique_movies = get_friends_unique_watched(user_data)
    for movie in unique_movies:
        if movie["host"] in user_data["subscriptions"]:
            recommended_movies.append(movie)
    return recommended_movies    

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    recommended_movies = []
    most_frequently_watched = get_most_watched_genre(user_data)
    unique_movies = get_friends_unique_watched(user_data)
    if most_frequently_watched is None:
        return []
    
    for movie in unique_movies:
        if movie["genre"] in most_frequently_watched:
            recommended_movies.append(movie)
    return recommended_movies

def get_rec_from_favorites(user_data): 
    friends_watched = all_movies_friends_watched(user_data)
    recommended_movies = []   
    for movie in user_data["favorites"]:
        if not movie in friends_watched:
            recommended_movies.append(movie)
    return recommended_movies