import requests
import pytest

token_yd = "y0__xCl3ZfkAxjblgMg6vji2BIxb8DFCfuKPCE5yPwcfcKICeyZFA"
BASE_URL = "https://cloud-api.yandex.net/v1/disk/resources"

@pytest.fixture
def create_arg():
    headers = {
                    'Content-Type': 'application/json',
                    'Authorization': token_yd
        }
    temp_folder = '123'
    return headers, temp_folder

def test_create_folder_success(create_arg):
    headers, temp_folder = create_arg
    response = requests.put(BASE_URL, headers=headers, params={'path': f'disk:/{temp_folder}'})
    assert response.status_code in [201, 409]

@pytest.mark.parametrize(
    'headers,create_and_cleanup_folder',
    (
            ({
                    'Content-Type': 'application/json',
                    'Authorization': token_yd
        }, '123'),
    )
)
def test_create_existing_folder(headers, create_and_cleanup_folder):
    folder = create_and_cleanup_folder
    response = requests.put(BASE_URL, headers=headers, params={'path': f'disk:/{folder}'})
    assert response.status_code == 409

@pytest.mark.parametrize(
    'headers',
    (
            ({
                    'Content-Type': 'application/json',
                    'Authorization': token_yd
        }),
    )
)
def test_create_folder_invalid_path(headers):
    response = requests.put(BASE_URL, headers=headers, params={'path': 'disk://///'})
    assert response.status_code == 404
