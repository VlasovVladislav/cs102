"""Набор тестов для алгоритма распределения по группам. """

import unittest

from src.lab4part2.models import Respondent
from src.lab4part2.models import AgeGroups
from src.lab4part2.models import AgeGroup



class GroupsTestCase(unittest.TestCase):
    """Тесты для классов Respondent, AgeGroup и AgeGroups."""

    def setUp(self):
        self.age_group = AgeGroup(0,18,[])
        self.age_groups = AgeGroups([18, 25])

    def test_contains_true(self):
        """Проверяет, что возраст внутри границ группы распознаётся корректно."""
        self.assertTrue(self.age_group.contains(0))
        self.assertTrue(self.age_group.contains(18))

    def test_contains_false(self):
        """Проверяет, что возраст за пределами группы не принадлежит ей."""
        self.assertFalse(self.age_group.contains(40))
        self.assertFalse(self.age_group.contains(-1))

    def test_add_respondent(self):
        """Проверяет добавление респондента в подходящую возрастную группу."""
        respondent = Respondent('Владислав Власов',15)
        self.age_group.add_respondent(respondent)
        self.assertEqual(self.age_group.respondents,[respondent])

    def test_add_respondent_out_of_range(self):
        """Проверяет, что респондент неподходящего возраста не добавляется в группу."""
        respondent = Respondent('Старостин Ростислав Ермолаевич',28)
        self.age_group.add_respondent(respondent)
        self.assertEqual(self.age_group.respondents, [])

    def test_sort_respondents(self):
        """Проверяет сортировку респондентов по убыванию возраста и имени."""
        respondent1 = Respondent('Волков Ростислав Ермолаевич', 6)
        respondent2 = Respondent('Старостин Петр Афанасьевич', 6)
        respondent3 = Respondent('Залуцкий Антон Владимирович', 3)
        self.age_group.add_respondent(respondent1)
        self.age_group.add_respondent(respondent2)
        self.age_group.add_respondent(respondent3)
        self.age_group.sort_respondents()
        self.assertEqual(self.age_group.respondents,[respondent1,respondent2,respondent3])

    def test_create_groups(self):
        """Проверяет создание возрастных групп с правильными границами."""
        self.assertEqual(len(self.age_groups.groups),3)
        self.assertEqual(self.age_groups.groups[0].min_age, 0)
        self.assertEqual(self.age_groups.groups[0].max_age,18)
        self.assertEqual(self.age_groups.groups[1].min_age, 19)
        self.assertEqual(self.age_groups.groups[1].max_age, 25)
        self.assertEqual(self.age_groups.groups[2].min_age, 26)
        self.assertEqual(self.age_groups.groups[2].max_age, None)

    def test_check_boundaries(self):
        """Проверяет отклонение некорректных границ возрастных групп."""
        with self.assertRaises(ValueError):
            self.wrong_group = AgeGroups([25, 18])
        with self.assertRaises(ValueError):
            self.wrong_group = AgeGroups([18, 18, 25])

    def test_add_respondents(self):
        """Проверяет распределение респондентов по соответствующим возрастным группам."""
        respondent1 = Respondent('Волков Ростислав Ермолаевич', 15)
        respondent2 = Respondent('Старостин Петр Афанасьевич', 22)
        respondent3 = Respondent('Залуцкий Антон Владимирович', 30)
        self.current_age_group = AgeGroups([18,22,30])
        self.current_age_group.add_respondent(respondent1)
        self.current_age_group.add_respondent(respondent2)
        self.current_age_group.add_respondent(respondent3)
        self.assertEqual(self.current_age_group.groups[0].respondents,[respondent1])
        self.assertEqual(self.current_age_group.groups[1].respondents, [respondent2])
        self.assertEqual(self.current_age_group.groups[2].respondents, [respondent3])

    def test_get_non_empty_groups(self):
        """Проверяет получение непустых групп в порядке от старшей к младшей."""
        age_groups = AgeGroups([18, 25, 30])

        respondent1 = Respondent('Волков Ростислав Ермолаевич', 15)
        respondent2 = Respondent('Старостин Петр Афанасьевич', 22)
        respondent3 = Respondent('Залуцкий Антон Владимирович', 28)

        age_groups.add_respondent(respondent1)
        age_groups.add_respondent(respondent2)
        age_groups.add_respondent(respondent3)

        result = age_groups.get_non_empty_groups()

        self.assertEqual(len(result), 3)
        self.assertEqual(result[0].respondents, [respondent3])
        self.assertEqual(result[1].respondents, [respondent2])
        self.assertEqual(result[2].respondents, [respondent1])
