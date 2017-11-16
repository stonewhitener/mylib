import math


class Fraction:
    """
    ================================================================
    Initialize
    ================================================================
    >>> Fraction(3, 4)
    3/4
    >>> Fraction(3, -4)
    -3/4
    >>> Fraction(3)
    3

    ================================================================
    Addition, subtraction
    ================================================================
    >>> Fraction(1, 2) + Fraction(2, 3)
    7/6
    >>> Fraction(1, 2) - Fraction(2, 3)
    -1/6

    ================================================================
    Multiplication, division
    ================================================================
    >>> Fraction(2, 3) * Fraction(5, 2)
    5/3
    >>> Fraction(2, 3) / Fraction(5, 2)
    4/15

    ================================================================
    Power
    ================================================================
    >>> Fraction(-1, 2) ** 2
    1/4
    >>> Fraction(-1, 2) ** -1
    -2
    >>> Fraction(-1, 2) ** -2
    4
    >>> Fraction(-1, 2) ** 0
    1
    """

    def __init__(self, numerator, denominator=1):
        self.sign = self.__sign(numerator, denominator)
        numerator = abs(numerator)
        denominator = abs(denominator)
        gcd = math.gcd(numerator, denominator)
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd

    @staticmethod
    def __sign(a, b):
        assert type(a) == type(b) == int
        return -1 if (a > 0) ^ (b > 0) else 1

    @staticmethod
    def __reduce(a, b):
        assert type(a) == type(b) == Fraction
        gcd = math.gcd(a.denominator, b.denominator)
        x = a.denominator // gcd
        y = b.denominator // gcd
        return a.sign * a.numerator * y, b.sign * b.numerator * x, a.denominator * y

    def __eq__(self, other):
        if type(other) == int:
            other = Fraction(other)
        return self.sign == other.sign and self.denominator == other.denominator and self.numerator == other.numerator

    def __lt__(self, other):
        if type(other) == int:
            other = Fraction(other)
        return float(self) < float(other)

    def __gt__(self, other):
        if type(other) == int:
            other = Fraction(other)
        return float(self) > float(other)

    def __pos__(self):
        return Fraction(self.sign * self.numerator, self.denominator)

    def __neg__(self):
        return Fraction(-self.sign * self.numerator, self.denominator)

    def __add__(self, other):
        if type(other) == int:
            other = Fraction(other)
        a, b, d = self.__reduce(self, other)
        return Fraction(a + b, d)

    __radd__ = __add__

    def __sub__(self, other):
        if type(other) == int:
            other = Fraction(other)
        a, b, d = self.__reduce(self, other)
        return Fraction(a - b, d)

    def __rsub__(self, other):
        if type(other) == int:
            other = Fraction(other)
        a, b, d = self.__reduce(other, self)
        return Fraction(a - b, d)

    def __mul__(self, other):
        if type(other) == int:
            other = Fraction(other)
        return Fraction(self.sign * other.sign * self.numerator * other.numerator, self.denominator * other.denominator)

    __rmul__ = __mul__

    def __truediv__(self, other):
        if type(other) == int:
            other = Fraction(other)
        return self * other ** -1

    def __rtruediv__(self, other):
        if type(other) == int:
            other = Fraction(other)
        return other * self ** -1

    __floordiv__ = __truediv__
    __rfloordiv__ = __rtruediv__

    def __pow__(self, exponent):
        if exponent > 0:
            return Fraction((self.sign * self.numerator) ** exponent, self.denominator ** exponent)
        if exponent == 0:
            return Fraction(1)
        if exponent < 0:
            exponent = abs(exponent)
            return Fraction((self.sign * self.denominator) ** exponent, self.numerator ** exponent)

    def __rpow__(self, other):
        return Fraction(other ** float(self))

    def __float__(self):
        return self.sign * self.numerator / self.denominator

    def __int__(self):
        return int(float(self))

    def __str__(self):
        if self.denominator == 1:
            return str(self.sign * self.numerator)
        else:
            return f'{self.sign * self.numerator}/{self.denominator}'

    __repr__ = __str__
