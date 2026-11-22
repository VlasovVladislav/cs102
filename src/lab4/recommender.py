from src.lab4.models import Movie


class RecommendationSystem:
    """Система рекомендаций фильмов на основе истории просмотров пользователей."""
    def __init__(self, film_catalog: dict[int, Movie], users_history: list[list[int]]):
        self.film_catalog = film_catalog
        self.users_history = users_history

    def find_similar_users(self, curr_user_history: list[int]) -> list[list[int]]:

        """Находит пользователей, просмотревших не менее 50% фильмов текущего пользователя."""

        curr_user_history = set(curr_user_history)
        if len(curr_user_history) == 0:
            return []
        result = []
        for user_history in self.users_history:
            users_intersection = set(user_history)&curr_user_history
            degree = len(users_intersection)/len(curr_user_history)
            if degree >= 0.5:
                result.append(user_history)
        return result

    def collect_movies(self,similar_users: list[list[int]]) -> dict[int,int]:

        """Собирает все фильмы в 1 словарь, где ключ - id фильма, значение - количество просмотров среди всех пользователей"""

        popularity = dict()
        for user in similar_users:
            for film in user:
                if film not in popularity:
                    popularity[film] = 1
                else:
                    popularity[film] += 1
        return popularity

    def exclude_watched_movies(self, popularity: dict[int, int], curr_user_history: list[int]) -> dict[int,int]:

        """Убирает из списка популярности фильмы уже посмотренные пользователем"""

        for film in set(curr_user_history):
            if film in popularity:
                popularity.pop(film)

        return popularity

    def find_most_popular(self, popularity: dict[int, int]) -> int | None:

        """Находит индекс самого популярного фильма среди оставшихся"""

        if len(popularity) == 0:
            return None
        else:
            curr_max = -1
            most_popular_film = -1
            for film in popularity:
                if popularity[film] > curr_max:
                    curr_max = popularity[film]
                    most_popular_film = film
        return most_popular_film

    def recommend(self, curr_user_history: list[int]) -> str | None:

        """Собирает все методы воедино и выдает рекомендациюю"""

        similar_users = self.find_similar_users(curr_user_history)
        popularity = self.collect_movies(similar_users)
        filtered_popularity = self.exclude_watched_movies(popularity,curr_user_history)
        most_popular_film = self.find_most_popular(filtered_popularity)
        if most_popular_film is None:
            return None
        movie = self.film_catalog[most_popular_film]
        return movie.title


