from requests import  Response
from utils.checking import Checking
from utils.api import GoogleMapsApi


class TestCreatePlace:

    def test_create_new_place(self):
        print('Метод POST')
        result_post: Response = GoogleMapsApi.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get("place_id")
        Checking.check_status_code(result_post, 200)

        print('Метод GET POST')
        result_get: Response = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)

        print('Метод PUT')
        result_put: Response = GoogleMapsApi.put_new_place(place_id)
        Checking.check_status_code(result_put, 200)

        print('Метод GET PUT')
        result_get: Response = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)

        print('Метод DELETE')
        result_delete: Response = GoogleMapsApi.delete_new_place(place_id)
        Checking.check_status_code(result_delete, 200)

        print('Метод GET DELETE')
        result_get: Response = GoogleMapsApi.get_new_place(place_id)
        Checking.check_status_code(result_get, 404)