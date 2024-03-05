def to_uppercase(input_string):
    """
    Преобразует строку в верхний регистр.

    input_string это Входная строка, которую нужно преобразовать в верхний регистр.

    Возвращает:
    str это Строка в верхнем регистре.
    """
    return input_string.upper()
def to_uppercase(input_string):
    """
    Преобразует строку в верхний регистр.

    param input_string это Входная строка.
    return это Строка в верхнем регистре.
    """
    return input_string.upper()

def capitalize_words(input_string):
    """
    Делает заглавными первые буквы каждого слова в строке.

    param input_string это Входная строка.
    return это Строка, в которой первые буквы каждого слова заглавные.
    """
    return ' '.join(word.capitalize() for word in input_string.split())