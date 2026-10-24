"""Набор тестов для судоку. """

import unittest

from src.lab3 import sudoku


class SudokuTestCase(unittest.TestCase):
    """ Тесты """
    def test_group(self):
        self.assertEqual(sudoku.group([3,8,5,6,2,4,5,6,8], 3),[[3,8,5],[6,2,4],[5,6,8]])

    def setUp(self):
        """Общая тестовая сетка для всех тестов"""
        self.test_grid = [
            ['0', '1', '2', '3', '4', '5', '6', '7', '8'],
            ['1', '2', '3', '4', '5', '6', '7', '8', '0'],
            ['2', '3', '4', '5', '6', '7', '8', '0', '1'],
            ['3', '4', '5', '6', '7', '8', '0', '1', '2'],
            ['4', '5', '6', '7', '8', '0', '1', '2', '3'],
            ['5', '6', '7', '8', '0', '1', '2', '3', '4'],
            ['6', '7', '8', '0', '1', '2', '3', '4', '5'],
            ['7', '8', '0', '1', '2', '3', '4', '5', '6'],
            ['8', '0', '1', '2', '3', '4', '5', '6', '7']
        ]

        self.test_grid_with_empty_pos = [
            ['0', '1', '2', '.', '4', '5', '6', '7', '8'],
            ['1', '2', '3', '4', '5', '6', '7', '8', '0'],
            ['2', '3', '4', '5', '.', '7', '8', '0', '1'],
            ['3', '4', '5', '6', '7', '8', '0', '1', '2'],
            ['4', '5', '6', '7', '8', '.', '1', '2', '3'],
            ['5', '6', '.', '8', '0', '1', '2', '.', '4'],
            ['6', '7', '8', '0', '.', '2', '3', '4', '5'],
            ['7', '8', '.', '1', '2', '.', '4', '5', '6'],
            ['8', '0', '1', '2', '3', '4', '5', '6', '7']
        ]

    def test_get_row(self):
        self.assertEqual(sudoku.get_row(self.test_grid,(1,0)), ['1', '2', '3', '4', '5', '6', '7', '8', '0'])

    def test_get_col(self):

        self.assertEqual(sudoku.get_col(self.test_grid,(0,2)),['2', '3', '4', '5', '6', '7', '8', '0', '1'])

    def test1_get_block(self):

        self.assertEqual(sudoku.get_block(self.test_grid,(0,0)),['0', '1', '2', '1', '2', '3', '2', '3', '4'] )

    def test2_get_block(self):
        self.assertEqual(sudoku.get_block(self.test_grid, (4, 4)), ['6', '7', '8', '7', '8', '0', '8', '0', '1'])

    def test_none_find_empty_pos(self):
        self.assertEqual(sudoku.find_empty_positions(self.test_grid),None)

    def test_find_empty_pos(self):
        self.assertEqual(sudoku.find_empty_positions(self.test_grid_with_empty_pos), (0,3))


    def test_find_possible_values(self):
        self.assertEqual(sudoku.find_possible_values(self.test_grid_with_empty_pos,(0,3)),{'3', '9'})

    def test_solve_without_solve(self):
        test_grid_without_solve = [
            ['0', '1', '2', '.', '5', '5', '5', '5', '5'],
            ['1', '2', '3', '4', '5', '6', '7', '8', '0'],
            ['2', '3', '4', '5', '.', '7', '8', '0', '1'],
            ['3', '4', '5', '6', '7', '8', '0', '1', '2'],
            ['4', '5', '6', '7', '8', '.', '1', '2', '3'],
            ['5', '6', '.', '8', '0', '1', '2', '.', '4'],
            ['6', '7', '8', '0', '.', '2', '3', '4', '5'],
            ['7', '8', '.', '1', '2', '.', '4', '5', '6'],
            ['8', '0', '1', '2', '3', '4', '5', '6', '7']
        ]
        result = sudoku.solve(test_grid_without_solve)
        self.assertIsNone(result)

    def test_solve_empty(self):
        empty_grid = [['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
                      ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
                      ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
                      ['.', '.', '.', '.', '.', '.', '.', '.', '.'], ['.', '.', '.', '.', '.', '.', '.', '.', '.'],
                      ['.', '.', '.', '.', '.', '.', '.', '.', '.']]
        result = sudoku.solve(empty_grid)
        is_valid = sudoku.check_solution(result)
        self.assertTrue(is_valid)

    def test_generate_sudoku_empty(self):
        empty_grid = [['.'] * 9 for _ in range(9)]
        self.assertEqual(sudoku.generate_sudoku(0), empty_grid)

    def test_generate_sudoku_full(self):
        result = sudoku.generate_sudoku(81)
        has_dots = any(e == '.' for row in result for e in row)
        self.assertFalse(has_dots)