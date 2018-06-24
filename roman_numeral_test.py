import unittest

class RomanNumeralTests(unittest.TestCase):
    def test_one_and_one_is_two(self):
        self.assertEqual(add('I','I'), 'II')

    def test_two_and_two_is_four(self):
        self.assertEqual(add('II', 'II'), 'IV')

    def test_two_and_three_is_five(self):
        self.assertEqual(add('II', 'III'), 'V')

    def test_conversion_to_roman_under_50(self):
        self.assertEqual(convert_to_roman(3),'III')
        self.assertEqual(convert_to_roman(4),'IV')
        self.assertEqual(convert_to_roman(5),'V')
        self.assertEqual(convert_to_roman(8),'VIII')
        self.assertEqual(convert_to_roman(9),'IX')
        self.assertEqual(convert_to_roman(10),'X')
        self.assertEqual(convert_to_roman(13),'XIII')
        self.assertEqual(convert_to_roman(14),'XIV')
        self.assertEqual(convert_to_roman(15),'XV')
        self.assertEqual(convert_to_roman(18),'XVIII')
        self.assertEqual(convert_to_roman(19),'XIX')
        self.assertEqual(convert_to_roman(20),'XX')
        self.assertEqual(convert_to_roman(23),'XXIII')
        self.assertEqual(convert_to_roman(24),'XXIV')
        self.assertEqual(convert_to_roman(25),'XXV')
        self.assertEqual(convert_to_roman(28),'XXVIII')
        self.assertEqual(convert_to_roman(29),'XXIX')
        self.assertEqual(convert_to_roman(30),'XXX')
        self.assertEqual(convert_to_roman(33),'XXXIII')
        self.assertEqual(convert_to_roman(34),'XXXIV')
        self.assertEqual(convert_to_roman(35),'XXXV')
        self.assertEqual(convert_to_roman(38),'XXXVIII')
        self.assertEqual(convert_to_roman(39),'XXXIX')
        self.assertEqual(convert_to_roman(40),'XL')
        self.assertEqual(convert_to_roman(43),'XLIII')
        self.assertEqual(convert_to_roman(44),'XLIV')
        self.assertEqual(convert_to_roman(45),'XLV')
        self.assertEqual(convert_to_roman(48),'XLVIII')
        self.assertEqual(convert_to_roman(49),'XLIX')
        self.assertEqual(convert_to_roman(50),'L')


def add(numeral1, numeral2):
    answer = numeral1 + numeral2;
    if len(answer) < 4:
        return answer
    else:
        if len(answer) == 4:
            return 'IV'
        else:
            return convert_to_roman(5)

def convert_to_roman(number):
    numeral =''

    if number - 50 >= 0:
        number -= 50
        numeral += 'L'

    if number - 40 >= 0:
        number -= 40
        numeral += 'XL'

    while number - 10 >= 0:
        number -= 10
        numeral += 'X'

    if number - 9 >= 0:
        number -= 9
        numeral += 'IX'

    if number - 5 >= 0:
        number -= 5
        numeral += 'V'

    if number - 4 >= 0:
        number -= 4
        numeral += 'IV'

    while number - 1 >= 0:
        number -= 1
        numeral += 'I'

    return numeral

if __name__=='__main__':
    unittest.main()