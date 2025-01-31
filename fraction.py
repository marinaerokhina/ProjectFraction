from __future__ import annotations
import math
import struct


class Fraction:
    num: int  # numerator
    _den: int  # denominator

    def __init__(self, num: int = 0, den: int = 1):
        if not isinstance(den, int):
            raise TypeError("Denominator must be an integer")
        if not isinstance(num, int):
            raise TypeError("Numerator must be an integer")
        if den == 0:
            raise ValueError("Denominator cannot be 0")
        elif num > 0 and den < 0:
            self.num *= -1
            self._den = abs(den)
        elif num < 0 and den < 0:
            self.num = abs(num)
            self._den = abs(den)
        else:
            self.num = num
            self._den = den
        self.red()

    @property
    def den(self) -> int:
        return self._den

    @den.setter
    def den(self, val):
        if not isinstance(val, int):
            raise TypeError("Denominator must be an integer")
        if val == 0:
            raise ValueError("Denominator cannot be 0")
        else:
            self._den = val

    def __str__(self) -> str:
        return str(f"{self.num}/{self._den}")

    def gcd(self, n, d) -> int:
        while d:
            n, d = d, n % d
        return abs(n)

    def red(self):
        val = self.gcd(self.num, self._den)
        self.num //= val
        self._den //= val

    def __add__(self, other: Fraction) -> Fraction:
        if not isinstance(other, Fraction):
            raise TypeError("Argument must be a fraction")
        new_den = self._den * other._den
        new_num = self.num * other._den + other.num * self._den
        return Fraction(new_num, new_den)

    def __sub__(self, other: Fraction) -> Fraction:
        if not isinstance(other, Fraction):
            raise TypeError("Argument must be a fraction")
        new_den = self._den * other._den
        new_num = self.num * other._den - other.num * self._den
        return Fraction(new_num, new_den)

    def __mul__(self, other: Fraction) -> Fraction:
        if not isinstance(other, Fraction):
            raise TypeError("Argument must be a fraction")
        new_num = self.num * other.num
        new_den = self._den * other._den
        return Fraction(new_num, new_den)

    def __truediv__(self, other: Fraction) -> Fraction:
        if not isinstance(other, Fraction):
            raise TypeError("Argument must be a fraction")
        if other.num == 0:
            raise ZeroDivisionError("Cannot divide by zero fraction")
        new_num = self.num * other._den
        new_den = self._den * other.num
        return Fraction(new_num, new_den)

    def __pow__(self, power: int) -> Fraction:
        if not isinstance(power, int):
            raise TypeError("Power must be an integer")
        new_num = self.num ** power
        new_den = self._den ** power
        return Fraction(new_num, new_den)

    def __float__(self) -> float:
        return float(self.num / self._den)

    def __eq__(self, other: Fraction) -> bool:
        return self.num == other.num and self._den == other._den

    def __gt__(self, other) -> bool:
        return self.num * other._den > other.num * self._den

    def __lt__(self, other) -> bool:
        return self.num * other._den < other.num * self._den

    @staticmethod
    def frac_input() -> Fraction:
        num, den = map(int, input().split('/'))
        return Fraction(num, den)

    @staticmethod
    def read_from_text_file(filename) -> Fraction:
        with open(filename, 'r') as file:
            num, den = map(int, file.read().strip().split('/'))
            return Fraction(num, den)

    def write_to_text_file(self, filename):
        with open(filename, 'w') as file:
            file.write(self.__str__())

    @staticmethod
    def read_from_binary_file(filename) -> Fraction:
        with open(filename, 'rb') as file:
            bdata = file.read()
            num, den = struct.unpack('ii', bdata)
            return Fraction(num, den)

    def write_to_binary_file(self, filename):
        with open(filename, 'wb') as file:
            bdata = struct.pack('ii', self.num, self._den)
            file.write(bdata)
