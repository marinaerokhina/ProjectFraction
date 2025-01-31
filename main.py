from fraction import Fraction
from decimal_fraction import DecimalFraction
from mixed_fraction import MixedFraction

try:
    frac1 = Fraction(5, 125)
    print(frac1)
    frac2 = Fraction.frac_input()
    print(frac2)
    print (f"sum = {frac1 + frac2}, sub = {frac1 - frac2}, mul = {frac1 * frac2}, "
           f"div = {frac1 / frac2}")
    print(float(frac2))
    frac7 = float(input())
    frac8 = DecimalFraction.to_fraction(frac7)
    print(frac8)
    Frac1 = MixedFraction(2, 3, 4)
    print(Frac1)
except Exception as e:
    print(f"There's an error occured: {e}. Please, be careful")

"""    frac3 = Fraction.read_from_text_file("input.txt")
    print(frac3)
    frac4 = Fraction.frac_input()
    print(frac4)
    print(frac3.__gt__(frac4), frac3.__lt__(frac4))
    frac5 = frac3 + frac4 - frac1 + frac2**3
    frac5.write_to_text_file("output.txt")
    frac5.write_to_binary_file("input.bin")
    frac6 = Fraction.read_from_binary_file("input.bin")
    print(frac5, frac6, frac5.__eq__(frac6)) """