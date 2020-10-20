import pytest

from python.calc import Calc


class TestCalc:
    def setup(self):
        self.calc = Calc()
        # setup：在一个类中最先被调用的函数，无论位置在哪儿

    def test_add_1(self):
        # self.calc = Calc()
        result = self.calc.add(1, 2)
        print(result)
        assert 3 == result

    def test_div(self):
        # self.calc = Calc()
        result = self.calc.div(8,4)
        print(result)
        assert 2.0 == result


if __name__ == '__main__':
    pytest.main(['-vs', 'test_pytest.py::TestCalc::test_add_1'])
    # tip1.这样写main语句实际上想要执行一条用例，但是还是执行了两条，需要把编译器换成python的，不要用pytest的，就是edit configurations选项
    # tip2.main函数里面的参数必须传入字符串列表，用[]就表示list列表
    # tip3.if __name__ == '__main__' 是python的入口函数

