from project.movie_specification.movie import Movie
from project.user import User


class MovieApp:
    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username: str, age: int):
        if self._find_user_by_username(username):
            raise Exception("User already exists!")

        new_user = User(username, age)
        self.users_collection.append(new_user)
        return f"{username} registered successfully."

    def upload_movie(self, username: str, movie: Movie):
        user = self._find_user_by_username(username)

        if user:
            raise Exception("This user does not exist!")

        self._check_if_user_own_the_movie(user, movie)

        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")

        user.movies_owned.append(movie)
        self.movies_collection.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username: str, movie: Movie, **kwargs):
        user = self._find_user_by_username(username)
        self._check_if_user_own_the_movie(user, movie)
        self._check_if_movie_is_uploaded(movie)

        for key, value in kwargs.items():
            movie.key = value

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username: str, movie: Movie):
        user = self._find_user_by_username(username)
        self._check_if_movie_is_uploaded(movie)
        self._check_if_user_own_the_movie(user, movie)

        self.movies_collection.remove(movie)
        user.movies_owned.remove(movie)

        return f"{username} successfully deleted {movie.title} movie."

    def like_movie(self, username: str, movie: Movie):
        user = self._find_user_by_username(username)

        if movie in user.movies_owned:
            raise Exception(f"{username} is the owner of the movie {movie.title}!")

        if movie in user.movies_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")

        movie.likes += 1
        user.movies_liked.append(movie)
        return f"{username} liked {movie.title} movie."



    # HELPING METHODS:

    def _find_user_by_username(self, username: str):
        user = next(filter(lambda u: u.username == username, self.users_collection), None)
        return user

    def _check_if_user_own_the_movie(self, user: User, movie: Movie):
        if movie not in user.movies_owned:
            raise Exception(f"{user.username} is not the owner of the movie {movie.title}!")

    def _check_if_movie_is_uploaded(self, movie: Movie):
        if movie not in self.movies_collection:
            raise Exception("The movie {movie_title} is not uploaded!")
