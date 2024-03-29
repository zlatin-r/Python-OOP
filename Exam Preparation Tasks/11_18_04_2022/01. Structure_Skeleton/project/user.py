class User:
    def __init__(self, username: str, age: int):
        self.username = username
        self.age = age
        self.movies_liked = []
        self.movies_owned = []

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not value.strip():
            raise ValueError("Invalid username!")
        self.__username = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 6:
            raise ValueError("Users under the age of 6 are not allowed!")
        self.__age = value

    def __str__(self):
        if self.movies_liked:
            result = [f"Username: {self.username},"
                    f" Age: {self.age}"
                    f"Liked movies:{}"]  # TODO ADD ALL MOVIES DETAILS
        else:
            result = ["No movies liked."]

        if self.movies_owned:
            result.append(f"Owned movies:"
                          f"{}")  # TODO ADD DETAILS OF ALL OWNED MOVIES
        else:
            result.append("No movies owned.")

        return "\n".join(result)
