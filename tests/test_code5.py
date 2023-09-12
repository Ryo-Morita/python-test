# src/code.pyのtestをtestクラスで実施する
from src import code

class Test_sum_numbers(object):
    def test_sum_numbers(self):
        assert code.sum_numbers(1,2) == 3