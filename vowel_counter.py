def count_vowels(text):
    """
    Подсчитывает количество гласных букв в строке.
    
    Args:
        text (str): Входная строка для анализа
        
    Returns:
        int: Количество гласных букв в строке
    """
    vowels = 'аеёиоуыэюяАЕЁИОУЫЭЮЯaeiouAEIOU'
    count = 0
    
    for char in text:
        if char in vowels:
            count += 1
    
    return count


# Тесты для функции
def test_count_vowels():
    """Тестирует функцию count_vowels с различными случаями."""
    
    # Тест 1: Строка, содержащая только гласные
    assert count_vowels('аеиоу') == 5, "Ошибка: должно быть 5 гласных в 'аеиоу'"
    assert count_vowels('aeiou') == 5, "Ошибка: должно быть 5 гласных в 'aeiou'"
    assert count_vowels('АЕЁИОУЫЭЮЯ') == 10, "Ошибка: должно быть 10 гласных в 'АЕЁИОУЫЭЮЯ'"
    
    # Тест 2: Строка без гласных
    assert count_vowels('бвгджз') == 0, "Ошибка: должно быть 0 гласных в 'бвгджз'"
    assert count_vowels('bcdfgh') == 0, "Ошибка: должно быть 0 гласных в 'bcdfgh'"
    assert count_vowels('1234567890') == 0, "Ошибка: должно быть 0 гласных в '1234567890'"
    assert count_vowels('!@#$%^&*()') == 0, "Ошибка: должно быть 0 гласных в '!@#$%^&*()'"
    
    # Тест 3: Смешанные строки с прописными и строчными буквами
    assert count_vowels('Привет мир!') == 3, "Ошибка: должно быть 3 гласных в 'Привет мир!'"
    assert count_vowels('Hello World') == 3, "Ошибка: должно быть 3 гласных в 'Hello World'"
    assert count_vowels('Программирование') == 7, "Ошибка: должно быть 7 гласных в 'Программирование'"
    assert count_vowels('Programming') == 3, "Ошибка: должно быть 3 гласных в 'Programming'"
    
    # Тест 4: Пустая строка
    assert count_vowels('') == 0, "Ошибка: должно быть 0 гласных в пустой строке"
    
    # Тест 5: Строка с повторяющимися гласными
    assert count_vowels('ааааа') == 5, "Ошибка: должно быть 5 гласных в 'ааааа'"
    assert count_vowels('eee') == 3, "Ошибка: должно быть 3 гласных в 'eee'"
    
    print("Все тесты прошли успешно!")


if __name__ == "__main__":
    # Запускаем тесты
    test_count_vowels()
    
    # Демонстрация работы функции
    print("\nДемонстрация работы функции:")
    test_cases = [
        "аеиоу",
        "бвгджз", 
        "Привет мир!",
        "Hello World",
        "Программирование",
        "Programming",
        "",
        "ааааа"
    ]
    
    for test_case in test_cases:
        result = count_vowels(test_case)
        print(f"'{test_case}' -> {result} гласных") 