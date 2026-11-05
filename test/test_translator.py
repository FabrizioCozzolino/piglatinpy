from unittest import TestCase

from src.translator import PigLatinTranslator


class TestPigLatinTranslator(TestCase):

    def test_get_phrase(self):
        translator = PigLatinTranslator("hello world")
        phrase = translator.get_phrase()
        self.assertEqual("hello world", phrase)

    def test_translate_empty_phrase(self):
        translator = PigLatinTranslator("")
        translation = translator.translate()
        self.assertEqual("nil", translation)

    def test_translate_word_starting_with_a_vowel_end_with_y(self):
        translator = PigLatinTranslator("any")
        translation = translator.translate()
        self.assertEqual("anynay", translation)

    def test_translate_word_starting_with_a_vowel_end_with_y_2(self):
        translator = PigLatinTranslator("enemy")
        translation = translator.translate()
        self.assertEqual("enemynay", translation)

    def test_translate_word_starting_with_a_vowel_end_with_vowel(self):
        translator = PigLatinTranslator("apple")
        translation = translator.translate()
        self.assertEqual("appleyay", translation)

    def test_translate_word_starting_with_a_vowel_end_with_consonant(self):
        translator = PigLatinTranslator("ask")
        translation = translator.translate()
        self.assertEqual("askay", translation)

    def test_translate_word_starting_with_a_single_consonant_H(self):
        translator = PigLatinTranslator("hello")
        translation = translator.translate()
        self.assertEqual("ellohay", translation)

    def test_translate_word_starting_with_a_single_consonant_W(self):
        translator = PigLatinTranslator("word")
        translation = translator.translate()
        self.assertEqual("ordway", translation)

    def test_translate_word_starting_with_double_consonant(self):
        translator = PigLatinTranslator("known")
        translation = translator.translate()
        self.assertEqual("ownknay", translation)

    def test_translate_word_starting_with_three_consonant(self):
        translator = PigLatinTranslator("spring")
        translation = translator.translate()
        self.assertEqual("ingspray", translation)

    def test_translate_word_with_only_consonant(self):
        translator = PigLatinTranslator("fly")
        translation = translator.translate()
        self.assertEqual("flyay", translation)