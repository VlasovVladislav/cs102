"""Набор тестов для алгоритма рекомендаций. """

import unittest

from src.lab4.recommender import RecommendationSystem
from src.lab4.models import Movie


class RecommenderTestCase(unittest.TestCase):
    """ Тесты """

    def setUp(self):
        film_catalog = {
            1: Movie(1, "Мстители: Финал"),
            2: Movie(2, "Хатико"),
            3: Movie(3, "Дюна"),
            4: Movie(4, "Унесенные призраками")
        }

        users_history = [
            [2, 1, 3],
            [1, 4, 3],
            [2, 2, 2, 2, 2, 3]
        ]

        self.system = RecommendationSystem(film_catalog, users_history)

    def test_find_similar_users_empty_history(self):
        self.assertEqual(self.system.find_similar_users([]), [])

    def test_find_similar_users(self):
        self.assertEqual(self.system.find_similar_users([2, 4]), [[2, 1, 3], [1, 4, 3], [2, 2, 2, 2, 2, 3]])

    def test_collect_movies(self):
        self.assertEqual(self.system.collect_movies(self.system.users_history),{2: 6, 1: 2, 3: 3, 4: 1})

    def test_exclude_watched_movies(self):
        self.assertEqual(self.system.exclude_watched_movies({2: 6, 1: 2, 3: 3, 4: 1},[2,4]),{1: 2, 3: 3})

    def test_find_most_popular(self):
        self.assertEqual(self.system.find_most_popular({2: 6, 1: 2, 3: 3, 4: 1}),2)

    def test_recommend(self):
        self.assertEqual(self.system.recommend([2,4]),'Дюна')