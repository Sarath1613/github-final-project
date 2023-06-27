import unittest
from translator import englishToFrench, frenchToEnglish


class TestenglishToFrench(unittest.TestCase):
    def test1(self):
        # Test that Hello returns Bonjour
        self.assertEqual(englishToFrench('hello'), 'bonjour')
        # Test that Hello does not return Hello
        self.assertNotEqual(englishToFrench('hello'),'hello')
class TestfrenchToEnglish(unittest.TestCase):
    def test1(self):
        # Test Bonjour returns Hello
        self.assertEqual(frenchToEnglish('bonjour'),'hello')
        # Test Bonjour does not return Bonjour
        self.assertNotEqual(frenchToEnglish('bonjour'),'bonjour')
            
if __name__ == '__main__':
    unittest.main()