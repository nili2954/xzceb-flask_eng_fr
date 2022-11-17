import unittest

from translator import english_to_french, french_to_english

class TestMyTranslator(unittest.TestCase):
    def test_englishtofrench(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
    
    def test_frenchtoenglish(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

if __name__=='__main__':
    unittest.main()
    