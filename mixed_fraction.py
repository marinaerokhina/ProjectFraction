from __future__ import annotations
from fraction import Fraction


class MixedFraction(Fraction):
    
    
    whole_part: int
    frac_part: Fraction

    def __init__(self, wp: int = 0, num: int = 0, den: int = 1):
        if not isinstance(wp, int):
            raise TypeError("Whole part must be integer")
        self.whole_part = wp
        self.frac_part = Fraction(num, den)

    def __str__(self) -> str:
        """
        MixedFraction to str
        :return: str
        """
        if self.whole_part == 0:
            return f"{super().__str__()}"
        else:
            return f"{self.whole_part} {self.frac_part.num}/{self.frac_part._den}"

    @staticmethod
    def to_fraction(frac) -> Fraction:
        """
        MixedFraction turns to Fraction
        :param frac: MixedFraction
        :return: Fraction
        """
        if not isinstance(frac, MixedFraction):
            raise TypeError("Argument must be a MixedFraction")
        if frac.whole_part == 0:
            return Fraction(frac.frac_part.num, frac.frac_part._den)
        else:
            return Fraction(frac.whole_part * frac.frac_part._den + frac.frac_part.num,
                            frac.frac_part._den)

    @staticmethod
    def to_mixed_fraction(frac:Fraction) -> MixedFraction:
        """
        Fraction turs into MixedFraction
        :param frac: Fraction
        :return: MixedFraction
        """
        if not isinstance(frac, Fraction):
            raise TypeError("Argument must be a Fraction")
        if frac.num < frac._den:
            wp = 0
            num = frac.num
            den = frac._den
        elif frac.num == frac._den:
            wp = 1
            num = 0
            den = frac._den
        else:
            wp = frac.num // frac._den
            num = frac.num % frac._den
            den = frac._den
        return MixedFraction(wp, num, den)

    def __eq__(self, other) -> bool:
        """
        MixedFraction comparison method (Does MixedFraction_1 equal MixedFraction_2?)
        :param other: MixedFraction or Fraction
        :return: bool
        """
        frac, frac2 = Fraction(), Fraction()
        if isinstance(self,  MixedFraction):
            frac = MixedFraction.to_fraction(self)
        if isinstance(other, MixedFraction):
            frac2 = MixedFraction.to_fraction(other)
        return frac.__eq__(frac2)

    def __gt__(self, other) -> bool:
        """
        MixedFraction comparison method (Does MixedFraction_1 greater then MixedFraction_2?)
        :param other: MixedFraction or Fraction
        :return: bool
        """
        frac, frac2 = Fraction(), Fraction()
        if isinstance(self, MixedFraction):
            frac = MixedFraction.to_fraction(self)
        if isinstance(other, MixedFraction):
            frac2 = MixedFraction.to_fraction(other)
        return frac.__gt__(frac2)

    def __lt__(self, other) -> bool:
        """
        MixedFraction comparison method (Does MixedFraction_1 less then MixedFraction_2?)
        :param other: MixedFraction or Fraction
        :return: bool
        """
        frac, frac2 = Fraction(), Fraction()
        if isinstance(self,  MixedFraction):
            frac = MixedFraction.to_fraction(self)
        if isinstance(other, MixedFraction):
            frac2 = MixedFraction.to_fraction(other)
        return frac.__lt__(frac2)

    def __add__(self, other) -> MixedFraction:
        """
        Fraction adding method
        :param other: MixedFraction or Fraction
        :return: MixedFraction
        """
        if not isinstance(other, (MixedFraction, Fraction)):
            raise TypeError("Argument must be a MixedFraction of a Fraction")
        frac = self
        frac1 = MixedFraction.to_fraction(frac)
        frac2 = MixedFraction.to_fraction(other) if isinstance(other, MixedFraction) else other
        res = frac1 + frac2
        return MixedFraction.to_mixed_fraction(res)

    def __sub__(self, other) -> MixedFraction:
        """
        Fraction substracting method
        :param other: MixedFraction or Fraction
        :return: MixedFraction
        """
        if not isinstance(other, (MixedFraction, Fraction)):
            raise TypeError("Argument must be a MixedFraction of a Fraction")
        frac = self
        frac1 = MixedFraction.to_fraction(frac)
        frac2 = MixedFraction.to_fraction(other) if isinstance(other, MixedFraction) else other
        res = frac1 - frac2
        return MixedFraction.to_mixed_fraction(res)

    def __mul__(self, other) -> MixedFraction:
        """
        Fraction multiplying method
        :param other: MixedFraction or Fraction
        :return: MixedFraction
        """
        if not isinstance(other, (MixedFraction, Fraction)):
            raise TypeError("Argument must be a MixedFraction of a Fraction")
        frac = self
        frac1 = MixedFraction.to_fraction(frac)
        frac2 = MixedFraction.to_fraction(other) if isinstance(other, MixedFraction) else other
        res = frac1 * frac2
        return MixedFraction.to_mixed_fraction(res)

    def __truediv__(self, other) -> MixedFraction:
        """
        Fraction dividing method
        :param other: MixedFraction or Fraction
        :return: MixedFraction
        """
        if not isinstance(other, (MixedFraction, Fraction)):
            raise TypeError("Argument must be a MixedFraction of a Fraction")
        frac = self
        frac1 = MixedFraction.to_fraction(frac)
        frac2 = MixedFraction.to_fraction(other) if isinstance(other, MixedFraction) else other
        res = frac1 / frac2
        return MixedFraction.to_mixed_fraction(res)
    
    def __pow__(self, power) -> MixedFraction:
        """
        Fraction raising to degree method
        :param power: int
        :return: MixedFraction
        """
        if not isinstance(power, int):
            raise TypeError("Argument must be an integer")
        frac = self
        frac1 = MixedFraction.to_fraction(frac)
        res = frac1 ** power
        return MixedFraction.to_mixed_fraction(res)

    @staticmethod
    def read_from_text_file(filename) -> MixedFraction:
        """
        Reading method (for text files)
        :param filename: str
        :return: MixedFraction
        """
        with open(filename, 'r') as file:
            wp = int(input())
            fr_pt = super().read_from_text_file()
            return MixedFraction(wp, fr_pt.num, fr_pt._den)
    
    def write_to_text_file(self, filename):
        """
        Writing method (for text files)
        :param filename: str
        :return: None
        """
        with open(filename, 'w') as file:
            file.write(self.__str__())
        
    @staticmethod
    def read_from_binary_file(filename) -> MixedFraction:
        """
        Reading metod (for binary files)
        :param filename: str
        :return: MixedFraction
        """
        with open(filename, 'rb') as file:
            bdata = file.read()
            wp, num, den = struct.unpack('iii', bdata)
            return MixedFraction(wp, num, den)
    
    def write_to_binary_file(self, filename):
        """
        Writing method (for binary files)
        :param filename: str
        :return: None
        """
        with open(filename, 'wb') as file:
            bdata = struct.pack('iii', self.whole_part, self.frac_part.num, self.frac_part._den)
            file.write(bdata)
        
