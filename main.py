from fraction import Fraction
from decimal_fraction import DecimalFraction
from mixed_fraction import MixedFraction
from tree import Node, Tree

try:
    Frac1 = MixedFraction(2, 3, 4)
    Frac2 = MixedFraction(3, 5, 8)
    print(Frac1, Frac2)
    Frac3 = Fraction(14, 8)
    Frac4 = Fraction(34, 7)
    print(Frac3, Frac4)
    tree = Tree()
    tree.insert(Frac1)
    tree.print_tree()
    print("\n")
    tree.insert(Frac2)
    tree.print_tree()
    print("\n")
    tree.insert(Frac3)
    tree.print_tree()
    print("\n")
    tree.insert(Frac4)
    tree.print_tree()
    print("\n")
    tree.balance()
    tree.print_tree()
    print("\n")
    tree.insert(Fraction(9, 4))
    tree.balance()
    tree.print_tree()
    print("\n")
except Exception as e:
    print(f"There's an error occured: {e}. Please, be careful")

"""    frac1 = Fraction(5, 125)
    print(frac1)
    frac2 = Fraction.frac_input()
    print(frac2)
    print (f"sum = {frac1 + frac2}, sub = {frac1 - frac2}, mul = {frac1 * frac2}, "
           f"div = {frac1 / frac2}")
    print(float(frac2))
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
    frac7 = float(input())
    frac8 = DecimalFraction.to_fraction(frac7)
    print(frac8)"""
