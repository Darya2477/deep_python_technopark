from file import gen
import unittest
from unittest.mock import patch
import os


class TestGen(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    # ТЕСТ НА ОТКРЫТИЕ НЕСУЩЕСТВУЮЩЕГО ФАЙЛА
    @patch("file.logging.error")
    def test_file_not_exist(self, error_mock):
        for i in gen("file_not_exist.txt", ["param1", "param2"]):
            pass
        error_mock.assert_called_once_with("Файл file_not_exist.txt не найден.")

    # ТЕСТ "ПАРАМЕТР file ЯВЛЯЕТСЯ ДИРЕКОРИЕЙ"
    @patch("file.logging.error")
    def test_directory_instead_file(self, error_mock):
        os.mkdir("folder")
        for i in gen("folder", ["param1", "param2"]):
            pass
        error_mock.assert_called_once_with(
            "В качестве параметра file, вы передали имя директории, а не файла."
        )
        os.rmdir("folder")

    # ТЕСТ НА ПРАВА ДОСТУПА
    @patch("file.logging.error")
    def test_no_permissions(self, error_mock):
        with open("file_with_no_permissions.txt", "r"):
            pass
        with open("file_with_no_permissions.txt", "r"):
            os.system("chmod a-rwx file_with_no_permissions.txt")
            with open("file_with_no_permissions.txt", "r"):
                pass
            for i in gen("file_with_no_permissions.txt", ["param1", "param2"]):
                pass
            os.chmod("file_with_no_permissions.txt", 0o000)
            with open("file_with_no_permissions.txt", "w"):
                pass
            error_mock.assert_called_once_with(
                "Ошибка доступа к файлу file_with_no_permissions.txt."
            )
        os.remove("file_with_no_permissions.txt")

    # ТЕСТ НА НЕПРАВИЛЬНУЮ ПЕРЕДАЧУ ПАРАМЕТРА file В ФУНКЦИЮ
    @patch("file.logging.error")
    def test_not_correct_file(self, error_mock):
        for i in gen(123, ["param1", "param2"]):
            pass
        error_mock.assert_called_once_with(
            "Пареметр file может быть только файлом или файловым объектом, a params списком строк."
        )

    # ТЕСТ НА НЕПРАВИЛЬНУЮ ПЕРЕДАЧУ ПАРАМЕТРА params В ФУНКЦИЮ №1
    @patch("file.logging.error")
    def test_not_correct_params(self, error_mock):
        for i in gen("text.txt", 456):
            pass
        error_mock.assert_called_once_with(
            "Пареметр file может быть только файлом или файловым объектом, a params списком строк."
        )

    # ТЕСТ НА НЕПРAВИЛЬНУЮ ПЕРЕДАЧУ ПАРАМЕТРА params В ФУНКЦИЮ №2
    @patch("file.logging.error")
    def test_not_correct_elements_in_params(self, error_mock):
        for i in gen("text.txt", ["text", 456, 9.043, {"key": 66}]):
            pass
        error_mock.assert_called_once_with(
            "Пареметр file может быть только файлом или файловым объектом, a params списком строк."
        )

    # ТЕСТ НА НЕПРАВИЛЬНУЮ КОДИРОВКУ
    @patch("file.logging.error")
    def test_uncorrect_encodding(self, error_mock):
        with open("file_with_uncorrect_encoding.txt", "w") as file:
            file.write("Ђ[ж5АІњ№5Lьn•CU5‘ф{І«@ј|¤ьЂџoYlэ2")
            for i in gen(file, ["param1, param2"]):
                pass
        os.remove("file_with_uncorrect_encoding.txt")

    # ТЕСТ НА ВЫХОД ЗА ГРАНИЦУ ГЕНЕРАТОРА
    def test_empty_file(self):
        with open("empty_file.txt", "w"):
            pass
        generator = gen("empty_file.txt", ["param1", "param2"])
        self.assertRaises(StopIteration, next, generator)
        os.remove("empty_file.txt")

    # ТЕСТ НА ПЕРЕДАЧУ ФАЙЛА В ФУНКЦИЮ
    def test_file_input(self):
        try:
            gen("./text.txt", ["search_term"])
        except Exception as e:
            self.fail(f"gen raised an exception: {e}")

    # ТЕСТ НА ПЕРЕДАЧУ ФАЙЛОВОГО ОБЪЕКТА В ФУНКЦИЮ
    def test_file_object_input(self):
        try:
            file = open("./text.txt")
            gen(file, ["search_term"])
        except Exception as e:
            self.fail(f"gen raised an exception: {e}")

    # ТЕСТ НА ПОИСК СТРОК С УЧЕТОМ РЕГИСТРА
    def test_case_sensitive_search(self):
        with open("./text.txt", "w") as file:
            file.write("This is a test line\n")
        results = list(gen("./text.txt", ["This"]))
        self.assertEqual(results, ["This is a test line\n"])

    # ТЕСТ НА ПОИСК СТРОК БЕЗ УЧЕТА РЕГИСТРА
    def test_case_insensitive_search(self):
        with open("./text.txt", "w") as file:
            file.write("This is a test line\n")
        results = list(gen("./text.txt", ["this"]))
        self.assertEqual(results, ["This is a test line\n"])

    # ТЕСТ НА ПРОВЕРКУ ПОЛНОГО СОВПАДЕНИЯ СЛОВА
    def test_exact_match(self):
        with open("./text.txt", "w") as file:
            file.write("This is a test line\n")
        results = list(gen("./text.txt", ["this is a test line"]))
        self.assertEqual(results, ["This is a test line\n"])

    # ТЕСТ "НЕТ РЕЗУЛЬТАТОВ"
    def test_no_results(self):
        with open("./text.txt", "w") as file:
            file.write("This is a test line\n")
        results = list(gen("./text.txt", ["another"]))
        self.assertEqual(results, [])
