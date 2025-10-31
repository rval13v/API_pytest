# Импортируем модуль datetime для работы с датой и временем.
import datetime
# Импортируем модуль os для взаимодействия с операционной системой, например, для получения переменных окружения.
import os

# Импортируем класс Response из библиотеки requests для аннотаций типов.
from requests import Response


# Создаём класс Logger для ведения логов.
class Logger:

    # Определяем переменную класса, которая будет хранить имя файла лога.
    # Имя файла формируется с использованием текущей даты и времени для уникальности.
    file_name = f"logs/log_" + str(datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")) + ".log"

    # Определяем метод класса, который записывает данные в файл.
    @classmethod
    def write_log_to_file(cls, data: str):
        # Открываем файл в режиме добавления ('a') с указанием кодировки UTF-8,
        # чтобы избежать проблем с русскими символами.
        with open(cls.file_name, 'a', encoding='utf=8') as logger_file:
            # Записываем данные в файл.
            logger_file.write(data)

    # Определяем метод класса для добавления информации о запросе в лог.
    @classmethod
    def add_request(cls, url: str, method: str):
        # Получаем имя текущего теста из переменной окружения.
        test_name = os.environ.get('PYTEST_CURRENT_TEST')

        # Формируем строку с информацией о запросе.
        data_to_add = f"\n-----\n"
        data_to_add += f"Test: {test_name}\n"
        data_to_add += f"Time: {str(datetime.datetime.now())}\n"
        data_to_add += f"Request method: {method}\n"
        data_to_add += f"Request URL: {url}\n"
        data_to_add += "\n"

        # Записываем сформированную строку в файл лога.
        cls.write_log_to_file(data_to_add)

    # Определяем метод класса для добавления информации об ответе в лог.
    @classmethod
    def add_response(cls, result: Response):
        # Преобразуем cookies из объекта ответа в словарь.
        cookies_as_dict = dict(result.cookies)
        # Преобразуем заголовки из объекта ответа в словарь.
        headers_as_dict = dict(result.headers)

        # Формируем строку с информацией об ответе.
        data_to_add = f"Response code: {result.status_code}\n"
        data_to_add += f"Response text: {result.text}\n"
        data_to_add += f"Response headers: {headers_as_dict}\n"
        data_to_add += f"Response cookies: {cookies_as_dict}\n"
        data_to_add += f"\n-----\n"

        # Записываем сформированную строку в файл лога.
        cls.write_log_to_file(data_to_add)
