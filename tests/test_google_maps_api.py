from requests import  Response

from utils.api import GoogleMapsApi


class TestCreatePlace():

    def test_create_new_place(self):

        print('Метод POST')
        result_post: Response = GoogleMapsApi.create_new_place()