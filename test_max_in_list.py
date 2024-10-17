# Файл с тестами для функции поиска максимума

from student_code import max_in_list  # Импортируем функцию студента

def test_max_in_positive_list():
    assert max_in_list([1, 2, 3, 4, 5]) == 5, "Максимум в списке [1, 2, 3, 4, 5] должен быть 5"

def test_max_in_negative_list():
    assert max_in_list([-1, -2, -3, -4, -5]) == -1, "Максимум в списке [-1, -2, -3, -4, -5] должен быть -1"

def test_max_in_mixed_list():
    assert max_in_list([1, -2, 3, 0, -5]) == 3, "Максимум в смешанном списке должен быть 3"

def test_max_in_single_element_list():
    assert max_in_list([10]) == 10, "В списке из одного элемента максимум должен быть сам элемент"
