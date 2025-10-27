from requests import Response
from utils.api import GoogleMapsApi


class TestCreatePlace:
    def test_create_new_place(self):
        print('Метод POST')
        result_post: Response = GoogleMapsApi.create_new_place()

        print(f'Статус-код: {result_post.status_code}')
        assert result_post.status_code == 200
        print('Стату-код POST корректен')

        # Получаем данные из JSON-ответа.
        check_response_post = result_post.json()

        # Проверяем, что поле status в ответе имеет значение OK.
        status = check_response_post.get('status')
        print(status)
        assert status == 'OK'
        print('Поле Status корректно')

        place_id = check_response_post.get("place_id")

        #________GET после POST____________________________________
        print('\nМетод GET после POST')
        result_get: Response = GoogleMapsApi.get_new_place(place_id)

        print(f'Статус-код: {result_get.status_code}')
        assert 200 == result_get.status_code
        print('Стату-код GET POST корректен')

        # ________PUT__________________________________
        print('\nМетод PUT')
        result_put: Response = GoogleMapsApi.put_new_place(place_id)

        print(f'Статус-код: {result_put.status_code}')
        assert 200 == result_put.status_code, f'Статус: {result_put.status_code}, Ошибка, локация не найдена'
        print('Стату-код GET PUT корректен')

        check_response_put = result_put.json()
        msg = check_response_put.get('msg')
        print(msg)
        assert msg == 'Address successfully updated'
        print('Поле MSG корректно')

        # ________GET (после PUT)__________________________________
        print('\nМетод GET (после PUT)')
        result_get_after_put: Response = GoogleMapsApi.get_new_place(place_id)
        print(f'Статус-код: {result_get_after_put.status_code}')
        assert 200 == result_get_after_put.status_code
        print('Стату-код GET после PUT корректен')

        check_response_get_after_put = result_get_after_put.json()
        actual_address = check_response_get_after_put.get('address')
        print(f"Фактический адрес после обновления: {actual_address}")
        assert actual_address == "100 Lenina street, RU"
        print('Адрес изменился')

