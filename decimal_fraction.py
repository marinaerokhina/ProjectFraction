from __future__ import annotations
from fraction import Fraction


class DecimalFraction(Fraction):
    value: float

    def __init__(self, val):
        if isinstance(val, Fraction):
            self.value = val.__float__()
        elif isinstance(val, float):
            self.value = val
        else:
            self.value = float(val)

    @classmethod
    def to_fraction(cls, val) -> Fraction:
        val_str = str(val)
        n = len(val_str) - 1 - val_str.index('.')
        num = int(val * 10 ** n)
        return Fraction(num, 10 ** n)
