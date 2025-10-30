import requests  # Импортируем библиотеку requests для выполнения HTTP-запросов.

from utils.logger import Logger

# Создали класс HTTP_methods, который будет содержать статические методы
# для отправки различных типов HTTP-запросов (GET, POST, PUT, DELETE).
class HTTPMethods:
    # Определяем атрибут класса headers (заголовки), которые будут
    # использоваться во всех запросах. Content-Type: application/json
    # указывает, что мы отправляем и ожидаем данные в формате JSON.
    headers = {'Content-Type': 'application/json'}

    # Определяем атрибут класса cookie для хранения куки.
    # В данном случае он пуст, но его можно было бы заполнить
    # для отправки куки с запросами.
    cookie = ""

    # @staticmethod — это декоратор, который объявляет, что следующий метод
    # является статическим. Это означает, что метод принадлежит классу, а не
    # конкретному экземпляру класса. Ему не нужен доступ к self или cls.
    @staticmethod
    def get(url):
        # Отправляем GET-запрос по указанному URL.
        # Используем заголовки и куки, определенные как атрибуты класса.
        Logger.add_request(url, method="GET")
        result = requests.get(url, headers=HTTPMethods.headers, cookies=HTTPMethods.cookie)
        Logger.add_response(result)
        # Возвращаем объект ответа (Response object), который содержит
        # всю информацию о результате запроса.
        return result

    @staticmethod
    def post(url, body):
        Logger.add_request(url, method="POST")
        # Отправляем POST-запрос по указанному URL.
        # Параметр json=body автоматически сериализует
        # словарь body в строку JSON и отправляет её в теле запроса.
        result = requests.post(url, json=body, headers=HTTPMethods.headers, cookies=HTTPMethods.cookie)
        Logger.add_response(result)
        return result

    @staticmethod
    def put(url, body):
        Logger.add_request(url, method="PUT")
        # Отправляем PUT-запрос по указанному URL.
        # Как и в случае с POST, данные в body сериализуются в JSON.
        result = requests.put(url, json=body, headers=HTTPMethods.headers, cookies=HTTPMethods.cookie)
        Logger.add_response(result)
        return result

    @staticmethod
    def delete(url, body):
        Logger.add_request(url, method="DELETE")
        # Отправляем DELETE-запрос по указанному URL.
        # Хотя DELETE-запросы часто не имеют тела, иногда оно используется,
        # поэтому здесь предусмотрена возможность его передачи.
        result = requests.delete(url, json=body, headers=HTTPMethods.headers, cookies=HTTPMethods.cookie)
        Logger.add_response(result)
        return result
