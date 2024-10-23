from Python_course.py_advanced.HW6.task1.functions import find_palindroms, find_solution_roots, ssd_models_checker
import pytest

TEST_DATA = {
    'Test1':[
        {'a': 3, 'b': 3, 'c': 5},
        {'a': 1, 'b': 8, 'c': 15},
        {'a': 1, 'b': -13, 'c': 12},
        {'a': 1, 'b': 1, 'c': 1},
    ],
    'Test2':[
        {'a': 1, 'b': 8, 'c': 15},
        {'a': 1, 'b': -13, 'c': 12},
        {'a': -4, 'b': 28, 'c': -49},
    ],
    'Test3':[
        {'models':['480 ГБ 2.5" SATA накопитель Kingston A400', '500 ГБ 2.5" SATA накопитель Samsung 870 EVO',
              '480 ГБ 2.5" SATA накопитель ADATA SU650', '240 ГБ 2.5" SATA накопитель ADATA SU650',
              '250 ГБ 2.5" SATA накопитель Samsung 870 EVO', '256 ГБ 2.5" SATA накопитель Apacer AS350 PANTHER',
              '480 ГБ 2.5" SATA накопитель WD Green', '500 ГБ 2.5" SATA накопитель WD Red SA500'],
         'available': [1, 1, 1, 1, 0, 1, 1, 0], 'manufacturers': ['Intel', 'Samsung', 'WD']}
    ],
    'Test4': [{'phrases': ["нажал кабан на баклажан", "дом как комод", "рвал дед лавр", "азот калий и лактоза",
                          "а собака боса", "тонет енот", "карман мрак", "пуст суп"]}

              ],
    'Test5': [{'phrases': ["нажал кабан на баклажан", "дом как комод", "рвал дед лавр", "азот калий и лактоза",
                           "а собака боса", "тонет енот", "карман мрак", "пуст суп"], 'result': 6},
              {'phrases': ["а роза упала на лапу азора", "люблю грозу в начале мая", "не гни папин ген", "все наоборот",
                           "нажал кабан на баклажан", "верной дорогой идете"], 'result': 3}
              ]
}
class TestCases:
    @pytest.mark.parametrize('testdata', TEST_DATA['Test1'])
    def test_root_triangles(self, testdata):
        assert find_solution_roots(testdata['a'], testdata['b'], testdata['c']) != 'корней нет'

    @pytest.mark.parametrize('testdata', TEST_DATA['Test2'])
    def test_multi_roots(self, testdata):
        solutions = []
        solution = find_solution_roots(testdata['a'], testdata['b'], testdata['c'])
        if not isinstance(solution, tuple):
            solutions.append(solution)
        else:
            solutions = solution
        assert len(solutions) == 2

    @pytest.mark.parametrize('testdata', TEST_DATA['Test3'])
    def test_models_check(self, testdata):
        assert (ssd_models_checker(testdata['models'], testdata['available'], testdata['manufacturers']) ==
                (['500 ГБ 2.5" SATA накопитель Samsung 870 EVO', '480 ГБ 2.5" SATA накопитель WD Green'], 2))

    @pytest.mark.parametrize('testdata', TEST_DATA['Test4'])
    def test_palidroms(self, testdata):
        assert find_palindroms(testdata['phrases']) == ["нажал кабан на баклажан", "рвал дед лавр", "азот калий и лактоза",
               "а собака боса", "тонет енот", "пуст суп"]

    @pytest.mark.parametrize('testdata', TEST_DATA['Test5'])
    def test_palidroms_count(self, testdata):
        assert len(find_palindroms(testdata['phrases'])) == testdata['result']