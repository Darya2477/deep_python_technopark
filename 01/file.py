import re
import logging
import os


def gen(file, params):
    try:
        if (
            type(file).isinstance(str)
            and type(params).isinstance(list)
            and all(isinstance(elem, str) for elem in params)
        ):
            if os.path.isdir(file):
                raise IsADirectoryError
            else:
                file = open(file, "r")
        else:
            raise AttributeError
    except AttributeError:
        logging.error(
            "Пареметр file может быть только файлом или файловым объектом, a params списком строк."
        )
    except IsADirectoryError:
        logging.error(
            "В качестве параметра file, вы передали имя директории, а не файла."
        )
    except FileNotFoundError:
        logging.error(f"Файл {file} не найден.")
    except UnicodeDecodeError:
        logging.error(f"Ошибка декодирования при попытке открыть файл {file}.")
    except PermissionError:
        logging.error(f"Ошибка доступа к файлу {file}.")
    except OSError:
        logging.error(f"Ошибка ввода-вывода при выполнении операции над файлом {file}.")
    except Exception as er:
        logging.error(f"Неизвестная ошибка при работе с файлом {file}", repr(er))
    else:
        try:
            while True:
                data = file.readline()
                if data == "":
                    raise (EOFError)
                for param in params:
                    if (
                        re.search(r"(^|\s)" + param.lower() + r"(\s|$)", data.lower())
                        is not None
                    ):
                        yield data
                        break
        except EOFError:
            logging.info(f"Достигнут конец файла {file.name}")
        except StopIteration:
            logging.error(f"Ошибка итерации при работе с файлом {file.name}.")
        except Exception as er:
            logging.error(
                f"Неизвестная ошибка при работе с файлом {file.name}", repr(er)
            )
        file.close()
