import unittest

from translator import english_to_french, french_to_english

class TestMyTranslator(unittest.TestCase):
    def test_englishtofrench(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
    
    def test_frenchtoenglish(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

    def test_negative_enfr(self):
        firstValue = 'Hello'
        secondValue = 'Bonjour'
        # error message in case if test case got failed
        message = "The translation is not correct!"
        # assertNotEqual() to check unequality of first & second value
        self.assertNotEqual(firstValue, secondValue, message)

    def test_negative_fren(self):
        firstValue = 'Bonjour'
        secondValue = 'Hello'
        # error message in case if test case got failed
        message = "The translation is not correct!"
        # assertNotEqual() to check unequality of first & second value
        self.assertNotEqual(firstValue, secondValue, message)

if __name__=='__main__':
    unittest.main()
    