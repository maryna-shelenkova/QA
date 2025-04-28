import requests
import os
from dotenv import load_dotenv

load_dotenv()

class TestEmployeeApi:
    base_url = "http://5.101.50.27:8000"
    client_token = os.getenv("CLIENT_TOKEN")

    if not client_token:
        raise ValueError("CLIENT_TOKEN не найден в переменных окружения")


    def test_user_create(self):
        data_json = {
            "first_name": "Марина",
            "last_name": "Шеленкова",
            "middle_name": "Александровна",
            "company_id": 1,
            "email": "net@net.net",
            "phone": "+49123456789",
            "birthdate": "1983-07-28",
            "is_active": True
        }

        response = requests.post(f"{self.base_url}/employee/create", json=data_json)
        assert response.status_code == 200
        assert response.json().get('email') == data_json['email']
    def test_user_info(self):
        user_id = 9
        response = requests.get(f"{self.base_url}/employee/info", params={"id": user_id})
        assert response.status_code == 200
        assert response.json().get('id') == user_id


    def test_user_update(self):
        data_json = {
            "company_id": 1,
            "email": "net1@net.net",
            "phone": "+49987654321",
        }

        headers = {
            'Authorization': f'Bearer {self.client_token}'
        }

        user_id = 1
        response = requests.patch(
            f"{self.base_url}/employee/change/{user_id}",
            json=data_json,
            headers=headers
        )
        assert response.status_code == 200
