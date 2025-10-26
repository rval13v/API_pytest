from requests import  Response

from utils.api import GoogleMapsApi


class TestCreatePlace():

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
        #________GET__________________________________
        print('\nМетод GET')
        result_get: Response = GoogleMapsApi.get_new_place(place_id)

        print(f'Статус-код: {result_get.status_code}')
        assert 200 == result_get.status_code
        print('Стату-код GET корректен')




