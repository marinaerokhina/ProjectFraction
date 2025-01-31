from __future__ import annotations
from fraction import Fraction

class MixedFraction(Fraction):
    whole_part:int
    frac_part:Fraction

    def __init__(self, wp:int = 0, num:int = 0, den:int = 1):
        if not isinstance(wp, int):
            raise TypeError("Whole part must be integer")
        self.whole_part = wp
        self.frac_part = Fraction(num, den)

    def __str__(self) -> str:
        if self.whole_part == 0:
            return f"{super().__str__()}"
        else:
            return f"{self.whole_part} {self.frac_part.num}/{self.frac_part._den}"
