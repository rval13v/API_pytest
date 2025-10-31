import json
from requests import Response


class Checking:

    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code, \
            f"Провал. Ожидаемый статус код: {status_code}, Фактический: {response.status_code}."
        print("Успешно. Статус код = " + str(response.status_code))

    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print("Все поля присутсвуют!")

    @staticmethod
    def check_json_value(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(field_name + ' верен!')

    @staticmethod
    def check_json_search_word_in_value(response: Response, field_name, search_word):
        check = response.json()
        check_info = check.get(field_name)
        assert search_word in check_info, \
            f"Провал. Слово {search_word} отсутствует в поле {field_name}. Фактическое значение: {check_info}"
        print("Слово " + search_word + " присутствует.")
