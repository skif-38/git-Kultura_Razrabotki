import sys
sys.path.append("../src")
import math_demo as md

def test_addition():
    assert md.add(2, 2) == 4, "Addition didnt return 4"
    print("Succesful addition test")

def test_addition_with_bug():
    assert md.add_with_bug(2, 2) == 4, "Bagged addition didnt return 4"
    assert md.add_with_bug(0, 0) == 0, "Bagged addition didnt return 0"
    # assert md.add_with_bug(6, 7) == 13, "Bagged addition didnt return 13"
    print("Succesful bugged addition test")

def test_addition_duplicated():
    assert md.add(2, 3) == 2 + 3

# def test_addition_overcomplicated():
#     for i in range(0, 2**32):
#         for j in range(0, 2**32):
#             assert md.add(i, j) == sum([i, j])
#             assert md.add(-i, j) == sum([-i, j])
#             assert md.add(i, -j) == sum([i, -j])
#             assert md.add(-i, -j) == sum([-i, -j])

def test_addition_reasonable():
    assert md.add(2, 2) == 4
    assert md.add(0, 0) == 0
    assert md.add(6, 7) == 13
    assert md.add(-6, -7) == -13
    assert md.add(6, -7) == -1
    assert md.add(-7, 0) == -7
    assert md.add(7, 0) == 7
    print("Succesfull reasonable test")
print('Vitalya')

def test_tax_calculate_with_bag():
    assert md.calculate_tax_with_bug(1000) == 150
    assert md.calculate_tax_with_bug(100) == 15
    assert md.calculate_tax_with_bug(10) == 1.5
    assert md.calculate_tax_with_bug(1) == 0.15
    assert md.calculate_tax_with_bug(245) == 36.75
    print("Succesful caculate tax with bag test")

def test_tax_calculate():
    assert md.calculate_tax(1000) == 150
    assert md.calculate_tax(100) == 15
    assert md.calculate_tax(10) == 1.5
    assert md.calculate_tax(1) == 0.15
    assert md.calculate_tax(24.5) == 3.67
    print("Succesful caculate tax test")

if __name__ == "__main__":
    test_addition()
    test_addition_with_bug()
    test_addition_duplicated()
    # test_addition_overcomplicated()
    test_addition_reasonable()
    test_tax_calculate_with_bag()
    test_tax_calculate()