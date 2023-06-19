import unittest

from deep_translator import MyMemoryTranslator
from translator import englishToFrench, frenchToEnglish

class TestE2F(unittest.TestCase):
    def test1(self):
        # Test that Hello returns Bonjour
        self.assertEqual(englishToFrench('hello'), 'bonjour')
        # Test that Hello does not return Hello
        self.assertNotEqual(englishToFrench('hello'),'hello')
class TestF2E(unittest.TestCase):
    def test2(self):
        # Test Bonjour returns Hello
        self.assertEqual(frenchToEnglish('bonjour'),'hello')
        # Test Bonjour does not return Bonjour
        self.assertNotEqual(frenchToEnglish('bonjour'),'bonjour')
            
if __name__ == '__main__':
    unittest.main()
