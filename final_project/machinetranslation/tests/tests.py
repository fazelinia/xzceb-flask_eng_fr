import unittest

from xzceb_flask_eng_fr.final_project.machinetranslation.translator import frenchToEnglish

from xzceb_flask_eng_fr.final_project.machinetranslation.translator import englishToFrench

from machinetranslation import translator

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(englishToFrench(), "") # test the output of englishToFrench function when the input is null.
        self.assertEqual(englishToFrench("Hello"), "Bonjour") # test the output of englishToFrench function when the input is Hello.
        self.assertNotEqual(englishToFrench("Hello"), "Bonjouri")  # test the output is not equal Bonjouri


class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(frenchToEnglish(), "") # test the output of frenchToEnglish function when the input is null.
        self.assertEqual(frenchToEnglish("Bonjour"), "Hello") # test the output of frenchToEnglish function when the input is Hello.
        self.assertNotEqual(frenchToEnglish("Bonjour"), "Hellou")  # test the output is not equal Bonjouri


unittest.main()