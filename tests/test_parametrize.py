import pytest


class TestParametrize:

    def factorial(self, n: int) -> int:
        if n < 0:
            raise ValueError("n must be a non-negative integer")
        if n == 0:
            return 1
        else:
            return n * self.factorial(n - 1)

    def test_factorial_0(self):
        assert self.factorial(0) == 1

    def test_factorial_1(self):
        assert self.factorial(1) == 1

    def test_factorial_2(self):
        assert self.factorial(2) == 2

    def test_factorial_3(self):
        assert self.factorial(3) == 6

    def test_factorial_4(self):
        assert self.factorial(4) == 24

    def test_factorial_5(self):
        assert self.factorial(5) == 120

    def test_factorial_6(self):
        assert self.factorial(6) == 720

    # @pytest.mark.parametrize(
    #     "n, expected_factorial",
    #     [
    #         (0, 1),
    #         (1, 1),
    #         (2, 2),
    #         (3, 6),
    #         (4, 24),
    #         (5, 120),
    #         (6, 720)
    #     ],
    # )
    # @pytest.mark.parametrize('value, expected_factorial', FACTORIAL)
    # @pytest.mark.parametrize('value, expected_factorial', ((1, 1), (0, 1)), ids=['One', 'Zero'])
    def test_factorial(self, value, expected_factorial):
        assert self.factorial(value) == expected_factorial
