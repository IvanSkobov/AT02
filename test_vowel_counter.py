import unittest
from vowel_counter import count_vowels


class TestVowelCounter(unittest.TestCase):
    """Тесты для функции count_vowels."""
    
    def test_only_vowels(self):
        """Тест: строка, содержащая только гласные."""
        self.assertEqual(count_vowels('аеиоу'), 5)
        self.assertEqual(count_vowels('aeiou'), 5)
        self.assertEqual(count_vowels('АЕЁИОУЫЭЮЯ'), 10)
        self.assertEqual(count_vowels('ааааа'), 5)
        self.assertEqual(count_vowels('eee'), 3)
    
    def test_no_vowels(self):
        """Тест: строка без гласных."""
        self.assertEqual(count_vowels('бвгджз'), 0)
        self.assertEqual(count_vowels('bcdfgh'), 0)
        self.assertEqual(count_vowels('1234567890'), 0)
        self.assertEqual(count_vowels('!@#$%^&*()'), 0)
        self.assertEqual(count_vowels(''), 0)
    
    def test_mixed_strings(self):
        """Тест: смешанные строки с прописными и строчными буквами."""
        self.assertEqual(count_vowels('Привет мир!'), 3)
        self.assertEqual(count_vowels('Hello World'), 3)
        self.assertEqual(count_vowels('Программирование'), 7)
        self.assertEqual(count_vowels('Programming'), 3)
        self.assertEqual(count_vowels('Тестирование кода'), 8)
        self.assertEqual(count_vowels('Code Testing'), 4)
    
    def test_case_sensitivity(self):
        """Тест: проверка регистра букв."""
        self.assertEqual(count_vowels('АаЕеИиОоУу'), 10)
        self.assertEqual(count_vowels('AaEeIiOoUu'), 10)
        self.assertEqual(count_vowels('ПрИвЕт'), 2)
        self.assertEqual(count_vowels('HeLLo'), 2)
    
    def test_special_characters(self):
        """Тест: строки со специальными символами и пробелами."""
        self.assertEqual(count_vowels('Привет, мир!'), 3)
        self.assertEqual(count_vowels('Hello, World!'), 3)
        self.assertEqual(count_vowels('Программирование на Python'), 9)
        self.assertEqual(count_vowels('Programming in Python'), 5)
        self.assertEqual(count_vowels('   а   е   и   '), 3)
    
    def test_numbers_and_symbols(self):
        """Тест: строки с числами и символами."""
        self.assertEqual(count_vowels('123а456'), 1)
        self.assertEqual(count_vowels('abc123def'), 2)
        self.assertEqual(count_vowels('!@#а$%^&*()'), 1)
        self.assertEqual(count_vowels('Программирование 2.0'), 7)


if __name__ == '__main__':
    # Запускаем тесты
    unittest.main(verbosity=2) 