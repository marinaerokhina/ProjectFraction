from fraction import Fraction

try:
    frac1 = Fraction(5, 125)
    print(frac1)
    frac2 = Fraction.frac_input()
    print(frac2)
    print (f"sum = {frac1 + frac2}, sub = {frac1 - frac2}, mul = {frac1 * frac2}, "
           f"div = {frac1 / frac2}")
    print(frac2.__float__())
    frac3 = Fraction.read_from_text_file("input.txt")
    print(frac3)
    frac4 = Fraction.frac_input()
    print(frac4)
    print(frac3.__gt__(frac4), frac3.__lt__(frac4))
    frac5 = frac3 + frac4 - frac1 + frac2**3
    frac5.write_to_text_file("output.txt")
    frac5.write_to_binary_file("input.bin")
    frac6 = Fraction.read_from_binary_file("input.bin")
    print(frac5, frac6, frac5.__eq__(frac6))
except Exception as e:
    print(f"There's an error occured: {e}. Please, be careful")