import time
import pytest
import task_7_6
import sys
sys.path.append('..')

from common_functions import check_function_exists, check_function_params


def test_func_created():
    '''Проверяем, что декоратор создан'''
    check_function_exists(task_7_6, 'total_order')


def test_total_order_exception():
    with pytest.raises(ValueError) as excinfo:
        @task_7_6.total_order
        class DoThing:
            pass

def test_total_order_methods():
    @task_7_6.total_order
    class DoThing:
        def __init__(self, num):
            self.num = num

        def __eq__(self, other):
            return self.num == other.num

        def __lt__(self, other):
            return self.num < other.num

    small_num = DoThing(1)
    big_num = DoThing(100)

    assert small_num < big_num
    assert small_num <= big_num
    assert not small_num > big_num
    assert not small_num >= big_num
    assert small_num != big_num
