from command.commands import *
def menu():
    command = ""
    headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {auth()}"
    }
    print("-TMDB CLI Tool")
    while command != "exit":
        command = input(f"> ")
        if "tmdb-app --type 'playing'" in command:
            exec("https://api.themoviedb.org/3/movie/now_playing?language=en-US&page=1",headers)
        elif "tmdb-app --type 'popular'" in command:
            exec("https://api.themoviedb.org/3/movie/popular?language=en-US&page=1",headers)
        elif "tmdb-app --type 'top'" in command:
            exec("https://api.themoviedb.org/3/movie/top_rated?language=en-US&page=1",headers)
        elif "tmdb-app --type 'upcoming'" in command:
            exec("https://api.themoviedb.org/3/movie/upcoming?language=en-US&page=1",headers)
        elif command != "exit":
            print("Invalid command")